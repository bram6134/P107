import pandas as pandas
import csv
import plotly.graph_objects as graph_objects

fig = graph_objects.Figure(graph_objects.Bar(
    x=[4, 4.8, 9, 11.2, 12, 0.6],
    y=["Basketball", "Tennis", "Hockey", "Football", "Cricket", "Baseball"],
    orientation='h'
))

fig.show()