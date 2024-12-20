import pandas as pd

def load_csv(file_path):
    """
    Loads a CSV file into a pandas DataFrame.
    :param file_path: Path to the CSV file.
    :return: pandas DataFrame
    :raises: FileNotFoundError, pd.errors.EmptyDataError
    """
    try:
        df = pd.read_csv(file_path, index_col=False)
        df = df[df.work_year == 2022]
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        print(f"Error loading CSV file: {e}")
        raise