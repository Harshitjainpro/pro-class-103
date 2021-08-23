import pandas as p
import plotly_express as px

df = p.read_csv("Copy+of+data+-+data.csv")
fig = px.scatter(df,x = "date", y= "cases", color="country",size_max=60,title="Covid data")
fig.show()