from dash import Dash, callback, Input, Output, State, callback, html, dcc
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Basic Radio Button", style = {'textAlign':'center'}),
    dcc.RadioItems(options = ['car', 'house', 'ship'], value='ship', id='select_item', inline=True),
    dcc.Markdown(children='', id='selected_items')
])

@callback(
    Output('selected_items', 'children'),
    Input('select_item', 'value')
)
def update_text(select_item):
    return f"The selected item is {select_item}"


if __name__ == '__main__':
    app.run(debug=True)