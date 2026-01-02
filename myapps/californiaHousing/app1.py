import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input

df = pd.read_csv('housing.csv')

app = Dash(__name__)

'''
* children = what goes INSIDE the <div>
* The Dash Core Components (dash.dcc) module includes a Graph component called dcc.Graph.
'''
app.layout = [
    html.Div(children = 'Dashboard'),
    dash_table.DataTable(data=df.to_dict('records'), page_size = 20),
    html.Div([
        html.Label('Select Feature: '),
        dcc.Dropdown(
            id = 'Feature-Dropdown',
            options = [{'label' : col, 'value': col} for col in df.columns],
            value = df.columns[0]
        )
    ]),

    dcc.Graph(id='Histogram')
]

@callback(
    Output(component_id = 'Histogram', component_property='figure'),
    Input(component_id = 'Feature-Dropdown', component_property='value')
)
def update_histogram(selected_features):
    fig = px.histogram(df, x = selected_features)
    fig.update_layout(title = f'Histogram of {selected_features}',
                        xaxis_title = selected_features,
                        yaxis_title = "Frequency"
    )
    return fig


if __name__ == '__main__':
    app.run(debug = True)