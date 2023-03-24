import pandas as pd
import numpy as np
actors=pd.read_csv("actors (2).csv")
maiormedia= actors.sort_values(by="Average per Movie",ascending=False)
print(maiormedia.head(1))