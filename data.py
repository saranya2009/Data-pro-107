
import pandas as pd
import csv
import plotly
import plotly_express as px
import plotly.graph_objects as go

df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/Python/Pro-107/project-files/data.csv")
# print(df.groupby("level")["attempt"].mean())
mean = df.groupby(["student_id", "level"], as_index= False)["attempt"].mean()

fig = px.scatter(mean, x = "student_id" , y = "level", size = 'attempt', color = 'attempt')
plotly.offline.plot(fig)