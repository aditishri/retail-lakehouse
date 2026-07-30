from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum, avg

spark = (
    SparkSession.builder
    .appName("Retail Gold Layer")
    .getOrCreate()
)

silver = spark.read.parquet("/app/data/silver/orders")

gold = (
    silver
    .groupBy("status")
    .agg(
        count("*").alias("total_orders"),
        sum("total_amount_cents").alias("total_revenue_cents"),
        avg("total_amount_cents").alias("avg_order_value_cents")
    )
)

gold.show(truncate=False)

gold.write.mode("overwrite").parquet("/app/data/gold/orders")

print("Gold layer created successfully!")

spark.stop()