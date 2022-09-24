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
    try:
        idh_df = csv.read_csv(get_abspath(file_name))
        idh_df2 = csv.read_csv(get_abspath(file_name))
        idh_df = csv.select_range_columns(idh_df, columns_range, '..')
        idh_df2 = csv.select_starting_year(idh_df2, '1990', '..')
        idh_df = csv.values_treatment(idh_df, columns_range)
        idh_df2 = csv.values_treatment_formula(idh_df2, '1990')
        matriz_transicao = csv.get_count_class(idh_df, columns_range)
        matriz_transicao2 = csv.class_count_starting_year(idh_df2)
        matriz_transicao = eck.ten_years_step(matriz_transicao,matriz_transicao2)
        #print(idh_df)
        print(f'Matriz de Transição:\n{matriz_transicao}')
    except FileNotFoundError as e:
        print(f'Arquivo "{file_name}" não encontrado')
    except BaseException as e:
        print(f"Erro desconhecido: {str(e)}")
