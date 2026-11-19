# AI STATEMENT: The following code was written by CHATGPT. I tried to understand it and make it better. 
# I added comments to explain what each part of the code does. CHATPPT helped write some of the comments.
# CHATGPT also added a function to save the summary of the streamflow data as a CSV file. 
# COPILOT added a function to count the number of hours above a given threshold for each gauge in the flows array.

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
    print(f"{'Gauge':<12}{'Max (cfs)':>10}"
          f"  {'Date of max':<22}"
          f"{'Min (cfs)':>10}{'Avg (cfs)':>12}")
    results = []
    # I use a for loop to calculate the max, min, and average flow rate for each site.
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
        results.append({
            "Gauge": sites[i],
            "Max (cfs)": max_flow,
            "Date of max": max_date,
            "Min (cfs)": min_flow,
            "Avg (cfs)": avg_flow
        })

    # I make a data frame to save the summary as a csv
    summary_df = pd.DataFrame(results)
    summary_df.to_csv("streamflow_summary.csv", index=False)
# min_flow and avg_flow are calculated and their results have a width of 10 and 12 characters respectively, and are printed as decimals to one place
sites = ["10163000", "10155200", "10155500",
         "10154200", "10155000"]
# Calls the first function and assigns it to dates, flows
dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
)
# Sends those variables to the plotting function
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)
# I call the function to later execute it
# input asks the user to enter a value. FLoat converts that value into a number that the code can use.
# AI-assisted code: Counts readings above the
# user's threshold and converts them to hours.

threshold = float(input("Enter a flow threshold (cfs): "))

print(f"\nHours above {threshold} cfs:")
# I print the number of hours above the threshold for each site.
for i in range(len(sites)):
# I loop through each site to count the number of readings above the threshold and convert
# that count to hours.
    gauge_flows = flows[:, i]

    count = np.sum(gauge_flows > threshold)

    hours = count * 0.25

    print(f"{sites[i]}: {hours:.2f} hours")
    # I print the number of hours above the threshold for each site. The 
    # result is formatted to two decimal places


# Threshold tests
# I define a new function that counts the number of hours above a given
# threshold for each gauge in the flows array.
# The function takes in the flows array and the threshold value as arguments,
# and return a list of hours above the threshold for each gauge.
def hours_above_threshold(flows, threshold):
    hours = []
    for i in range(flows.shape[1]):
        count = np.sum(flows[:, i] > threshold)
        hours.append(count * 0.25)
    return hours

# AI STATEMENT: The following code below was written by COPILOT. I tried to underst
# It tests the hours_above_the_threshold function with two boundary cases.
# The first case checks that all gauges have 720 hours above a threshold of 0 cfs,
# and the second case checks that all gauges have 0 hours above a threshold that is 
# greater than the maximum flow in the dataset. If either of these assertions fails, 
# an error message will be printed.
# At threshold zero, any normal positive flow is above the threshold.
zero_threshold_hours = hours_above_threshold(flows, 0)
assert all(hours == 720 for hours in zero_threshold_hours), \
    "Every gauge should be above 0 cfs for all 720 hours."

# A threshold above the largest flow in the file must have zero hours
# for every gauge.
above_max_threshold = float(np.max(flows) + 1)
above_max_hours = hours_above_threshold(flows, above_max_threshold)
assert all(hours == 0 for hours in above_max_hours), \
    "Every gauge should have 0 hours above a threshold above all flows."

print("\nThreshold tests:")
print("Threshold 0 cfs: all gauges have 720.0 hours")
print(f"Threshold {above_max_threshold:.1f} cfs: all gauges have 0.0 hours")