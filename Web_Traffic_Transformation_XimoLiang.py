# # -*- coding: utf-8 -*-
# @author: Ximo Liang




import pandas as pd


################################

def csv_proc(root_url, outpath = 'web_traffic_transformation.csv'):
    
    ## Create URL list of CSVs
    urls = [
            f'{root_url}/{letter}.csv'
            for letter in 'abcdefghijklmnopqrstuvwxyz'
            ]
    
    ## read CSVs from URL list and combine them into one dataframe
    dfs = [pd.read_csv(url) for url in urls]
    df = pd.concat(dfs).reset_index(drop=True)
    
    
    ## Create a new dataframe to have user_id as the index, path as columns, and length as values
    df2 = df.pivot_table(index='user_id', columns='path', values='length', aggfunc='sum', fill_value=0)
    df2.reset_index(inplace=True)
    
    ## Save the the new df to CSV
    df2.to_csv(outpath, index=False)



def main():
    
    ## Define the root URL of CSVs
    root_url= 'https://public.wiwdata.com/engineering-challenge/data'
    
    ## Define the output path if necessary
    # csv_proc(root_url, 'e:/web_traffic_transformation.csv')
    csv_proc(root_url)

if __name__ == "__main__":
    main()
