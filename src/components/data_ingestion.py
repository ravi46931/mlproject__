## It has all the codes related to reading the data
import os
import sys

from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact',"train.csv") #All the output will be stored here,It save all the files in this path 
    test_data_path: str = os.path.join('artifact',"test.csv") #All the output will be stored here,It save all the files in this path 
    raw_data_path: str = os.path.join('artifact',"data.csv") #Initial path

# If we define only variables then we need dataclass

# But if we have some other function then go with constructor part __init__
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

# When DataIngestion is called then ingestion_config save the path of train_data_path, test_data_path, raw_data_path
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component ")
        try:
            df=pd. read_csv('notebook\data\stud.csv')
            logging. info('Read the dataset as dataframe')
            os. makedirs (os. path. dirname (self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv ( self. ingestion_config. raw_data_path, index=False, header=True)
            

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
    # train_data,test_data=obj.initiate_data_ingestion()

    # data_transformation=DataTransformation()
    # train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # modeltrainer=ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
