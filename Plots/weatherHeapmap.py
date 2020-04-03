import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Draw a heatmap to represent the recorded max temperature  on day of week and month of year.
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['record_max_temp'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Recorded max temperature from June 2014/15', xaxis_title="Day of Week",
                   yaxis_title="Month of year")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherHeatmap.html')
