from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Retail Bronze Layer")
    .getOrCreate()
)

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "orders")
    .option("startingOffsets", "earliest")
    .load()
)

bronze = df.selectExpr(
    "CAST(value AS STRING) AS json",
    "timestamp"
)

query = (
    bronze.writeStream
    .format("parquet")
    .option("path", "/app/data/bronze/orders")
    .option("checkpointLocation", "/app/data/checkpoints/orders")
    .outputMode("append")
    .start()
)

query.awaitTermination()