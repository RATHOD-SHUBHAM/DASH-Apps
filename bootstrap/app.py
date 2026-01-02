import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas_datareader.data as web
import datetime
import time

df = pd.read_csv("mystocks.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY],
          meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.title = "Shubham Shankar"

cache_buster = str(int(time.time()))

app.index_string = f'''
<!DOCTYPE html>
<html>
    <head>
        {{%metas%}}
        <title>{{%title%}}</title>
        <link rel="icon" type="image/png" href="/assets/favicon.png?v={cache_buster}">
        {{%css%}}
    </head>
    <body>
        {{%app_entry%}}
        <footer>
            {{%config%}}
            {{%scripts%}}
            {{%renderer%}}
        </footer>
    </body>
</html>
'''

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("Bootstrap Stock Market DashBoard", className='text-uppercase text-center mb-4'), width=12),
    ),
    
    # FIRST ROW
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='my-dpdn', 
                multi=False, 
                value='AMZN',
                options=[{'label': x, 'value': x} for x in sorted(df['Symbols'].unique())],
            ),
            dcc.Graph(id='line-fig', figure={}, style={'height': '400px'})
        ], xs=12, sm=12, md=12, lg=5, xl=5),
        
        dbc.Col([
            dcc.Dropdown(
                id='my-dpdn2', 
                multi=True, 
                value=['PFE', 'BNTX'],
                options=[{'label': x, 'value': x} for x in sorted(df['Symbols'].unique())],
            ),
            dcc.Graph(id='line-fig2', figure={}, style={'height': '400px'})
        ], xs=12, sm=12, md=12, lg=5, xl=5),
    ], justify='around', className='mb-4'),

    # SECOND ROW - Fixed checklist spacing
    dbc.Row([
        dbc.Col([
            html.P("Select Company Stock:", 
                   style={"textDecoration": "underline", "fontSize": "18px", "fontWeight": "bold"}),
            dcc.Checklist(
                id='my-checklist', 
                value=['FB', 'GOOGL', 'AMZN'],
                options=[{'label': x, 'value': x} for x in sorted(df['Symbols'].unique())],
                labelStyle={'marginBottom': '10px'},  # Changed: vertical list with spacing
                inputStyle={"marginRight": "10px"},  # Space between checkbox and label
                inline = True
            ),
            dcc.Graph(id='my-hist', figure={}, style={'height': '400px', 'marginTop': '20px'}),
        ], xs=12, sm=12, md=12, lg=5, xl=5),

        dbc.Col([
            dbc.Card([
                dbc.CardBody(
                    html.P("We're better together. Help each other out!", className="card-text")
                ),
                dbc.CardImg(
                    src="https://media.giphy.com/media/Ll0jnPa6IS8eI/giphy.gif",
                    bottom=True
                ),
            ], style={"width": "24rem"}),
        ], xs=12, sm=12, md=12, lg=5, xl=5)
    ], justify='around', align="center", className='mb-4')

], fluid=True)


# Callbacks
@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'] == stock_slctd]
    figln = px.line(dff, x='Date', y='High', title=f'{stock_slctd} Stock High Price')
    figln.update_layout(height=400)
    return figln


@app.callback(
    Output('line-fig2', 'figure'),
    Input('my-dpdn2', 'value')
)
def update_graph2(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    figln2 = px.line(dff, x='Date', y='Open', color='Symbols', title='Multiple Stocks Open Price')
    figln2.update_layout(height=400)
    return figln2


@app.callback(
    Output('my-hist', 'figure'),
    Input('my-checklist', 'value')
)
def update_graph3(stock_slctd):
    print(f"Selected stocks: {stock_slctd}")  # Debug
    
    if not stock_slctd:  # Handle empty selection
        return px.histogram(title='Please select at least one stock')
    
    dff = df[df['Symbols'].isin(stock_slctd)]
    print(f"Filtered data shape: {dff.shape}")  # Debug
    
    # Instead of filtering by a specific date, let's show the latest date available
    if not dff.empty:
        latest_date = dff['Date'].max()
        dff = dff[dff['Date'] == latest_date]
        print(f"Data for {latest_date}: {dff.shape}")  # Debug
        
        fighist = px.histogram(dff, x='Symbols', y='Close', 
                              title=f'Stock Close Price on {latest_date}',
                              color='Symbols')
        fighist.update_layout(height=400, showlegend=False)
        return fighist
    
    # If no data, return empty figure with message
    empty_fig = px.histogram(title='No data available')
    empty_fig.update_layout(height=400)
    return empty_fig


if __name__ == '__main__':
    app.run(debug=True)