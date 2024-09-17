

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('bio_encoded.csv')
print(df)


# The following won't work but it showcases what we are trying to do
link = {'source': df['source'], 'target': df.target, 'value': df.value,
        'line': {'color': 'black', 'width': 2}}

node = {'label': ['?'] * 6, 'pad': 50, 'thickness': 50,
        'line': {'color': 'black', 'width': 2}}

sk = go.Sankey(link=link, node=node)
fig = go.Figure(sk)
fig.show()
