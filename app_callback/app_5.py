from dash import Dash, callback, Input, Output, State, callback, html, dcc, State
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H1("DropDown Radio", style = {'textAlign':'center'}),
    dcc.Dropdown(options = ['Texas', 'Michigan', 'California'], value = 'Texas', clearable=True, id='demo-dropdown'),
    html.Button('Submit', id='submit_button', n_clicks=0),
    dcc.RadioItems(options = ['Dallas','Arlington','Austin'], id='radio_btn', inline=True),
])

@callback(
    Output('radio_btn', 'options'),
    Input('submit_button', 'n_clicks'),
    State('demo-dropdown', 'value')
)
def update_text(n_clicks, chosen_state):
    if n_clicks > 0:
        print(chosen_state)
        # Handle None case when dropdown is cleared
        if chosen_state is None:
            return []
        elif chosen_state == 'Texas':
            return ['Dallas','Arlington','Austin']
        elif chosen_state == 'California':
            return ['San Francisco','San Jose','LA']
        elif chosen_state == 'Michigan':
            return ['Troy','Auburn Hills','Milford']
        else:
            return []
    return ['Dallas','Arlington','Austin']


if __name__ == '__main__':
    app.run(debug=True)