import requests
from mystrings import *

def test_func():
    print("Hello this is mypandas")
    
def data_scanner(df,column_name,show_sample=False):
    print(df.describe())
    print_text_line(4,"Column scanned: {}".format(column_name))
    print_text_line(1,"Count Row by length in '{}".format(column_name))
    print_text_line(0,df[column_name].str.len().value_counts())
    print_text_line(1,"Count Row by all numbers in '{}".format(column_name))
    print_text_line(0,df[column_name].str.match('[0-9]*$').value_counts())
    if show_sample:
        print(df.loc[df[column_name].str.match('[0-9]*$')])
    print_text_line(1,"Count Row by value in '{}".format(column_name))    
    print_text_line(0,df[column_name].value_counts())

def get_comma_separated_columns(df):
    column_name=[]
    commas_parameter=[]

    for column in df.columns:
        column_name.append(column)
        commas_parameter.append('%s')
        
    column_name =','.join(column_name)
    commas_parameter = ','.join(commas_parameter)
    return [column_name,commas_parameter]

def column_cleaner(df,column_to_clean,column_length=None,column_only_numbers=None,column_allow_special_character=None):    
    row_count = df.shape[0]
    current_row_count = 0
    
    print_text_line(3,"Cleaning column '{}' which contains {} rows".format(column_to_clean,row_count))
    
    if isinstance(column_length,int):
        df = df.loc[df[column_to_clean].str.len()==column_length]
        current_row_count = df.shape[0]
        print_text_line(3,"Before cleaning length, it contains: {} rows\nAfter cleaning length, it contains: {} rows".format(row_count,current_row_count))
    if isinstance(column_only_numbers,bool):
        match column_only_numbers:
            case True:
                df = df.loc[df[column_to_clean].str.match('[0-9]*$')]
            case False:
                df = df.loc[~df[column_to_clean].str.match('[0-9]*$')]
        current_row_count = df.shape[0]
        print_text_line(3,"Before cleaning only numbers, it contains: {} rows\nAfter cleaning only numbers, it contains: {} rows".format(row_count,current_row_count))
    print_text_line(2,"Cleaning finished.")
    return df
        