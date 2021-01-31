import pandas as pd
from math import radians, cos, sin, asin, sqrt
import time

# Record the computing time.
start_time = time.time()

# Set Earth's radius.
radius = 6371

# Parse the fixed width texts into structured numerical data.
ColSpecs = [(11, 20), (21, 30)]
stations = pd.read_fwf("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt", colspecs=ColSpecs, header=None)

# (Optional) To use less memory and space, take only 1% of the stations.
stations = stations.iloc[::100, :]

# Compute the geographical distances using the Haversine formula (unit: kilometer).
def get_distance(long_a, lat_a, long_b, lat_b):

  # Transform to radians.
  long_a, lat_a, long_b, lat_b = map(radians, [long_a, lat_a, long_b, lat_b])

  distance = 2 * radius * asin(sqrt(sin((lat_b - lat_a) / 2) ** 2 + cos(lat_a) * cos(lat_b) * sin((long_b - long_a) / 2) ** 2))
  return abs(round(distance, 2))

# Get the adjacency matrix.

# Create an empty matrix.
matrix_dim = list(range(len(stations.index)))
adjacency_matrix = pd.DataFrame(index=matrix_dim, columns=matrix_dim)
print("The number of rows is " + str(len(stations.index)) + ".")

# Fill the matrix.
for i in matrix_dim:
    adjacency_matrix.iat[i, i] = 0
    for j in range(i + 1, matrix_dim[-1] + 1):
        distance = get_distance(stations.iat[i, 1], stations.iat[i, 0], stations.iat[j, 1], stations.iat[j, 0])
        adjacency_matrix.iat[i, j] = distance
        adjacency_matrix.iat[j, i] = distance
    print("Add the %sth row." % i)

print("--------------------")
print("The adjacency matrix:")
print(adjacency_matrix)
print("--------------------")
print("Computing used %s seconds." % round((time.time() - start_time), 2))
print("Save the adjacency matrix into a CSV file.")
adjacency_matrix.to_csv("/home/dning/GHCN/output.csv", index=False, header=False)