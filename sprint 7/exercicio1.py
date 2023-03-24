import pandas as pd
import numpy as np
actors= pd.read_csv("./actors (2).csv")
maisfilmes=actors.sort_values(by="Number of Movies",ascending=False)
print(maisfilmes.head(1))
