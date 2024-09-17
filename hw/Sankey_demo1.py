
import plotly.graph_objects as go


source = [0,0]

target = [1, 2]

value = [2,1]


link = {'source' : source, 'target': target, 'value': value}


sk = go.Sankey(link=link)

fig = go.Figure(sk)


fig.show()