
import plotly.graph_objects as go


source = [0, 0, 3, 3]
target = [ 1, 2, 2, 1]
value = [1, 2, 3, 4]

label = ['Souren', 'Varsha', 'Jharna', 'Deep Blue']

#creating the links
link = {'source' : source, 'target': target, 'value': value}

#creating labels
node = {'label':label, 'pad': 200, 'thickness': 20}

sk = go.Sankey(link=link, node=node)

fig = go.Figure(sk)


fig.show()