from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import *

from pyspark.sql.types import StructType, StructField, StringType, TimestampType

spark = (
    SparkSession.builder
    .appName("Retail Silver Layer")
    .getOrCreate()
)

schema = StructType([
    StructField("order_id", StringType()),
    StructField("customer_id", StringType()),

    StructField(
        "items",
        ArrayType(
            StructType([
                StructField("product_id", StringType()),
                StructField("quantity", IntegerType()),
                StructField("unit_price_cents", IntegerType()),
                StructField("line_total_cents", IntegerType())
            ])
        )
    ),

    StructField("status", StringType()),
    StructField("total_amount_cents", IntegerType()),
    StructField("currency", StringType()),
    StructField("order_placed_ts", StringType()),
    StructField("event_id", StringType()),
    StructField("event_ts", StringType())
])


bronze_schema = StructType([
    StructField("json", StringType(), True),
    StructField("timestamp", TimestampType(), True)
])

bronze = (
    spark.readStream
    .schema(bronze_schema)
    .format("parquet")
    .load("/app/data/bronze/orders")
)

silver = (
    bronze
    .withColumn("data", from_json(col("json"), schema))
    .select("data.*")
)

query = (
    silver.writeStream
    .format("parquet")
    .option("path", "/app/data/silver/orders")
    .option(
        "checkpointLocation",
        "/app/data/checkpoints/silver_orders"
    )
    .outputMode("append")
    .start()
)

query.awaitTermination()