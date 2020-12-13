import json
import pickle
import pandas as pd
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *
from pyspark.sql.types import *


if __name__ == "__main__":
    
    files = ['{:0>2}'.format(str(i)) for i in list(range(10, 11))]
    
    with open('text_classifier', 'rb') as training_model:
        model = pickle.load(training_model)
        
    with open('vectorizer', 'rb') as vectorizer:
        count_vector = pickle.load(vectorizer)
        
    for f in files:
        with open('data{name}.json'.format(name = f)) as json_file:
            data = json.load(json_file)

        df = pd.DataFrame(data)
        df.dropna(axis=0, inplace=True)
        df.drop(df[df['comments'].map(len) < 1].index, inplace=True)

        comments = []
        sentiments = []

        for app in df['comments']:
            for item in app:
                try:
                    df = pd.DataFrame({'comments':  [item]}, columns=['comments'])
                    response = model.predict(count_vector.transform(df['comments']))
                    sentiments.append(response[0])    
                    comments.append(item)
                except:
                    # item chua cac ki tu dac biet => None
                    pass

        dict = {'comments': comments, 'sentiments': sentiments}
        df = pd.DataFrame(dict)
        df.to_csv('file{name}.csv'.format(name = f), index=False)

