import pandas as pd
import os
from datetime import datetime

def read_csv():
    script_directory = os.path.dirname(__file__)
    # /scripts -> ../ -> /data -> customers-100.csv
    df = pd.read_csv(os.path.join(script_directory,'..','data', 'customers-100.csv'))
    print("CSV file is read")
    return df

def filter_columns(df):
    columns_to_exclude = ['Index','Phone 2']
    df = df.drop(columns=columns_to_exclude)
    print("Unnecessary columns are dropped")
    return df

def define_data_types(df):
    # convert subscription date to datetime (keep as datetime for filtering)
    df['Subscription Date'] = pd.to_datetime(df['Subscription Date'], format="%Y-%m-%d")
    print("Data types are defined")
    return df

def filter_data(df):
    # Country that starts with United
    df = df[df['Country'].str.lower().str.startswith('united')] 
    # filter by subscription date where year is greater than 2020
    df = df[df['Subscription Date'].dt.year > 2020]
    print("CSV data is filtered based on country and subscription date")
    return df

def format_dates(df):
    # Convert datetime to string format AFTER filtering
    df['Subscription Date'] = df['Subscription Date'].dt.strftime("%m-%d-%Y")
    print("Dates formatted to string")
    return df

def write_csv(df):
    script_directory = os.path.dirname(__file__)
    # Create the output directory path: /scripts -> ../ -> /dags -> /data -> /output
    output_dir = os.path.join(script_directory, '..', 'data', 'output')
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create the full file path
    output_path = os.path.join(output_dir, f'customers-100-{datetime.now().strftime("%m-%d-%Y_%H-%M-%S")}.csv')
    df.to_csv(output_path, index=True)
    print(f"CSV file written to {output_path}")

def main():
    df = read_csv()
    df = filter_columns(df)
    df = define_data_types(df)
    df = filter_data(df)
    df = format_dates(df)
    write_csv(df)
    return df

if __name__ == '__main__':
    main()