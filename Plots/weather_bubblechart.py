import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from x column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

new_df = df.groupby(['month']).agg(
    {'average_min_temp': 'mean', 'average_max_temp': 'mean'}).reset_index()

data = [
    go.Scatter(x=new_df['average_min_temp'],
               y=new_df['average_max_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['average_max_temp'], color=new_df['average_max_temp'], showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average Min and Max Temperature of Each Month Weather',
                   xaxis_title="Min Temperature", yaxis_title="Max Temperature", hovermode='closest')

# Plot the figure and save it in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weather_bubblechart.html')