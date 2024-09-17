
import plotly.graph_objects as go


source = [0, 0, 0, 1, 1, 2, 2, 2]
target = [3, 4, 5, 3, 5, 3, 4, 5]
value = [1, 1, 1, 1, 2, 2, 0.5, 1]
label  = ['Brain', 'Stomach', 'Lung', 'Gx', 'Gy', 'Gz']


#label = ['Souren', 'Varsha', 'Jharna', 'Deep Blue']

#creating the links
link_colors = ['lightgrey'] * 8
link_colors[5] = '#F4B282'
#link_colors[2] = rgba(3, 20, 50, .5)

link = {'source' : source, 'target': target, 'value': value, 
        'line': {'color':'black', 'width':2}, 'color': link_colors}

#creating labels
node = {'label':label, 'pad': 50, 'thickness': 50,\
    'line': {'color':'black', 'width':2}}

sk = go.Sankey(link=link, node=node)

fig = go.Figure(sk)


fig.show()