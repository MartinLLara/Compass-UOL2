import pandas as pd
import numpy as np
actors = pd.read_csv("actors (2).csv")
frequencia= actors["#1 Movie"].value_counts()
print(frequencia.head(1))