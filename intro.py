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
df = pd.read_csv("ir_master_fbdat_mod1_final.csv")

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

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
    html.P("This graph represents a change in baseline measurement of Facebook users' physical movement in various regions of Iraq. "
           "The baseline measurement was taken in Feb. 2020, before COVID19 movement restrictions."
           "In addition, Armed Conflict Location & Event Data Project data"
           " has been added by region for comparison and analysis."),
    html.Br(),
    html.P("Data Sources:"),
    html.Br(),
    html.P("https://data.humdata.org/dataset/c3429f0e-651b-4788-bb2f-4adbf222c90e"),
    html.Br(),
    html.P("https://acleddata.com/"),
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
    fig = px.bar(dff, x='Date', y='Baseline Movement Deviation', color='Baseline Movement Deviation')
    fig2 = px.bar(dff, x='Date', y='Attacks')
    fig3 = px.scatter(dff, x='Date', y='Attacks', size='Dsize')
    fig.add_trace(fig2.data[0])
    fig.add_trace(fig3.data[0])
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
