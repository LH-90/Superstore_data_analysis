# Librairies importation

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


# Dataset importation
url="https://raw.githubusercontent.com/LH-90/Superstore_data_analysis/main/Merged_Supertore.csv"

df= pd.read_csv(url)

# Figure 1

# Group by "State"
state_product = df.groupby("State")["Quantity"].sum()
state_product = state_product.reset_index()

from urllib.request import urlopen
import json

geo_states='https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json'
with urlopen(geo_states) as file:
    geo_states= json.load(file)

# Create a choropeth with Plotly
fig_states = px.choropleth_mapbox(
    state_product,
    geojson=geo_states,
    locations="State",
    featureidkey="properties.NAME",
    color="Quantity",
    color_continuous_scale="Blues",
    mapbox_style="carto-positron",
)

# Update the map layout to cover the entire USA
fig_states.update_layout(
    mapbox=dict(
        center=dict(lat=37, lon=-95),
        zoom=3,
    ),
)
     

# figure 2


# Group by "State" and "City"
state_city = df.groupby(["State", "City"])["Quantity"].sum()
state_city = state_city.reset_index()

# Merge "state_city" and df3
df2 = df[["State", "City", "Latitude ", "Longitude "]]
df3 = pd.merge(state_city, df2, on=["State", "City"], how="left")

# Select only the data related to California
california = df3[df3["State"] == "California"]
     

# Create a bubble map
fig = px.scatter_mapbox(california, lat="Latitude ", lon="Longitude ", size="Quantity",
                        zoom=4, mapbox_style="open-street-map", hover_name="City",
                        size_max=30)  # Adjust size_max to control the maximum size of bubbles


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
        html.H1("Superstore Sales in USA", className="Dashboard-title"),
        html.Div([
            html.H1("Quantity of products sold in each state", className="title"),
            dcc.Graph(figure=fig_states)
            ],className="section1"),
        html.Div([
            html.H1("Quantity of products sold in California cities", className="title"),
            dcc.Graph(figure=fig)
            ],className="section2"),
 ], className="mainSection")


# Run the app
if __name__ == '__main__':
    app.run(port= 8000, debug=True)