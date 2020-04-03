import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data
trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Maximum')
trace2 = go.Scatter(x=df['date'], y=df['average_min_temp'], mode='lines', name='Minimum')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Mean')
data = [trace1,trace2,trace3]


# Preparing layout
layout = go.Layout(title='Actual Maximum, Minimum, Mean temperature of each month in weather statistics From June 2014-15', xaxis_title="Date",
                   yaxis_title="Actual Max,Min,Mean Temperatures")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Weathermultilinechart.html')
