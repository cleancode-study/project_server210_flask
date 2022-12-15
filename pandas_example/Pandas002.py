import seaborn as sns
import pandas as pd


class Pandas002:
    def __init__(self):
        self.titanic_data = sns.load_dataset('titanic')

    def read_titanic_head(self):
        return self.titanic_data.head()

    def update_titanic_head(self, var1):
        self.titanic_data['column_example'] = var1
