"""
file: sankey.py

autho: Souren prakash


wrapper library for plotly sankey vis
"""
import pandas as pd
import plotly.graph_objects as go







#doing as classwork

def code_mapping(df, src, targ):

    """maps labels in src and targ colm to integers"""


    labels = sorted(list(set(list(df[src]) + list(df[targ]))))
    print(labels)


    #creating code source mapping

    codes = range(len(labels))
    lc_map = dict(zip(labels, codes))

    df = df.replace({src:lc_map, targ:lc_map})






    return df, labels





def make_sankey(df, src, targ, vals):
    """
    Create a sankey figure
    df - Dataframe
    src - Source node column
    targ - Target node column
    vals - Link values (thickness)
    """
    df, labels = code_mapping(df, src, targ)
    link = {'source': df[src], 'target': df[targ], 'value': df[vals]}
    node = {'label': labels}
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.show()
def read_data(file):
    """
    Purpose- reading a file and turning into dataframe
    """
    data = pd.read_csv(file)

    return data



def main():

    data = read_data(r'C:\Users\Souren Prakash\Courses\DS3500\DS3500\sankey\data\bio.csv')
    make_sankey(data, 'cancer', 'gene', 'evidence')


if __name__ == '__main__':

    main()