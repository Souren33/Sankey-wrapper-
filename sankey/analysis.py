import pandas as pd
import sankey as sk


def main():
    #bio = pd.read_csv('data/bio.csv')
    #sk.make_sankey(bio, 'cancer', 'gene')

    #brain = pd.read_csv('data/BrainCancer.csv').dropna()
    #sk.make_sankey(brain, 'diagnosis', 'loc')

    bike = pd.read_csv('data/Bikeshare.csv')
    bike_agg = bike.groupby(['mnth', 'weathersit'])['bikers'].sum().reset_index()
    sk.make_sankey(bike_agg, 'mnth', 'weathersit', 'bikers')


if __name__ == '__main__':
    main()