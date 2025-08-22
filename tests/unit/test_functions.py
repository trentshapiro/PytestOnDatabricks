import pytest
from pyspark.sql import DataFrame
from src.utils.functions import sample_function

@pytest.mark.sample
@pytest.mark.unit
def test_sample_function(sample_df: DataFrame) -> None:
    ret = sample_function(sample_df).select("row_number").collect()
    assert {i["row_number"] for i in ret} == {0, 1}