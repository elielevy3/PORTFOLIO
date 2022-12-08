# EXERCISE_UBER
Streamlit exercice for the 30/11/2022 Wyseday


## Useful functions in utility.py

### load_data(): return a dataframe with the following columns: 

#### - Latitude of the pickup
#### - Longitude of the pickup
#### - Hour of the pickup (HH:MM)

----------------------------
                                                              
### sample_data(data, sample_size):
#### - return a sample of the dataframe [data] of size [sample_size]

----------------------------

### get_map(data, lat=None, lon=None):
#### - return None but write a Pydeck plot including datapoints in data
#### - data points in data must be of the form ["lat", "lon"]
#### - careful about coordinates: 40.7484° N, 73.9857° W is equivalent to [40.7484, -73.9857]
#### - lat and lon parameters are used to determine the initial center of the map plot
#### - if lat and lon are not passed, the centroid of the group of points passed in data is computed and used

----------------------------
                                     
### get_famous_points(): 
#### - return a dictionnary of the following shape: {"Famous point name": {"lat": val, "lon": val}}

----------------------------

### get_filtered_data(start_time, end_time, data): 
#### - return a dataframe with of the following shape: ["date/time",   "lat", "lon"]
#### - start_time and end_time must be of type datetime
#### - data must be of the shape ["date/time", "lat", "lon"] with "date/time" as string

----------------------------

### get_line_chart(data): 
#### - return dataframe with the following shape: ["Number of pickups"]
#### - group data by time and count number of pickups for a given HH:MM time
                                           
