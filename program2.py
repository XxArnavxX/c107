import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

ref = pd.read_csv('./data.csv')
student = ref.loc[ref['student_id'] == "TRL_987"]
av = student.groupby("level")["attempt"].mean()
gra = go.Figure(go.Bar(x = av, y = ['level 1', 'level 2', 'level 3', 'level 4'],orientation = 'h'))
gra.show()
