import numpy as np

def ten_years_step (t_matrix, count_matrix) -> np.ndarray:
    count_matrix[1][0] = t_matrix[0][0]*count_matrix[0][0] + t_matrix[1][0]*count_matrix[0][1] + t_matrix[2][0]*count_matrix[0][2] + t_matrix[3][0]*count_matrix[0][3] 
    count_matrix[1][1] = t_matrix[0][1]*count_matrix[0][0] + t_matrix[1][1]*count_matrix[0][1] + t_matrix[2][1]*count_matrix[0][2] + t_matrix[3][1]*count_matrix[0][3]
    count_matrix[1][2] = t_matrix[0][2]*count_matrix[0][0] + t_matrix[1][2]*count_matrix[0][1] + t_matrix[2][2]*count_matrix[0][2] + t_matrix[3][2]*count_matrix[0][3]
    count_matrix[1][3] = t_matrix[0][3]*count_matrix[0][0] + t_matrix[1][3]*count_matrix[0][1] + t_matrix[2][3]*count_matrix[0][2] + t_matrix[3][3]*count_matrix[0][3]
    return count_matrix