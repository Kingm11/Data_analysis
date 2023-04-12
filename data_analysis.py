

import pandas as pd

def data_analysis(df):
    # Check for missing values
    if df.isnull().sum().sum() > 0:
        df = df.dropna()
        print('Removed missing values')

    # Check for duplicate rows
    if df.duplicated().sum() > 0:
        df = df.drop_duplicates()
        print('Removed duplicate rows')

    # Calculate statistics
    mean = df.mean()
    mode = df.mode().iloc[0]
    median = df.median()
    std = df.std()

    # Print results
    print(f'Mean:\n{mean}\n')
    print(f'Mode:\n{mode}\n')
    print(f'Median:\n{median}\n')
    print(f'Standard Deviation:\n{std}\n')

    return df





