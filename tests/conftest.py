import pytest
from pyspark.sql import SparkSession, DataFrame
from databricks.connect import DatabricksSession

@pytest.fixture(scope="session")
def spark() -> SparkSession:
    try:
        spark = DatabricksSession.builder.getOrCreate()
    except:
        spark = SparkSession.builder.getOrCreate()
    yield spark


@pytest.fixture
def sample_df(spark) -> DataFrame:
    return spark.createDataFrame([(1, "a"), (2, "b")], ["id", "value"])