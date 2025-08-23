# Databricks notebook source
# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# MAGIC %pip install pytest
# MAGIC %pip install pytest-cov

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import sys
import pytest
import os

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

sys.path.append(".")

retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."

# COMMAND ----------

retcode = pytest.main(
    [".", "-v", "-p", "no:cacheprovider", "--disable-warnings", "-m", "sample"]
)

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."

# COMMAND ----------

retcode = pytest.main(
    [
        ".",
        "-v",
        "-p",
        "no:cacheprovider",
        "--disable-warnings",
        "--cov=tests/",
        "--cov-report=term-missing"
    ]
)

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."

# Remove the coverage file, not sure how to suppress this.
os.remove(".coverage")

# COMMAND ----------

