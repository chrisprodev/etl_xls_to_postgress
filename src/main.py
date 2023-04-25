from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

#print(os.getenv('HOST'))

# Extract
def extract():
    try:
        directory = 'src/data'
        for filename in os.listdir(path=directory):
            filename_clean = os.path.splitext(filename)[0]

            # only excel files
            if filename.endswith('.xlsx'):
                print(f'Extrating: {filename}')
                filename_path = os.path.join(directory, filename)

                df = pd.read_excel(filename_path)
                transform(df, filename_clean)
            
    except Exception as ex:
        print('Something went wrong extracting: ' + str(ex))


# Transform
def transform(df, filename):
    try:            
        print(f'Transforming: {filename}')
        df_clean = df[['Segment', 'Country', 'Product', 'Gross Sales', 'Discounts',
        ' Sales', 'COGS', 'Profit', 'Date']].copy()
        countries = ['United States of America', 'Mexico', 'Canada']
        df_clean = df_clean[df_clean['Country'].isin(countries)]
        load(df_clean, filename)
    except Exception as ex:
        print('Something went wrong transforming: ' + str(ex))

# Load
def load(df, filename):
    try:
        print(f'Loading: {filename}')
        print(df)
    except Exception as ex:
        print('Loading fail, filename: ' + str(ex))

extract()