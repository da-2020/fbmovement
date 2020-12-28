# ------------------------------------------------------------------------------
# Iraq Facebook Users Change In Movement From FEB2020 Baseline By Region
# Code derived from https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Other/Dash_Introduction
# Modified by Daniel Allen
# ------------------------------------------------------------------------------

import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server
# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("ir_master_fbdat.csv")

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Iraq Facebook Users Change In Movement From FEB2020 Baseline By Region", style={'text-align': 'center'}),
    html.Br(),
    html.H3("Daniel Allen", style={'text-align': 'center'}),
    html.Br(),
    dcc.Dropdown(id="slct_region",
                 options=[
                     {"label": "Abu Ghraib", "value": 'Abu Ghraib'},
                     {"label": "Al Fallujah", "value": 'Al Fallujah'},
                     {"label": "Al Haditha", "value": 'Al Haditha'}],


                 multi=False,
                 value='Abu Ghraib',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    html.P("This graph represents a change in baseline measurement of Facebook users' physical movement in various regions of Iraq. The baseline measurement was taken in Feb. 2020, before COVID19 movement restrictions."),
    html.Br(),
    html.Link("Data Source", href="https://data.humdata.org/dataset/c3429f0e-651b-4788-bb2f-4adbf222c90e"),
    html.Br(),

    dcc.Graph(id='iraq_chart', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='iraq_chart', component_property='figure')],
    [Input(component_id='slct_region', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The region chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Region"] == option_slctd]

    # Plotly Express
    fig = px.bar(dff, x='Date', y='Baseline Movement Deviation')

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
