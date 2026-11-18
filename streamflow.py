

import matplotlib.pyplot as plt
import numpy as np


### Part 3 - Provo River Streamflow Data

### Numpy Array Creation & Slicing

# I define a new fuction that loads the streamflow data from a CSV file and returns the dates and flow rates as numpy arrays. The function uses np.genfromtxt to read the data, specifying the delimiter as a comma, the data type as string, and the encoding as 'utf-8'. It then slices the array to extract the dates and flow rates, converting them to appropriate data types.
def load_streamflow(filename):

    array3 = np.genfromtxt(
        filename,
        delimiter=',',
        dtype=str,
        encoding='utf-8'
    )
# I extract the dates from each row simultaneouslyin the array and convert them to floats
    dates = array3[1:, 0].astype('datetime64')

    flows = array3[1:, 1:6].astype(float)

    return dates, flows



### Graphing the Data
# I define a new function to take the array we established earlier to plot the data
def plot_streamflow(dates, flows, sites):

    plt.figure(figsize=(12, 5))
# We plot each of the rows in each column in a variety of colors
    plt.plot(dates, flows[:, 0], color='blue',
             label=f'Site {sites[0]}')

    plt.plot(dates, flows[:, 1], color='red',
             label=f'Site {sites[1]}')

    plt.plot(dates, flows[:, 2], color='green',
             label=f'Site {sites[2]}')

    plt.plot(dates, flows[:, 3], color='orange',
             label=f'Site {sites[3]}')

    plt.plot(dates, flows[:, 4], color='purple',
             label=f'Site {sites[4]}')
# I give the plot various labels, titles, and other features
    plt.title('Provo River Streamflow Rates - June 2021')
    plt.xlabel('Date')
    plt.ylabel('Streamflow Rate (cfs)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
# I display the plot

# NOTE: THE COMMENTS USED BEFORE TO EXPLAIN WHAT THE CODE IS DOING TO PLOT THE GRAPH OF THE DATA APPLIES HERE AS WELL.**
# Main program

sites = ["10163000", "10155200", "10155500",
         "10154200", "10155000"]
# Calls the first function and assigns it to dates, flows
dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
)
# Sends those variables to the plotting function
plot_streamflow(dates, flows, sites)