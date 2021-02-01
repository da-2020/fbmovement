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
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server
# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("ir_master_fbdat_mod1_final.csv")

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div(
children=[
    html.H1("Iraq Facebook Users Change In Movement From FEB2020 Baseline and ACLED Attack Data By Region ", style={'text-align': 'center'}),
    html.Br(),
    html.H3("Daniel Allen", style={'text-align': 'center'}),
    html.Br(),
    dcc.Dropdown(id="slct_region",
                 options=[
                     {"label": "Abu Ghraib", "value": "Abu Ghraib"},
                     {"label": "Al Fallujah", "value": "Al Fallujah"},
                     {"label": "Al Haditha", "value": "Al Haditha"},
                     {"label": "Al Qaim", "value": "Al Qaim"},
                     {"label": "Anah", "value": "Anah"},
                     {"label": "Ar Ramadi", "value": "Ar Ramadi"},
                     {"label": "Ar Rutbah", "value": "Ar Rutbah"},
                     {"label": "Hit", "value": "Hit"},
                     {"label": "Kadhimiya", "value": "Kadhimiya"},
                     {"label": "Adhamiya", "value": "Adhamiya"},
                     {"label": "An Nasiriyah", "value": "An Nasiriyah"},
                     {"label": "Chibayish", "value": "Chibayish"},
                     {"label": "Refai", "value": "Refai"},
                     {"label": "Shatrah", "value": "Shatrah"},
                     {"label": "Suq ash Shuyukh", "value": "Suq ash Shuyukh"},
                     {"label": "Amedi", "value": "Amedi"},
                     {"label": "Dahuk", "value": "Dahuk"},
                     {"label": "Simele", "value": "Simele"},
                     {"label": "Zakho", "value": "Zakho"},
                     {"label": "Al Khalis", "value": "Al Khalis"},
                     {"label": "Al Miqdadiyah", "value": "Al Miqdadiyah"},
                     {"label": "Baqubah", "value": "Baqubah"},
                     {"label": "Balad Ruz", "value": "Balad Ruz"},
                     {"label": "Khanaqin", "value": "Khanaqin"},
                     {"label": "Kifri", "value": "Kifri"},
                     {"label": "Karbala", "value": "Karbala"},
                     {"label": "Al Amarah", "value": "Al Amarah"},
                     {"label": "Al Kahla", "value": "Al Kahla"},
                     {"label": "Al Miamona", "value": "Al Miamona"},
                     {"label": "Al Mijar al Kabir", "value": "Al Mijar al Kabir"},
                     {"label": "Ali al Gharbi", "value": "Ali al Gharbi"},
                     {"label": "Qalat Salih", "value": "Qalat Salih"},
                     {"label": "Tilkef", "value": "Tilkef"},
                     {"label": "Akre", "value": "Akre"},
                     {"label": "Al Hamdaniyah", "value": "Al Hamdaniyah"},
                     {"label": "Mosul", "value": "Mosul"},
                     {"label": "Sinjar", "value": "Sinjar"},
                     {"label": "Talafar", "value": "Talafar"},
                     {"label": "Al Door", "value": "Al Door"},
                     {"label": "Al Shirkat", "value": "Al Shirkat"},
                     {"label": "Balad", "value": "Balad"},
                     {"label": "Bayji", "value": "Bayji"},
                     {"label": "Samarra", "value": "Samarra"},
                     {"label": "Tikrit", "value": "Tikrit"},
                     {"label": "Al Hayy", "value": "Al Hayy"},
                     {"label": "Al Kut", "value": "Al Kut"},
                     {"label": "As Suwayrah", "value": "As Suwayrah"},
                     {"label": "Badrah", "value": "Badrah"},
                     {"label": "Abu al Khasib", "value": "Abu al Khasib"},
                     {"label": "Al Faw", "value": "Al Faw"},
                     {"label": "Al Madiana", "value": "Al Madiana"},
                     {"label": "Al Qurnah", "value": "Al Qurnah"},
                     {"label": "Al Zubair", "value": "Al Zubair"},
                     {"label": "Basrah", "value": "Basrah"},
                     {"label": "Shatt Al Arab", "value": "Shatt Al Arab"},
                     {"label": "Al Khithir", "value": "Al Khithir"},
                     {"label": "As Samawah", "value": "As Samawah"},
                     {"label": "Rumaitha", "value": "Rumaitha"},
                     {"label": "Ad Diwaniyah", "value": "Ad Diwaniyah"},
                     {"label": "Afak", "value": "Afak"},
                     {"label": "Al Hamza", "value": "Al Hamza"},
                     {"label": "Shamiya", "value": "Shamiya"},
                     {"label": "Al Kufa", "value": "Al Kufa"},
                     {"label": "Al Manathera", "value": "Al Manathera"},
                     {"label": "Najaf", "value": "Najaf"},
                     {"label": "Arbil", "value": "Arbil"},
                     {"label": "Choman", "value": "Choman"},
                     {"label": "Koisnjaq", "value": "Koisnjaq"},
                     {"label": "Makhmur", "value": "Makhmur"},
                     {"label": "Mergasur", "value": "Mergasur"},
                     {"label": "Shaqlawa", "value": "Shaqlawa"},
                     {"label": "Soran", "value": "Soran"},
                     {"label": "Sulaymaniya", "value": "Sulaymaniya"},
                     {"label": "Chamchamal", "value": "Chamchamal"},
                     {"label": "Darbandokeh", "value": "Darbandokeh"},
                     {"label": "Dukan", "value": "Dukan"},
                     {"label": "Halabja", "value": "Halabja"},
                     {"label": "Kalar", "value": "Kalar"},
                     {"label": "Penjwin", "value": "Penjwin"},
                     {"label": "Pshdar", "value": "Pshdar"},
                     {"label": "Rania", "value": "Rania"},
                     {"label": "Sharbazher", "value": "Sharbazher"},
                     {"label": "Daquq", "value": "Daquq"},
                     {"label": "Haweeja", "value": "Haweeja"},
                     {"label": "Kirkuk", "value": "Kirkuk"},
                     {"label": "Al Madain", "value": "Al Madain"},
                     {"label": "Al Hashimiyah", "value": "Al Hashimiyah"},
                     {"label": "Al Hillah", "value": "Al Hillah"},
                     {"label": "Al Mahawil", "value": "Al Mahawil"},
                     {"label": "Al Misiab", "value": "Al Misiab"},
                     {"label": "Mahmudiya", "value": "Mahmudiya"}],

                 multi=False,
                 value='Abu Ghraib',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    html.P("This graph represents the change in a baseline measurement of Facebook users' physical movement in various regions of Iraq. "
           "The baseline measurement was taken in Feb. 2020, before COVID19 movement restrictions."
           " In addition, Armed Conflict Location & Event Data Project (ACLED) data"
           " has been added by region for comparison and analysis. Each red dot represent an attack or disturbance as coded by ACLED."
           " Finally, the change in a baseline measurement of static Facebook users is depicted for additional context."),
    html.P("Data Sources:"),
    html.A("Facebook Data", href="https://data.humdata.org/dataset/c3429f0e-651b-4788-bb2f-4adbf222c90e"),
    html.A(" ACLED Data", href="https://acleddata.com/"),
    html.Br(),
    dbc.Spinner(children=[dcc.Graph(id='iraq_chart', figure={})], size="lg", color="dark", type="grow", fullscreen=True,),
    ]
)


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
    dff = dff[dff["region"] == option_slctd]
    df1 = dff[dff["region"] == option_slctd].copy()
    df2 = df1[['movdev', 'attacksbool']]
    statdat = df2.corr()
    statcon = "The Pearsons R correlation of this data is: {}".format(statdat)

    # Plotly Express
    fig = px.area(dff, x='date', y='movdev', labels={'date': 'Date', 'movdev': 'Baseline User Movement Deviation'},
                  template="plotly_dark")
    fig.add_trace((go.Scatter(x=dff.date, y=dff.staticusers, name='Baseline Static User Deviation', fill='tozeroy',
                              line=dict(color='#565656', width=2))))
    fig.add_trace(
        (go.Scatter(x=dff.date, y=dff.attacks, mode='markers', name='Attacks/Disturbances', text=dff.attacktype)))

    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    fig.update_traces(marker=dict(size=12, color='Red', line=dict(width=2, color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

#    return container, fig
    return container, statcon, fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
