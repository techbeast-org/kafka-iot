import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import scala.sys.env
import java.util.Properties
import org.apache.spark.sql.DataFrame

val pg_username = env("pg_username")
val pg_password = env("pg_password")
val host = env("host")
val driver = "org.postgresql.Driver"
val mode = "append"
val sslmode = "require"
val url = s"jdbc:postgresql://'$host':5432/postgres"


val connectionProperties = new Properties()
connectionProperties.setProperty("Driver", driver)
connectionProperties.setProperty("user", pg_username)
connectionProperties.setProperty("password", pg_password)
// connectionProperties.setProperty("sslmode", sslmode)

val username = env("username")
val password = env("password")
val df = spark.readStream 
.format("kafka") 
.option("kafka.bootstrap.servers", "pkc-921jm.us-east-2.aws.confluent.cloud:9092") 
.option("kafka.security.protocol", "SASL_SSL") 
.option("kafka.sasl.mechanism", "PLAIN") 
.option("kafka.sasl.jaas.config", s"kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username='$username' password='$password';")
.option("subscribe", "topic_0") 
.option("startingOffsets", "earliest") 
.load()
val schema = ArrayType(new StructType()
.add("temperature", StringType))

val val_df = df
    .withColumn("timestamp",$"timestamp".cast("timestamp"))
    .withColumn("room",$"key".cast(StringType))
    .withColumn("temp",explode(from_json($"value".cast("string"),schema)))
    .withColumn("temperature", $"temp.temperature".cast("string"))

    .select("timestamp","room","temperature")
// display(val_df)

// Aggregation Logic
val groupCols = List("Room")
val cols = groupCols.map(col) ++ Seq(window($"timestamp", "20 second"))
val tumblingWindowDF = val_df
//       .groupBy(window(df.col("eventdatetime"),"1 minute"))
      .withWatermark("timestamp", "20 second")
      .groupBy(cols: _*)
      .agg(avg("temperature").as("avg_temperature"))
      .withColumn("timestamp",$"window.start")
      .select("timestamp","Room","avg_temperature").na.drop()
display(tumblingWindowDF)
val_df.writeStream.foreachBatch { (batchDF: DataFrame, batchId: Long) =>
  batchDF.write.mode(SaveMode.Append).jdbc(url=url, table="iot_telemetry", connectionProperties=connectionProperties)
}.start()