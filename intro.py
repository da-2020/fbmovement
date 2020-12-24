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
df = pd.read_csv("FBLOCDENSE_IR_STRIP_AG.csv")

#df = df.groupby(['date', 'mov-dev', 'no-move-ratio'])[['no-move-ratio']].mean()
#df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
#df.reset_index(inplace=True)
print(df[:5])

dff = df.copy()
fig = px.bar(dff, x='date', y='mov-dev')
fig.show()

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Abu Ghraib Change In Movement Baseline from FEB2020", style={'text-align': 'center'}),
    html.Br()
    html.H3("Daniel Allen", style={'text-align': 'center'})
    html.Br(),
    html.P("This graph represents a change in baseline measurement of Facebook users in the Abu Ghraib region of Iraq. The baseline measurement was taken in Feb. 2020, before COVID19 movement restrictions."),
    html.Br(),
    html.Link("Data Source", href="https://data.humdata.org/dataset/c3429f0e-651b-4788-bb2f-4adbf222c90e"),

    html.Br(),

    dcc.Graph(figure=fig)


])



# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
