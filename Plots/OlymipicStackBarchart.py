import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


# Sorting values and select top first 20 Countries
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold', marker={'color': '#FFD700'})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='All medals of Olympic 2016 in the first 20 country expect China', xaxis_title="Country",
                   yaxis_title="Number of cases", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='OlymipicStackBarchart.html')