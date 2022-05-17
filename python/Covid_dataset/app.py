# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Note that this file is under development, and is not complete.

import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
from components import generate_table

app = Dash(__name__)

# Adding in custom colors
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

dfCovid = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

#df = df[df.population > 0]

markdown_text = '''
## Using Markdown

Markdown is a subset of html, so it makes sense that 
I can use soem markdown text in these dash.


'''

#print(df.columns)
#print(df.population.unique())

"""
df['norm_pop'] = df.population/1000000000
print(df.norm_pop.unique())
print(type(df.norm_pop[4]))
"""

#df.drop(df[(df['population'] == 'nan')].index, inplace=True)

dfFruit = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.scatter(df, x='gdp per capita', y='life expectancy',
	size="population", color="continent", hover_name="country",
	log_x=True, size_max=60)

fig.update_layout(
	plot_bgcolor=colors['background'],
	paper_bgcolor=colors['background'],
	font_color=colors['text']
	)

# packs into an app
app.layout = html.Div(children=[html.H1(children='Hello Dash'),

	html.Div(children='''
		Dash: a web application framework for your data.
		'''),

	dcc.Graph(
		id='example-graph',
		figure=fig
		),

	html.Div(children=[html.H2(children="Reusable Table Out"),
		html.H3(children='Covid Data'),
		html.P(children=""),
		generate_table(dfCovid)
		])
	])

if __name__=='__main__':
	app.run_server(debug=True)