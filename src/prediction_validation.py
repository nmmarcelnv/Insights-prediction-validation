import pandas as pd
import sys

def parse_data(filename, colnames=['hour','stock_id','stock_price']):
    """ parse the data file. assumes file as 3 inputs per row.
        filename : path to file to parse.
        colnames : default column names to use
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


def compute_rolling_errors(df1, df2, roll_on, target, window_size):

    """Computes the rolling mean error between two columns
        df1,df2 : dataframes
        roll_on : column to roll on (should be sorted)
        target  : target column for which error required
        window  : rolling window size

        Returns a dataframe with 3 columns named
        'start_hour', 'end_hour', 'error'
    """

    #First check that the columns actually exist in the dataframe
    if ( (roll_on not in df1.columns) | (target not in df1.columns) or
         (target not in df2.columns) ) :
         printf("Input Error in compute_rolling_errors: A specified column not in data frame\n")
         return

    #Get the minimum and maximun time
    min_time = min(df1[roll_on])
    max_time = max(df1[roll_on])

    results = {}
    while min_time <= max_time-window_size+1:

        stop_time = min_time + window_size - 1


        window_mask = ( (df1[roll_on] >= min_time) & (df1[roll_on] <= stop_time) )

        actual = df1[window_mask]

        #see https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reindex.html
        selection = actual.index
        predicted = df2.reindex(selection)

        #compute the error for the current window
        error = abs(actual[target] - predicted[target]).mean()

        results[min_time] = [min_time, stop_time, error]

        min_time +=1

    #take the transpose to have correct columns
    results = pd.DataFrame(results).T
    results.columns = ['start_hour', 'end_hour', 'error']

    print(results)
    return results


def write_dfto_file(df, file_out):

    """ Write data frame to a file
        df : DataFrame
        file_out : string specifying the output file
    """

    #convert hours to string to avoid float_format from to_csv
    df['start_hour'] = df['start_hour'].map(lambda x: '%d'%(x))
    df['end_hour'] = df['end_hour'].map(lambda x: '%d'%(x))

    pd.DataFrame(df).to_csv(file_out,
                                sep='|',
                                index=False,
                                header=False,
                                na_rep='NA',
                                float_format='%.2f')



if __name__=="__main__":

    #get input file paths from command line
    file_window = sys.argv[1]
    file_actual = sys.argv[2]
    file_predicted = sys.argv[3]
    file_out = sys.argv[4]


    #parse the files
    actual_df = parse_data(file_actual)
    predicted_df = parse_data( file_predicted)
    window = int(open(file_window,'r').readlines()[0])

    results = compute_rolling_errors(actual_df, predicted_df,
                            roll_on = 'hour',
                            target = 'stock_price',
                            window_size = window)
    #write result to file
    write_dfto_file(results, file_out)
