import pickle
import pandas as pd

class Sentiment:
    def __init__(self, text):
        self.text = text

    def polarity(self):
        with open('text_classifier', 'rb') as training_model:
            model = pickle.load(training_model)
    
        with open('vectorizer', 'rb') as vectorizer:
            count_vector = pickle.load(vectorizer)
        

        df = pd.DataFrame({'comments':  [self.text]}, columns=['comments'])
        
        response = model.predict(count_vector.transform(df['comments']))

        return response[0]


