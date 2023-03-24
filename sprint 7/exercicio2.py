import pandas as pd
import numpy as np
actors = pd.read_csv("./actors (2).csv")
media= actors["Number of Movies"].mean()
print(media)