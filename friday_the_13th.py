import pandas as pd 

#input your datasets
data = {("Date",""):["October 1989","July 1990","September 1991","December 1991","March 1992","November 1992"],
        ("Accidenet & Poisoning","Friday 6th"):[4,6,1,9,9,1],
        ("Accidenet & Poisoning","Friday 13th"):[7,6,5,5,7,6],
        ("Traffic Accidents","Friday 6th"):[9,6,11,11,3,5],
        ("Traffic Accidents","Friday 13th"):[13,12,14,10,4,12]
        }

#create a dataframe from your data
df = pd.DataFrame(data)

#rename the dataframe
friday_13th = df

print(friday_13th.to_string(index=False))



def calculate_columns_statistics(df):
    # Exclude the 'Date' column explicitly
    numeric_df = df.loc[:, df.columns.get_level_values(0) != 'Date']

    # Calculate statistics for each numeric column
    stats_dict = {
        'Mean': numeric_df.mean(numeric_only=True),
        'Median': numeric_df.median(),
        'SD': numeric_df.std(),
        'IQR': numeric_df.quantile(0.75) - numeric_df.quantile(0.25)
    }

    #convert the stats into a dataframe 
    stats_df = pd.DataFrame(stats_dict)
    return stats_df

stats_df = calculate_columns_statistics(friday_13th)
print(stats_df)


