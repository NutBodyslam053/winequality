import os
from mlProject import logger
from mlProject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Splited data: Train set = {}, Test set = {}".format(train.shape, test.shape))