import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')


# Removing empty spaces from Country column to avoid errors
filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# # Creating sum of number of cases group by State Column
# new_df = filtered_df.groupby(['State'])['Confirmed'].sum().reset_index()

# Sorting values and select top first 20 Countries
new_df = filtered_df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout
layout = go.Layout(title='Total medals of Olympic 2016', xaxis_title="First top 20 countries",
                   yaxis_title="Total number of medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='OlympicBarchart.html')
