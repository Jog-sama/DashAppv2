import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from flask import Flask


app = Dash(__name__)

df = pd.read_csv("intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[
    ['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:50])
# to only describe this particular column
df["Pct of Colonies Impacted"].describe()

app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash",
            style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_period",
                 options=[
                     {"label": "2015- JAN THRU MAR ",
                         "value": '2015- JAN THRU MAR'},
                     {"label": "2015- APR THRU JUN", "value": '2015- APR THRU JUN'},
                     {"label": "2015- JUL THRU SEPT",
                         "value": '2015- JUL THRU SEPT'},
                     {"label": "2015- OCT THRU DEC", "value": '2015- OCT THRU DEC'},
                     {"label": "2016- JAN THRU MAR", "value": '2016- JAN THRU MAR'},
                     {"label": "2016- APR THRU JUN", "value": '2016- APR THRU JUN'},
                     {"label": "2016- JUL THRU SEPT",
                         "value": '2016- JUL THRU SEPT'},
                     {"label": "2016- OCT THRU DEC", "value": '2016- OCT THRU DEC'},
                     {"label": "2017- JAN THRU MAR", "value": '2017- JAN THRU MAR'},
                     {"label": "2017- APR THRU JUN", "value": '2017- APR THRU JUN'},
                     {"label": "2017- JUL THRU SEPT",
                         "value": '2017- JUL THRU SEPT'},
                     {"label": "2017- OCT THRU DEC", "value": '2017- OCT THRU DEC'},
                     {"label": "2018- JAN THRU MAR", "value": '2018- JAN THRU MAR'},
                     {"label": "2018- APR THRU JUN", "value": '2018- APR THRU JUN'},
                     {"label": "2018- JUL THRU SEPT",
                         "value": '2018- JUL THRU SEPT'},
                     {"label": "2018- OCT THRU DEC", "value": '2018- OCT THRU DEC'},
                     {"label": "2019- JAN THRU MAR", "value": '2019- JAN THRU MAR'},
                     {"label": "2019- APR THRU JUN", "value": '2019- APR THRU JUN'},
                     {"label": "2019- JUL THRU SEPT",
                         "value": '2019- JUL THRU SEPT'},
                     {"label": "2019- OCT THRU DEC", "value": '2019- OCT THRU DEC'}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

if __name__ == '__main__':
    app.run_server(debug=True)
