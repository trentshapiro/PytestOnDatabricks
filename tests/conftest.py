import pytest
from pyspark.sql import SparkSession, DataFrame
from databricks.connect import DatabricksSession
from typing import Generator

@pytest.fixture(scope="session")
def spark() -> Generator[SparkSession]:
    try:
        spark = DatabricksSession.builder.serverless().getOrCreate()
    except:
        spark = SparkSession.builder.getOrCreate()
    yield spark


@pytest.fixture
def sample_df(spark) -> DataFrame:
    return spark.createDataFrame([(1, "a"), (2, "b")], ["id", "value"])