import os
import pandas as pd
import sys

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
project_root = os.path.abspath(os.path.join(current_dir, '../..'))

print(project_root)

@dataclass
class ExtractDataConfig:
    train_data_path = str=os.path.join(project_root,'datafiles/train.csv')
    test_data_path = str=os.path.join(project_root,'datafiles/test.csv')
    data_path = str=os.path.join(project_root,'datafiles/data.csv')

class ExtractData:
    def __init__(self):
        self.path_files = ExtractDataConfig()

    def initiate_data_extraction(self):
        try:
            df = pd.read_csv(os.path.join(project_root,'dataset/data.csv'))
            os.makedirs(os.path.join(project_root,os.path.dirname(self.path_files.data_path)),exist_ok=True)
            df.to_csv(self.path_files.data_path,index=False)

            training_set, test_set = train_test_split(df,test_size=0.2,random_state=42)
            training_set.to_csv(self.path_files.train_data_path,index=False)
            test_set.to_csv(self.path_files.test_data_path,index = False)

            return(
                self.path_files.test_data_path,
                self.path_files.train_data_path
            )
        except Exception as e:
            print(e)
            raise Exception
if __name__ == '__main__':
    extract = ExtractData()
    train_path,test_path = extract.initiate_data_extraction()