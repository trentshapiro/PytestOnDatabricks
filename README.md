# Pytest Repo Template

### Objectives
1. Invoke pytest from inside Databricks Notebooks
2. Serverless compute
3. Handle repository level relative imports within tests
4. Handle pyspark fixtures
5. Handle pytest markers
6. Generate coverage report

### Repo Requirements
1. `Test Runner.ipynb` must be in a location outside of both `src/` and `tests/`
    - putting it inside `tests/` and trying to chdir will break relative imports
2. Serverless Environment <= 2
    - Environments 3 & 4 both break `tests/` imports, I have not been successful in any way to make these envs work

### Optional Setup
1. `conftest.py` is not strictly required, fixtures defined in `tests/conftest.py` can be moved directly into `test_xx.py` files
2. `pytest.ini` is not strictly required, but is convenient to avoid warnings related to custom markers
    - must run `chmod +w pytest.ini` one time after file creation
3. `.coveragerc` is not strictly required for coverage reports, but without the line exclusions you will get false positives on rows
4. I believe `pytest.ini` and `.coveragerc` can be reconciled into a single `pyproject.toml`, but leaving separate here on purpose

## Usage
### Databricks
1. Clone to Databricks workspace
2. Run `Test Runner` notebook

### Local
1. Clone repo
2. `pip install -e .`
3. Create profile entry in `~/.databrickscfg`, set `serverless_compute_id = auto` for serverless
4. Log into databricks connect `databricks auth login -p {profile_name}`
5. `python -m pytest .`