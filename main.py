import csv_file_treatment as csv


if __name__ == '__main__':
    columns = ['1990', '2000']
    df = csv.read_csv('HDI.csv')
    df = csv.select_range_rows(df, columns, '..')
    df = csv.values_treatment(df, columns)
    array = csv.get_count_class(df, columns)
    #print(df)
    print(array)