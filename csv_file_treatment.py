import pandas as pd
import numpy as np

def read_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def select_range_rows(df: pd.DataFrame, columns: list, pattern: str) -> tuple:
    start_year = columns[0]
    end_year = columns[1]
    result = df.drop(df[(df[start_year] == pattern) | (df[end_year] == pattern)].index)
    result = result.reset_index()
    result = result.astype({start_year: float, end_year: float})
    return result[[start_year, end_year]]


def values_treatment(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    for column in columns:
        df.loc[(df[column] >= 0.9) & (df[column] < 1), column] = 3
        df.loc[(df[column] >= 0.8) & (df[column] < 0.9) & (df[column] < 1), column] = 2
        df.loc[(df[column] >= 0.5) & (df[column] < 0.8) & (df[column] < 1), column] = 1
        df.loc[df[column] < 0.5, column] = 0  
    result = df.astype({str(columns[0]): int, str(columns[1]): int})
    return result


def get_count_class(df: pd.DataFrame, columns: list) -> np.ndarray:
    matriz = np.zeros((4, 4))
    for i in range(df.shape[0]):
        matriz[df[columns[0]][i], df[columns[1]][i]] += 1
    matriz = (matriz / matriz.sum(axis=1)[:,None])
    matriz[np.isnan(matriz)] = 0
    return matriz
