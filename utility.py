import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np


# LOAD DATA ONCE
@st.experimental_singleton
def load_data():
    data = pd.read_csv(
        "uber-raw-data-sep14.csv.gz",
        nrows=80000,
        names=[
            "date/time",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=["date/time"],)

    data["date/time"] = pd.to_datetime(data["date/time"], format="%H:%M")
    data["date/time"] = data["date/time"].dt.strftime('%H:%M')
    return data

@st.experimental_memo
def sample_data(data, sample_size): 
    return data.sample(sample_size)

# lat and long correspond to the center of the plot
# we compute it by taking the average of lat and long from the data we recieve
def get_map(data, lat=None, lon=None):
    if lat is None:
        lat = np.average(data["lat"])
    if lon is None: 
        lon = np.average(data["lon"])

    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": 12,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    opacity=0.25,
                    get_position=["lon", "lat"],
                    radius=35,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    wireframe=True,
                    extruded=True,
                ),
            ],
        )
    )

def get_famous_points(): 
    return {"Central Park": {'lat': 40.785091, 'lon': -73.968285},
                 "Brooklyn Bridge":{'lat': 40.7061, "lon": -73.9969},
                 "Empire State Building": {'lat': 40.7484, 'lon': -73.9857} , 
                 "Time Square": {'lat': 40.7580, 'lon': -73.9855}, 
                 "La Guardia": {"lat": 40.7769, "lon": -73.8740},
                 "Madison Square Garden": {'lat': 40.7505, "lon": -73.9934}, 
                 "Yankee Stadium": {"lat": 40.8296, "lon": -73.9262}, 
                 "JFK Airport": {'lat': 40.6413, "lon": -73.7781}}


def get_filtered_data(start_time, end_time, data): 
    # transform to string for comparison
    start_time = start_time.strftime("%H:%M")
    end_time = end_time.strftime("%H:%M")
    filtered_data = data[((data["date/time"] >= start_time) & (data["date/time"] <= end_time))]
    return filtered_data


def get_line_chart(data): 
    return data.groupby(by=["date/time"]).count()[["lat"]].rename(columns={"lat": "Number of pickups"})