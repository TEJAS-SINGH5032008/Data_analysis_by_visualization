import pandas as pd
import csv
import ploty.graph_objects as go

df = pd.read_csv["data.csv"]
print(df.groupby("level")["attempt"].mean())
fig = go.figure(go.bar(
    x = df.groupby("level")["attempt"].mean()
    y = ["level","leve2","leve3","leve4"]
    orientation = "h"
))