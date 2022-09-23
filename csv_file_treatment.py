import pandas as pd
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

def read_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def select_range_columns(df: pd.DataFrame, columns: list, pattern: str) -> tuple:
    start_column = columns[0]
    end_column = columns[1]
    result = df.drop(df[(df[start_column] == pattern) | (df[end_column] == pattern)].index)
    result = result.reset_index()
    result = result.astype({start_column: float, end_column: float})
    return result[[start_column, end_column]]


def values_treatment(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    for column in columns:
        df.loc[(df[column] >= 0.9), column] = 3
        df.loc[(df[column] >= 0.8) & (df[column] < 0.9), column] = 2
        df.loc[(df[column] >= 0.5) & (df[column] < 0.8), column] = 1
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
