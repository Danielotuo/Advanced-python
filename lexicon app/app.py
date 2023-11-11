import pandas as pd

class Definitions:
    
    def __init__(self, term):
        self.term = term
        
    def get_definition(self):
        df = pd.read_csv("data.csv")
        return tuple(df.loc[df["word"] == self.term]["definition"])
    
    lexicon = Definitions(term = 'sun')
    print(lexicon.get_definition())
    
        