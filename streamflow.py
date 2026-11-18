

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# I add pandas to save the summary as a CSV file


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
    # Plt saves the figure as a PNG file (image), dpi=150 is for the resolution, then the plot is displayed
    plt.savefig("provo_streamflow.png", dpi=150,
            bbox_inches="tight")
    plt.show()
# I display the plot

# I define a new function that summarizes various statistics about the data

def summarize(dates, flows, sites):
# I use f to input strings with values
    print(f"{'Gauge':<12}{'Max (cfs)':>10}"
          f"  {'Date of max':<22}"
          f"{'Min (cfs)':>10}{'Avg (cfs)':>12}")
    results = []
# I use a for loop to iterate through the data to calculate the max, min, and 
# average flow rate for each site. I also find the date of the max flow rate
    for i in range(len(sites)):

        gauge_flows = flows[:, i]

        max_flow = np.max(gauge_flows)
        min_flow = np.min(gauge_flows)
        avg_flow = np.mean(gauge_flows)

        max_index = np.argmax(gauge_flows)
        max_date = dates[max_index]

        print(f"{sites[i]:<12}{max_flow:10.1f}"
              f"  {str(max_date):<22}"
              f"{min_flow:10.1f}{avg_flow:12.1f}")
# min_flow and avg_flow are calculated and their results have a width of 10 and 12 characters respectively, and are printed as decimals to one place
sites = ["10163000", "10155200", "10155500",
         "10154200", "10155000"]
# Calls the first function and assigns it to dates, flows
dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
)
# Sends those variables to the plotting function
plot_streamflow(dates, flows, sites)