

import matplotlib.pyplot as plt
import numpy as np


### Part 3 - Provo River Streamflow Data

### Numpy Array Creation & Slicing



#   x - Date
#   y_1 - Site 10163000
#   y_2 - Site 10155200
#   y_3 - Site 10155500
#   y_4 - Site 10154200
#   y_5 - Site 10155000


# AI WROTE THE CODE. AI HELPED ME UNDERSTAND THE CODE.

# I import the Provo River streamflow CSV. Same process of uploading and
# converting as before.
array3 = np.genfromtxt(
    'June-2021-Provo-River-Streamflow-Rates.csv',
    delimiter=',',
    dtype=str,
    encoding='utf-8'
)

# I display the first five rows to verify the columns
print(array3[:5, :])

# I extract the dates. "datetime64" converts the strings in the CSV value to dates to be used
# by python
x = array3[1:, 0].astype('datetime64')

# I extract streamflow measurements for each station. I convert the strings from the CSV file to
# numbers to be used by python
y_1 = array3[1:, 1].astype(float)
y_2 = array3[1:, 2].astype(float)
y_3 = array3[1:, 3].astype(float)
y_4 = array3[1:, 4].astype(float)
y_5 = array3[1:, 5].astype(float)

# I check the extracted data to ensure all arrays print correctly.
print(x[:5])
print(y_1[:5])
print(y_2[:5])
print(y_3[:5])
print(y_4[:5])
print(y_5[:5])

### Graphing the Data



# NOTE: THE COMMENTS USED BEFORE TO EXPLAIN WHAT THE CODE IS DOING TO PLOT THE GRAPH OF THE DATA APPLIES HERE AS WELL.**


# AI WROTE THE CODE. AI HELPED ME UNDERSTAND THE CODE.

plt.figure(figsize=(12, 5))

plt.plot(x, y_1, color='blue', label='Site 10163000')
plt.plot(x, y_2, color='red', label='Site 10155200')
plt.plot(x, y_3, color='green', label='Site 10155500')
plt.plot(x, y_4, color='orange', label='Site 10154200')
plt.plot(x, y_5, color='purple', label='Site 10155000')

plt.title('Provo River Streamflow Rates - June 2021')
plt.xlabel('Date')
plt.ylabel('Streamflow Rate (cfs)')

plt.legend()

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.show()

