from dash import Dash, callback, Input, Output, State, html, dcc
import plotly.express as px

df = px.data.tips()
print(df.head())

app = Dash(__name__)

"""
1. Wrapped the pie chart in a container div with display: 'none' initially
2. Added output for container style to show/hide it
3. Added proper validation - checks if chosen_data is not None and has the expected structure
4. Removed clickData={} and animate=True from the Graph component (not needed)
5. Returns empty figure with hidden style if conditions aren't met

"""

app.layout = html.Div([
    html.H1("Graph", style={'textAlign': 'center'}),
    dcc.Graph(
        figure=px.histogram(df, x='sex', y='tip'), 
        id='bar-graph'
    ),
    html.Div(id='graph-container', style={'display': 'none'}, children=[
        dcc.Graph(figure={}, id='my-graph')
    ])
])

@callback(
    [Output('my-graph', 'figure'),
     Output('graph-container', 'style')],
    Input('bar-graph', 'clickData'),
    prevent_initial_call=True
)
def update_text(chosen_data):
    if chosen_data is not None:
        print(chosen_data)
        print(type(chosen_data))
        
        # Check if clickData has the expected structure
        if 'points' in chosen_data and len(chosen_data['points']) > 0:
            
            extract_sex = chosen_data['points'][0]['x']
            print(extract_sex)
            dff = df[df.sex == extract_sex]
            print(dff.head())
            fig = px.pie(dff, names='smoker', values='total_bill',  title=f'Total bill by a {extract_sex} smoker')
            
            return fig, {'display': 'block'}  # Show the graph
        else:
            # No bar was clicked
            return {}, {'display': 'none'}
    
    # If Submit not clicked or no data
    return {}, {'display': 'none'}


if __name__ == '__main__':
    app.run(debug=True)