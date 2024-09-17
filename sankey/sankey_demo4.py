
import plotly.graph_objects as go

source = [0, 0, 0, 1, 1, 2, 2, 2]
target = [3, 4, 5, 3, 5, 3, 4, 5]
value = [1, 1, 1, 1, 2, 2, 0.5, 1]

"""
Stomach, Gx, 1
Stomach, Gy, 1
.
.

Brain, Gz, 1

"""

label  = ['Stomach', 'Lung', 'Brain', 'Gx', 'Gy', 'Gz']

link_colors = ['lightgrey'] * 8
link_colors[5] = '#F4B212'
link_colors[3] = 'rgba(145, 154, 232, 0.5)'

node_colors = ['mediumslateblue'] * 3 + ['palegoldenrod'] * 3


link = {'source': source, 'target': target, 'value': value,
        'line': {'color': 'black', 'width': 2},
        'color': link_colors}


node = {'label': label, 'pad': 50, 'thickness': 50,
        'line': {'color': 'black', 'width': 2},
        'color': node_colors}

sk = go.Sankey(link=link, node=node)

fig = go.Figure(sk)

fig.show()
