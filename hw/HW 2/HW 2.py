import pandas as pd
import plotly.graph_objects as go
import sankey as sk

def read_data(path):
    #simple function to read path to pd
    art = pd.read_json(path)
    return art


def clean_data(df):
    """

    :param df: any data frame
    :return: returns a data frame converting all values in begin column to a float then rounded to nearest decade
    """

    df.loc[:, 'BeginDate'] = df['BeginDate'].astype(float).apply(lambda x: round(x / 10) * 10)
    return df


def filter_base_on_val(df, val, column_name):
    """

    :param df: dataframe that has been rounded
    :param val: the value wanted to filter by
    :param column_name: the column which is desired to be filtered
    :return: dataframe that dropped all the data below that value
    """
    # Filter rows where the column value is greater than the specified value
    filtered = df[df[column_name] > val]
    return filtered


def grouping_data(df, new_column, **kwargs):
    """

    :param df: dataframe that data has been formatted
    :param new_column: the name of a new column
    :param kwargs: the different groups that you want to group by
    :return: returns a dataframe that adds that column that was grouped by
    """
    groupings = list(kwargs.values())
    combined_filter = df.groupby(groupings).size().reset_index(name=new_column)
    return combined_filter


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
    filtered_group_data = filter_base_on_val(grouped_data, 20, "ArtistAmount")


    # Step 6: Create Sankey diagram to display nationality and begin date, artist amount is
    #creating col group for nationality and Begin date
    Nationality_BeginDate = ['Nationality', 'BeginDate']
    #sk.SP_make_sankey(filtered_group_data, Nationality_BeginDate,'ArtistAmount', 'ArtistAmount')


    # Step 7 Creating sankey diagram grouped by gender and decade

    gendered_data = grouping_data(clean_art_data, 'GenderAmount', group1="Gender", group2="BeginDate")

    filter_gendered_data = filter_base_on_val(gendered_data, 20, "GenderAmount")
    #graphing on sankey

    gender_decade_columns = ["Gender", "BeginDate"]

    sk.SP_make_sankey(filter_gendered_data,gender_decade_columns,"GenderAmount", "GenderAmount" )



    #print(clean_art_data)
    multi_grouped = grouping_data(clean_art_data, 'GenderAmount',group1="Nationality", group2="Gender", group3="BeginDate")
    #the last sankey should be multilayered and using stacked function to get correct format

    #columns of focus for final multilayered sankey
    multicolumn = ['Nationality', 'Gender', 'BeginDate']

    #reducing amount of data by filtering by certain amount
    filter_multi_grouped = filter_base_on_val(multi_grouped, 20, "GenderAmount")
    sk.SP_make_sankey(filter_multi_grouped, multicolumn, 'GenderAmount', 'GenderAmount')

if __name__ == '__main__':
    main()
