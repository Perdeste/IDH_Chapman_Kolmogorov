import csv_file_treatment as csv
import os
import sys
import equacoesCK as eck


def get_abspath(file_name: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', file_name)


def get_attributes() -> tuple:
    if len(sys.argv) >= 3:
        return (sys.argv[1], sys.argv[2:])
    else:
        print(f'{4 - len(sys.argv)} valores faltantes. Iniciando com valores padrões\n')
        return  ('HDI.csv', ['1990', '2000'])


if __name__ == '__main__':
    file_name, columns_range = get_attributes()
    select_year = '2004'
    result_year = str(int(select_year) + 10)
    try:
        idh_df = csv.read_csv(get_abspath(file_name))
        idh_df = csv.select_range_columns(idh_df, columns_range, '..')
        idh_df = csv.values_treatment(idh_df, columns_range)
        idh_df_select = csv.read_csv(get_abspath(file_name))
        idh_df_select = csv.select_starting_year(idh_df_select, select_year, '..')
        idh_df_select = csv.values_treatment_formula(idh_df_select, select_year)   
        idh_df_result = csv.read_csv(get_abspath(file_name))
        idh_df_result = csv.select_starting_year(idh_df_result, result_year, '..')
        idh_df_result = csv.values_treatment_formula(idh_df_result, result_year)  
        matriz_transicao = csv.get_count_class(idh_df, columns_range) 
        matriz_resultado = csv.class_count_starting_year(idh_df_select)
        result_count = csv.class_count_starting_year(idh_df_result)
        matriz_resultado = eck.ten_years_step(matriz_transicao, matriz_resultado)
        print(f'Matriz de Transição:\n{matriz_transicao}')
        print(f'Distribuição das classificações do ano de {select_year}:\n{matriz_resultado[0]}')
        print(f'Previsão para {result_year}:\n{matriz_resultado[1]}')
        print(f'Valores reais do ano de {result_year}:\n{result_count[0]}')
    except FileNotFoundError as e:
        print(f'Arquivo "{file_name}" não encontrado')
    except BaseException as e:
        print(f"Erro desconhecido: {str(e)}")
