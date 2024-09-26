"""
File: sankey.py
Author: Souren Prakash

Description: A wrapper library for plotly sankey visualizations

"""

import pandas as pd
import plotly.graph_objects as go

data = {'A': ['u', 'u', 'u', 'v'],
        'B': ['x', 'y', 'y', 'x'],
        'C': ['p', 'p', 'q', 'p'],
        'Values': [10, 20, 15, 15]}

def SP_code_mapping(df, src, targ):
    """

    :param df: dataframe
    :param src: name of columns, is autofilled by stacking
    :param targ: name of target column
    :return: returns dictionary with all unique values for the data fram
    """
    # Create a dictionary to map source and target values to unique codes
    sources = {}
    i = 0
    #iterates through all unique items in the dataframe in the focus src and targ
    for name in pd.concat([df[src], df[targ]]).unique():
        sources[name] = i
        #increments by 1 to give all values a unique indentity
        i += 1
    #replaces the sources and targets with their unique identities (they are like superheroes and villans)
    df = df.replace({src: sources, targ: sources})
    labels = list(sources.keys())

    return df, labels


def stacking(df,cols, val_col):
    """

    :param df: takes the intial dataframe
    :param cols: a list of columns that are in the data set, I would have used kwargs but I needed to get this done
    :param val_col: the name of the column that is the values
    :return: returns a df with 2 columns and a 3rd for the values. The 2 columns are all the links
    """

    #creating dataframe to hold stacked data for end
        stacked_data = pd.DataFrame()

        #print(range(len(cols) -1))
        #iterating through the column names
        for i in range(len(cols) - 1):

            src_col = cols[i]
            targ_col = cols[i+1]


        # Create a temporary DataFrame with the required columns
            temp_df = df[[src_col, targ_col, val_col]]
            temp_df = temp_df.rename(columns ={src_col:'src', targ_col:'targ'})


            # grouping to get updated values for val col
            temp_df = temp_df.groupby(['src','targ'])[val_col].sum().reset_index()

            #combining the dataframes
            stacked_data = pd.concat([stacked_data, temp_df])
            #print(stacked_data)
        #dropping anything that might be empty
        stacked_data = stacked_data.dropna()

        return(stacked_data)


def SP_make_sankey(df, src, targ, vals=None, **kwargs):
    if vals:
        values = df[vals]
    else:
        values = [1] * len(df)

    #calling stacking to df to have only two columns for data
    df = stacking(df, src, targ)

    #now using code mapping to prepare data to be on sankey
    df, labels = SP_code_mapping(df, 'src', 'targ')


    #print(df)
    #declaring params for sankey
    link = {'source': df['src'], 'target': df['targ'], 'value': values}
    node = {'label': labels}


    #plotting
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.show()



def main():
    # Sample dataframe
    data = {'A': ['u', 'u', 'u', 'v'],
            'B': ['x', 'y', 'y', 'x'],
            'C': ['p', 'p', 'q', 'p'],
       'Values': [10, 20, 15, 15]}

    df = pd.DataFrame(data)

    # Columns for stacking
    columns = ['A', 'B', 'C']

    # Apply the stacking function
    #stacked_df = stacking(df,columns,'Values')



    #testing sp code mapping
    #SP_code_mapping()

    #print(stacked_df)





    stacked_data = stacking(df, columns, "Values")

    print(stacked_data)
    print(SP_code_mapping(stacked_data, 'src', 'targ'))

    SP_make_sankey(df, columns, 'Values','Values')


    #SP_make_sankey()
if __name__ == '__main__':
    main()

