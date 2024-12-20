# test_dsassignment.py
import pandas as pd
import pytest
from dsassignment import load_csv


#This testcase checks if the df returned by load_csv is an instance of pandas.DataFrame
def test_load_valid_csv():
    valid_csv_file = "C:/2025/conda/data_science_job.csv"
    df = load_csv(valid_csv_file)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    assert df.shape == (1622, 12)

#This testcase checks if the dataFrame created is not empty.
def test_csv_check_empty():
    valid_csv_file = "C:/2025/conda/data_science_job.csv"
    df = load_csv(valid_csv_file)
    assert not df.empty

#This testcase checks if the DataFrame has the exact columns names as expected
def test_csv_check_columns():
    valid_csv_file = "C:/2025/conda/data_science_job.csv"
    df = load_csv(valid_csv_file)
    assert list(df.columns) == ["work_year","job_title","job_category",
                                "salary_currency","salary","salary_in_usd",
                                "employee_residence","experience_level",
                                "employment_type","work_setting",
                                "company_location","company_size"]
    
#This testcase checks if the DataFrame has 1622 rows and 12 columns
def test_csv_check_row_col_numbers():
    valid_csv_file = "C:/2025/conda/data_science_job.csv"
    df = load_csv(valid_csv_file)
    assert df.shape == (1622, 12)
    
