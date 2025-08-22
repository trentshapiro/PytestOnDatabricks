from pyspark.sql import DataFrame
from pyspark.sql.functions import monotonically_increasing_id


def sample_function(df: DataFrame) -> DataFrame:
    return df.withColumn("row_number", monotonically_increasing_id())