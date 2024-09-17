# -*- coding: utf-8 -*-
"""
@author: John Rachlin
@date  : January 12, 2020
@file  : cherry.py

Analysis of the full-flowering day-of-year for cherry blossums 
in Kyoto Japan.

Why is this significant?   Scientists are interested in understanding
periodic biological phenomena (flowering, breeding, migration) 
especially as it relates to climatic conditions.  (The scientific
study of these types of phenomena is known as PHENOLOGY.)

Data source: https://www.ncei.noaa.gov/pub/data/paleo/historical/phenology/japan/LatestVersion/KyotoFullFlower7.xls

According to https://www.thetimes.co.uk/expert-traveller/destinations/japan/guide-to-cherry-blossom-holidays-in-japan
The actual full-blossum day was day was March 23th (31 + 29 + 23 = day 83) 
and the prediction for 2021 is March 22 (31 + 28 + 22 = day 81).
These two values were added to the dataset.

"""

import matplotlib.pyplot as plt



def read_flowering_data(filename):
    """ Read cherry blossum full-flowering day-of-year data.
    Return a dictionary mapping year to day-of-year (of full blossums) """
    
    data = {}
    
    file = open(filename, 'r')
    
    # Ignore the header
    file.readline()
    
    # Read each data row
    line = file.readline()
    while line != '':
        
        # Tokenize line
        fields = line.split(',')
        
        # Extract year and doy (if available)
        year = int(fields[0])        
        if fields[1] != '\n':  # doy is not missing
            doy = int(fields[1][:-1])

            # Store in dictionary
            data[year] = doy

            
        # Read next line
        line = file.readline()
    
    file.close()
    return data
    

def blossum_day_century_average(bldata):
    """ The average doy for years of a given century
    Return a dictionary: century -> average doy """
    century_average = {}
    
    # Aggregate by century
    for year, doy in bldata.items():
        century = (year // 100) * 100 
        if century in century_average:
            century_average[century].append(doy)
        else:
            century_average[century] = [doy]
            
    # Convert each aggregate into an average        
    for century in century_average:
        century_average[century] = sum(century_average[century]) / len(century_average[century])
        
    return century_average  



def blossum_date_moving_average(bldata, window_size = 50):
    """ Compute a moving average using a specified window size.
    (Specifically +/- window_size / 2.)    """
    
    moving_average = {}
    # For each data point, acccumulate all values
    # follwing within +/- window_size / 2 of that year
    
    for year in bldata:
        moving_average[year] = []
        for window_year, doy in bldata.items():
            if abs(year - window_year) <= window_size / 2:
                moving_average[year].append(doy)
                
    # Convert each aggregate (window values) to an average
    for year in moving_average:
        moving_average[year] = sum(moving_average[year]) / len(moving_average[year])
        
    return moving_average
        


def plot_blossum_day_history(bldata, centdata, mavgdata):
    """ Plot the day-of-year full blossuming by year
    for all available years """
    
    years = bldata.keys()
    days = bldata.values()
    
    #centuries = centdata.keys()
    #averages = centdata.values()
    
    moving_averages = mavgdata.values()
    
    plt.figure(figsize=(10,6), dpi=100)
    plt.title("Cherry Blossom full blossom date (Kyoto, Japan)")
    plt.xlabel("Year")
    plt.ylabel("Date")
    plt.scatter(years, days, marker='.', color='#FF66B2', label='Full blossom date') # The color of cherry blossums!
    
    #plt.plot(centuries, averages, marker = 'h', color='b', label='century avg')
    
    plt.plot(years, moving_averages, color='b', label='30 year moving avg')   
    plt.yticks([80,90,100,110,120], ['Mar 21', 'Mar 31', 'Apr 10', 'Apr 20', 'Apr 30'])

    
    # Actual (2020) and predicted (2021)
    plt.text(1930, 82.5, '2020---')
    plt.text(1869, 80.6, '2021 pred---')
    
    # Outliers are interesting!
    # There was a global temperature reduction at that time.
    # See global_temps.png
    
    plt.text(1333,124, '1323 (May 4th)')
    
    # Annotate figure with "The little ice-age" - a period of cooling
    # occurring between 1400-1800, though, according to wikipedia,
    # some experts prefer the alternative timespan of 1300-1850
    
    plt.text(1300,84, '<- - - - - -------- The "Little Ice Age" ---------- - ->')
    
    
    # Include a legend
    plt.legend(facecolor='lightgrey', edgecolor='black')
    plt.grid()
    plt.show()
    
    



def main():
    
    # Read the data into a dictionary (year -> doy)
    blossum_day_data = read_flowering_data('cherry.csv')
    
    
    # Compute blossum doy average for each century
    century_average = blossum_day_century_average(blossum_day_data)
    
    # Compute blossum day 50-year moving averages
    moving_average = blossum_date_moving_average(blossum_day_data, 30)

    
    # Visualize full-blossum day-of-year (Kyoto, Japan)
    plot_blossum_day_history(blossum_day_data, century_average, moving_average)
        
    
    
if __name__ == '__main__':
    main()
