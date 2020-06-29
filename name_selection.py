import pandas as pd


def name_selection(csv_file):
    """Select one name from a csv file
        input: csv file with all data
        returns: a name, str value

        csv file should have a column 'name'
    """
    ## Code to extract names from DataFrame
    # Create DataFrame
    df1 = pd.read_csv(csv_file, index_col=None)
    
    # Subset with names
    column_name = df1['name'] # <class 'pandas.core.series.Series'>
    
    # Remove duplicated names
    names = column_name.drop_duplicates() # <class 'pandas.core.series.Series'>
    
    # Loop to show list of codes and names
    for index in names.index:
        print(' %d - %s' % (index, names[index]))
    print('\n') 

    name_code = input('Select name (enter code value):')

    name_selected = names[int(name_code)]

    return name_selected