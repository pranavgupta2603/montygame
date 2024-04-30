import pandas as pd


def add_data(df, num_doors, result_column):
    # locate where 
    if num_doors in df['num_doors'].values:
        # Add 1 to 'Column1' where 'Column2' is 'D'
        df.loc[df['num_doors'] == num_doors, 'num_times_played'] += 1
        df.loc[df['num_doors'] == num_doors, f'{result_column}'] += 1
    else:
        # Add a new row with 'D' in 'Column2' and set 'Column1' to 1
        df = df.append({'num_doors': num_doors, 'num_times_played': 1, result_column: 1}, ignore_index=True)
        df.fillna(0, inplace=True)

    df.to_csv('data.csv', index=False)
    
    
    
if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    num_doors = 2
    results = [1, 0, 0, 0] # stay_wins, switch_wins, stay_loses, switch_loses
    result_column = df.columns[2:][results.index(1)]
    print(result_column)
    add_data(df, num_doors, result_column)