# %%
import pandas as pd
import sqlite3
import logging

# %%
# Set up logging configuration to create a log file with fixed name

LOG_FILE = "C:/2025/conda/logs/data_logging.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
# Try connecting to the SQLite database with the fixed name myAssignment.db
try:
    con = sqlite3.connect('C:/2025/conda/myAssignment.db') # Establish a connection to the SQLite database
    logging.info(" [SUCCESS] Database myAssignment connected successfully") # Log success
except:
    logging.exception('[ERROR] Error in connecting to myAssignment database') # Log any connection error

# %%
try:
    # Try reading the input CSV file into a pandas DataFrame
    df_job = pd.read_csv('C:/2025/conda/data_science_job.csv', index_col=False) # Read CSV file into DataFrame
    logging.info("[SUCCESS] CSV file found and data read successfully")  # Log success
except FileNotFoundError as fnf_error:
    logging.error(fnf_error)
    logging.error("Explanation: We cannot load the csv file") # Additional error explanation


# %%
# Try filtering the DataFrame for work_year == 2022
try:
    df_job = df_job[df_job.work_year == 2022] # Filter rows where 'work_year' equals 2022
    logging.info("[SUCCESS] Dataframe filtered with the work_year = 2022 ") # Log success
    df_job  # Ensure DataFrame is updated
    logging.info("[SUCCESS] Dataframe created successfully") # Log creation success
except:
    logging.info("Error in finding record and to write in dataframe") # Print generic error message

# %%
# Try saving the filtered DataFrame to the SQL database
try:
    df_job.to_sql('myassignment', con, if_exists='replace') # Write DataFrame to SQL table
    logging.info("[SUCCESS] SQL database has been updated successfully with the previous dataframe") # Log success
except Exception as e:
    logging.error(f"An error occurred: {e}") # Log exception details
    logging.error("Explanation: We could not load the DataFrame into the SQL database.") # Additional explanation

# %%
# Iterate through each row in the DataFrame df_job which has been created 
try:
    for row in df_job:
    # Update the 'company_size' column to 'Large' where it contains the letter 'L'.
        df_job.loc[df_job['company_size'].str.contains('L', na=False), 'company_size'] = 'Large'
        # Update the 'company_size' column to 'Medium' where it contains the letter 'M'.
        df_job.loc[df_job['company_size'].str.contains('M', na=False), 'company_size'] = 'Medium'
        # Update the 'company_size' column to 'Small' where it contains the letter 'S'.
        df_job.loc[df_job['company_size'].str.contains('S', na=False), 'company_size'] = 'Small'
        # Update the 'salary_currency' column to 'USD' where it contains the string 'us dolars'.
        df_job.loc[df_job['salary_currency'].str.contains('us dolars', na=False), 'salary_currency'] = 'USD'
except Exception as e:
    logging.error(f"An error occurred: {e}")
    logging.error("Error: Could not replace the values in the dataframe.")

# Display the modified DataFrame
df_job

# %%
try:
    # Save the updated DataFrame `df_job` to the SQL database table 'myassignment'.
    df_job.to_sql('myassignment', con, if_exists='replace')
    logging.info("[SUCCESS] SQL database has been updated successfully with new values") # Log success
except Exception as e:
    logging.error(f"An error occurred: {e}")
    logging.error("Explanation: We could not load the DataFrame into the SQL database.")


