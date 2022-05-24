import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px


app = Dash(__name__)
df = pd.read_csv('owid-covid-data.csv')

fig = px.bar(df, x='location', y='gdp_per_capita', barmode='group')

app.layout = html.Div(children=[html.H1(children='Hello Dash'),

	html.Div(children='''
		Dash: a web application framework for your data.
		'''),

	dcc.Graph(
		id='example-graph',
		figure=fig
		)
	])

if __name__=='__main__':
	app.run_server(debug=True)