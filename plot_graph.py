import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
from matplotlib.dates import DateFormatter, FR, WeekdayLocator
from datetime import datetime
from lists import morning, evening


def plot_graph(name, moment, file_name):
    """Plot records of body temperature and oxygen saturarion
        input: name, moment (morning, evening)
        return: plot of temperature & saturation and probability of saturation


    """
    # Create a list with selected columns.
    select_columns = moment # <class 'list'>

    # Determine moment.
    if moment == morning:
        day_time = ' MORNING'
    else:
        day_time = ' EVENING'

    # Use the index_col parameter to select the first column of data as the index 
    # index_col = 1 corresponds to 'name'
    # Define dtype according to moment passed. Index 2 is 'temp' and 3 is 'satu'
    temp = moment[2] 
    satu = moment[3]
    
    # Read and ecode data from file passed argument.
    df = pd.read_csv(file_name, index_col=1, dtype={temp:np.float64, satu:np.float64}) # <class 'pandas.core.frame.DataFrame'>

    # Subset with only values when getting in to the office.
    in_values = df[select_columns] # <class 'pandas.core.frame.DataFrame'>

    # Select one person to plot data using name_selection function.
    select_name = name # <class 'list'>

    name_selected = in_values.loc[select_name] # <class 'pandas.core.frame.DataFrame'>

    name_selected_values = name_selected.values # <class 'numpy.ndarray'>

    # Create DataFrame.
    df1 = pd.read_csv(file_name, index_col=None)
    
    # Subset with names.
    column_name = df1['name'] # <class 'pandas.core.series.Series'>
    
    # Remove duplicated names
    names = column_name.drop_duplicates() # <class 'pandas.core.series.Series'>


    ## Plot data.
    # Values to plot: daily temperature and saturation.
    # Extract temperature data for name selected.
    reading_temperature = name_selected[temp]
    mean_temperature = reading_temperature.mean()

    # Extract saturarion data for name selected.
    reading_saturation = name_selected[satu]
    mean_saturation =reading_saturation.mean()

    # Extract date without date format for name selected.
    dates = name_selected['date']

    # Give format to dates (month-day-year).
    dates_format = pd.to_datetime(dates, format='%m-%d-%Y')


    # tick on mondays every week.
    loc = WeekdayLocator(byweekday=FR, interval=1)

    # Define the format for date data, remove year and name each month (Apr-02).
    formatted_date = DateFormatter("%b-%d")


    fig = plt.figure(figsize=[16,6])
    ax1 = plt.subplot(121)

    # Plot line, color red, temperature values.
    color = 'tab:red'
    ax1.set_ylabel('Temperature (C)', color= color)
    ax1.tick_params(axis='y', length=7,  labelcolor=color, color=color)
    temperature, = ax1.plot( dates_format, reading_temperature, color=color)

    # Plot line, color blue, oxygen saturation values.
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Saturation (%)', color=color)
    ax2.tick_params(axis='y', length=7,  labelcolor=color, color=color)
    saturation, = ax2.plot(dates_format,reading_saturation, color=color)

    ax1.set(title='Body Temperature and Saturation')
    ax1.xaxis.set_major_locator(loc)
    ax1.xaxis.set_major_formatter(formatted_date)
    ax1.grid()
    ax1.xaxis_date()

    ax3 = plt.subplot(122)
    histogram = plt.hist(reading_saturation, bins=6, density=True, stacked=True)
    ax3.set_xlabel('Saturation (%)', color=color)
    saturation_labels = [89,90,91,92,93,94,95,96,97,98]
    ax3.set_xticks(saturation_labels)
    textstr = '\n'.join((
        r'Mean Temperature= %.1f %s' % (mean_temperature,'C' ),
        r'Mean Saturation= %.1f %s' % (mean_saturation,'%' )))

    # these are matplotlib.patch.Patch properties.
    props = dict(boxstyle='round', facecolor='gray', alpha=0.5)
    
    # Place a text box in upper left in axes coords.
    ax3.text(0.55,0.95, textstr, transform=ax3.transAxes, fontsize=12,
            verticalalignment='top', bbox=props)
    ax3.set(title='Most Probable Saturation')
    
    # Define main title of graph.
    main_title = str(name[0]).upper()+': '+day_time+' TEMPERATURE AND SATURATION RECORDS'
    fig.suptitle(main_title)

    return plt.show()





