import pandas as pd
import sys

def parse_data(filename, colnames=['hour','stock_id','actual']):
    """ parse the data file. assumes file as 3 inputs per row.
        filename : path to file to parse.
        colname  : default column names to use
        Returns a pandas dataframe
    """

    df = pd.read_csv( filename,
                        sep = '|',
                        header = None,
                        names = colnames,
                        float_precision='high')
    df.sort_values(by=['hour','stock_id'], inplace=True)


    """create a column of unique keys combining
    hour and stock_id to use as index.
    This will be useful in merding data frames"""
    unique_keys = [str(hour)+stock_id for hour,stock_id in
                    zip(list(df['hour']), list(df['stock_id']))]
    df.index = unique_keys

    return df

def merge_frames(df1, df2, keys = ['hour','stock_id']):
    """ merge two dataframes (inner join) on 'hour' and 'stock_id'
        Returns a dataframe where keys match in both df1 and df2.
    """
    return pd.merge(df1, df2, on=keys)

def compute_rolling_errors(df, roll_on, column1, column2, window_size):

    """Computes the rolling mean error between two columns
        df      : dataframe
        roll_on : column to roll on (should be sorted)
        column1 : first target columns for the error
        column2 : second target columns for the error
        window  : rolling window size

        Returns a dataframe with 3 columns named
        'start_hour', 'end_hour', 'error'
    """

    #First check that the columns actually exist in the dataframe
    if ( (roll_on not in df.columns) | (column1 not in df.columns) or
         (column2 not in df.columns) ) :
         printf("Input Error: A specified column not in data frame\n")
         return

    #Get the minimum and maximun time
    min_time = min(df[roll_on])
    max_time = max(df[roll_on])

    results = {}
    while min_time <= max_time-window_size+1:

        stop_time = min_time + window_size - 1
        selection = df[ (df[roll_on] >= min_time) & (df[roll_on] <= stop_time) ]

        error = abs(selection[column2] - selection[column1]).mean()
        results[min_time] = [min_time, stop_time, error]

        min_time +=1

    results = pd.DataFrame(results).T
    results.columns = ['start_hour', 'end_hour', 'error']

    return results


def write_dfto_file(df, file_out):

    """ Write data frame to a file
        df : DataFrame
        file_out : string specifying the output file
    """

    #convert hours to string to avoid float_format from to_csv
    df['start_hour'] = results['start_hour'].map(lambda x: '%d'%(x))
    df['end_hour'] = results['end_hour'].map(lambda x: '%d'%(x))

    pd.DataFrame(results).to_csv(file_out,
                                sep='|',
                                index=False,
                                header=False,
                                float_format='%.2f')



if __name__=="__main__":

    #get input file paths from command line
    file_window = sys.argv[1]
    file_actual = sys.argv[2]
    file_predicted = sys.argv[3]
    file_out = sys.argv[4]


    #parse the files
    actual_df = parse_data(file_actual)
    predicted_df = parse_data( file_predicted,
                                colnames=['hour','stock_id','predicted'])
    window = int(open(file_window,'r').readlines()[0])

    #use indices of of predicted_df to subset actual_df, essentially a merge
    merged_df = actual_df.loc[predicted_df.index]
    merged_df['predicted'] = predicted_df.predicted

    #compute the rolling error between actual and predicted stocks
    results = compute_rolling_errors(merged_df,
                            roll_on = 'hour',
                            column1 = 'actual',
                            column2 = 'predicted',
                            window_size = window)

    #write result to file
    write_dfto_file(results, file_out)
