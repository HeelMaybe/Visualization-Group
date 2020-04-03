import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#Draw a line chart to represent the actual max temperature of each month in weather statistics.
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data
data = [go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='month')]

# Preparing layout
layout = go.Layout(title='Actual max temperature of each month in weather statistics From June 2014-15', xaxis_title="Date",
                   yaxis_title="Max temperature of each month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Weatherlinechart.html')