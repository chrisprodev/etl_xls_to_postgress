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
                
        return
    except Exception as error:
        print('Something goes wrong: '+ str(error))


# Transform
def transform(df, filename):
    return



# Load