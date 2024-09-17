"""
file: sankey.py

autho: Souren prakash


wrapper library for plotly sankey vis
"""
import pandas as pd







#doing as classwork

def code_mapping(df, src, targ):

    """maps labels in src and targ colm to integers"""


    labels = sorted(list(set(list(df[src]) + list(df[targ]))))
    print(labels)

    return labels






















def make_sankey( df, src, targ, vals):

    """ Create sankey figure
    df - dataframe
    src = source node column
    targ - target node colum
    vals - link values  ( Thickness of line)
    """

    code_mapping(df, src,targ)


    #creating dictionary to store the source with the number associate
    links = {}
    c = 0

    for item in df[src]:
        if item not in links:
            links[item] = c
            c += 1


    new_column = []
    for item in df[src]:
        target = links.get(item)
        if target is not None:
            new_column.append(target)
        else:
            print(f'{item} not found in dict')

    #print(new_column)
    #print(new_column)

   # print (df[src])

    df['source_mapped'] = new_column

    print (new_column)

def read_data(file):
    """
    Purpose- reading a file and turning into dataframe
    """
    data = pd.read_csv(file)

    return data



def main():

    data = read_data(r'C:\Users\Souren Prakash\Courses\DS3500\DS3500\sankey\data\bio.csv')


    make_sankey(data, 'cancer', 'gene', 'evidence')


main()
