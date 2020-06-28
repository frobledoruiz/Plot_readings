import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
from matplotlib.dates import DateFormatter, FR, MO, SA, SU, TH, TU, WE, WeekdayLocator
from datetime import datetime



## Use the index_col parameter to select the first column of data as the index 
# inex_col = 1 corresponds to 'name'
df = pd.read_csv('temp_satur.csv', index_col=1, dtype={'temp_in':np.float64, 'satu_in':np.float64}) # <class 'pandas.core.frame.DataFrame'>


# Just to know
index = df.index # <class 'pandas.core.indexes.range.RangeIndex'>
columns = df.columns # <class 'pandas.core.indexes.base.Index'>
values = df. values # <class 'numpy.ndarray'>

# Create a list with selected columns
select_columns = ['date', 'time_in', 'temp_in', 'satu_in'] # <class 'list'>

# Subset with only values when getting in to the office
in_values = df[select_columns] # <class 'pandas.core.frame.DataFrame'>

# Select one person
select_name = ['FERNANDO ROBLEDO'] # <class 'list'>

name_selected = in_values.loc[select_name] # <class 'pandas.core.frame.DataFrame'>

name_selected_values = name_selected.values # <class 'numpy.ndarray'>

## Code to extract names from DataFrame
# Create DataFrame
df1 = pd.read_csv('temp_satur.csv', index_col=None)
# Subset with names
column_name = df1['name'] # <class 'pandas.core.series.Series'>
# Remove duplicated names
names = column_name.drop_duplicates() # <class 'pandas.core.series.Series'>


## Plot data
# Values to plot: daily temperature and saturation
morning_temperature = name_selected['temp_in']
morning_saturation = name_selected['satu_in']
dates = name_selected['date']
dates_format = pd.to_datetime(dates, format='%m-%d-%Y')

#print(type(dates_format)) # <class 'pandas.core.series.Series'>


# tick on mondays every week
loc = WeekdayLocator(byweekday=FR, interval=1)

# Define the date format (e.j: Apr-02)
date_form = DateFormatter("%b-%d")

#plt.figure(1)

#fig, ax1 = plt.subplots()
fig = plt.figure(figsize=[16,6])
ax1 = plt.subplot(121)

# Plot line, color red, temperature values
color = 'tab:red'
ax1.set_ylabel('Temperature (C)', color= color)
ax1.tick_params(axis='y', length=7,  labelcolor=color, color=color)
temperature, = ax1.plot( dates_format, morning_temperature, color=color)

# Plot line, color blue, oxygen saturation values
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Saturation (%)', color=color)
ax2.tick_params(axis='y', length=7,  labelcolor=color, color=color)
saturation, = ax2.plot(dates_format, morning_saturation, color=color)

ax1.set(title='Morning Body Temperature and Saturation')
ax1.xaxis.set_major_locator(loc)
ax1.xaxis.set_major_formatter(date_form)
ax1.grid()
ax1.xaxis_date()

ax3 = plt.subplot(122)
histogram = plt.hist(morning_saturation, bins=6, density=True, stacked=True)
ax3.set_xlabel('Saturation (%)', color=color)

fig.tight_layout()
plt.show()





