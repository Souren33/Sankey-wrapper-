

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('bio.csv')
print(df)

link = {'source': df.source, 'target' :df.target, 'value':value}