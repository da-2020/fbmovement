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

df = df.groupby(['date', 'mov-dev', 'no-move-ratio'])[['no-move-ratio']].mean()
df.reset_index(inplace=True)
print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Template Application Daniel Allen", style={'text-align': 'center'}),

    html.Br(),

    dcc.Graph(irqbar)


])

dff = df.copy()
fig = px.bar(dff, x='date', y='mov-dev')
irqbar = fig.show()

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
