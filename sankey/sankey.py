"""
File: sankey.py
Author: John Rachlin

Description: A wrapper library for plotly sankey visualizations

"""

import pandas as pd
import plotly.graph_objects as go




def code_mapping(df, src, targ):
    """ Map labels in src and targ colums to integers """

    # Get the distinct labels
    labels = sorted(list(set(list(df[src]) + list(df[targ]))))

    # Create a label->code mapping
    codes = range(len(labels))
    lc_map = dict(zip(labels, codes))

    # Substitute codes for labels in the dataframe
    df = df.replace({src: lc_map, targ: lc_map})


    print(lc_map)
    return df, labels



def make_sankey(df, src, targ, vals=None, **kwargs):
    """
    Create a sankey figure
    df - Dataframe
    src - Source node column
    targ - Target node column
    vals - Link values (thickness)
    """

    if vals:
        values = df[vals]
    else:
        values = [1] * len(df)


    df, labels = code_mapping(df, src, targ)

    link = {'source': df[src], 'target': df[targ], 'value': values}
    node = {'label': labels}

    #thickness = kwargs.get("thickness" : 50),

    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.show()


def main():

    bio = pd.read_csv('bio.csv')

    print(bio)
    make_sankey(bio, 'cancer', 'gene', 'evidence')
    code_mapping(bio, 'cancer', 'gene')

if __name__ == '__main__':
    main()

