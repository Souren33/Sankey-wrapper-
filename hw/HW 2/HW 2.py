import pandas as pd
import plotly.graph_objects as go


def read_data(path):
    art = pd.read_json(path)
    return art


def clean_data(df):
    df.loc[:, 'BeginDate'] = df['BeginDate'].astype(float).apply(lambda x: round(x / 10) * 10)
    return df


def filter_base_on_val(df, val, column_name):
    # Filter rows where the column value is greater than the specified value
    filtered = df[df[column_name] > val]
    return filtered


def grouping_data(df, new_column, **kwargs):
    groupings = list(kwargs.values())
    combined_filter = df.groupby(groupings).size().reset_index(name=new_column)
    return combined_filter


def diff_code_mapping(df, src, targ):
    # Create a dictionary to map source and target values to unique codes
    sources = {}
    i = 0
    for name in pd.concat([df[src], df[targ]]).unique():
        sources[name] = i
        i += 1

    df = df.replace({src: sources, targ: sources})
    labels = list(sources.keys())

    return df, labels


def make_sankey(df, src, targ, vals=None, **kwargs):
    if vals:
        values = df[vals]
    else:
        values = [1] * len(df)

    df, labels = diff_code_mapping(df, src, targ)

    link = {'source': df[src], 'target': df[targ], 'value': values}
    node = {'label': labels}

    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.show()


def main():
    # Step 1: Load data
    art_path = r"C:\Users\Souren Prakash\Downloads\artists.json"
    art = read_data(art_path)

    # Focus on columns: nationality, gender, and decade of birth
    art_data = art[['Nationality', 'Gender', 'BeginDate']]

    # Step 2: Clean the data
    processing_art_data = clean_data(art_data)

    # Step 3: Filter out rows with missing or invalid data
    clean_art_data = filter_base_on_val(processing_art_data, 0, "BeginDate")

    # Step 4: Group data by nationality and birth decade
    grouped_data = grouping_data(clean_art_data, "ArtistAmount", group1="Nationality", group2="BeginDate")

    # Step 5: Further filter the grouped data based on a threshold
    filtered_group_data = filter_base_on_val(grouped_data, 35, "ArtistAmount")

    # Step 6: Create Sankey diagram
    make_sankey(filtered_group_data, 'Nationality', 'BeginDate', 'ArtistAmount')


if __name__ == '__main__':
    main()
