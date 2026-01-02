from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
# print(df.head(5))

# ----------- Initialize the app ----------
app = Dash(__name__)

# ------------ App layout: DASH Component ---------------
app.layout = [
    html.H1(children = 'My First DASH APP', style = {'textAlign':'center'}),
    dcc.Dropdown(options = df.country.unique(), value = 'India', id = 'dropdown-selection'),
    dcc.Graph(id='graph-content')
]

# -------- Call Back ---------- Decorator ----------
@callback(
    Output('graph-content','figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    plot = px.line(dff, x='year', y='lifeExp')
    return plot

# ------ Entry Point ---------
if __name__ == '__main__':
    app.run(debug=True)