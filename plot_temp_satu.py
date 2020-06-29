import os
from lists import morning, evening
from name_selection import name_selection
from plot_graph import plot_graph


# Clear the screen.
os.system('clear')

# Determine csv file to plot data from.
#csv_file = input('Write file name (include file extension):')
csv_file = 'temp_satur.csv'

# Determine which set of data to plat, i.e. morning or evening.
moment = ['Morning', 'Evening', 'Both']
# Print a line break.
#print('\n')
# Show selection list
for i in range(len(moment)):
    print('{} - {}'.format(i,moment[i]))
# Print a line break.
print('\n') 
selection = int(input('Select a number: '))
# Determine columns to subset
if selection==0:
    select_columns = morning
elif selection==1:
    select_columns = evening
else:
    print('You have selected both. Sorry, this is under construction')

# Select one person to plot data using name_selextion function.
select_name = [name_selection(csv_file)] # <class 'list'>

# Plot readings according to name, moment of day and file selected.
plot_graph(select_name, select_columns, csv_file)