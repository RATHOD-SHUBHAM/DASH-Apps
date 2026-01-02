from dash import Dash, callback, Input, Output, State, callback, html, dcc, State
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Submit Radio Button", style = {'textAlign':'center'}),
    dcc.RadioItems(options = ['car', 'house', 'ship'], value='ship', id='select_item', inline=True),
    html.Button('Submit', id='submit_button', n_clicks=0),
    dcc.Markdown(children='', id='selected_items')
])

@callback(
    Output('selected_items', 'children'),
    Input('submit_button', 'n_clicks'),
    State('select_item', 'value')
)
def update_text(n_clicks, select_item):
    if n_clicks > 0:
        return f"The selected item is {select_item}"


if __name__ == '__main__':
    app.run(debug=True)