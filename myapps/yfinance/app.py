import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from dash import Dash, callback,  dcc, html, Input, Output, State

app = Dash(__name__)

app.layout = html.Div(
    style={'backgroundColor' : '#000000', 'color': '#FFFFFF', 'padding' : '20px'},
    children = [
        html.H1("Stock CandleStick Chart Tool", style={'textAlign' : 'center', 'color' : '#FFFFFF'}),
        html.Div([
            html.Label('Enter Stock Ticker Symbol: ', style = {'color' : '#FFFFFF'}),
            dcc.Input(id='ticker-input', type = 'text', value = 'AAPL',
            style={'backgroundColor' : '#333333', 'color' : '#FFFFFF', 'padding' : '5px'})
        ],
        style = {'padding' : '10px'},
        ),

        html.Div([
            html.Label('Select Start Date: ', style = {'color' : '#FFFFFF', 'marginBottom': '5px', 'fontSize': '14px'}),
            dcc.DatePickerSingle(id='start-date-picker', date='2022-11-01', display_format='YYYY-MM-DD', first_day_of_week=1,
            className='compact-datepicker',
        )
        ], style={'padding': '10px', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            html.Label('Select End Date: ', style = {'color' : '#FFFFFF', 'marginBottom': '5px', 'fontSize': '14px'}),
            dcc.DatePickerSingle(id='end-date-picker', date='2023-12-01', display_format='YYYY-MM-DD', first_day_of_week=1,
            className='compact-datepicker',
        )
        ], style={'padding': '10px', 'display': 'inline-block', 'verticalAlign': 'top'}),

        # Range Slider
        html.Div([
            dcc.Checklist(
                id='toggle-rangeslider',
                options=[{"label": " Include Range Slider", "value": "slider"}],
                value=["slider"],  # Default: rangeslider is visible
                style={'color': '#FFFFFF'}
            )
        ], style={'padding': '10px', 'textAlign': 'center'}),

        html.Div([
            html.Button('Submit', id='submit-button', n_clicks = 0, className='submit-btn')
        ], style={'padding': '10px', 'textAlign' : 'center'}),

        html.Div(id='chart-container', style={'visibility': 'hidden'}, 
        children=[
            dcc.Graph(id='candlestick-chart', style={'backgroundColor': '#111111'})
        ])
    ]
)


@app.callback(
    [Output('candlestick-chart','figure'),
    Output('chart-container', 'style')],
    [Input('submit-button', 'n_clicks'),
    Input('toggle-rangeslider', 'value')],
    [State('ticker-input', 'value'),
    State('start-date-picker', 'date'),
    State('end-date-picker', 'date')]
)
# Dash does NOT match function arguments by name. It matches them by POSITION.
def update_chart(n_clicks, rangeslider_value, ticker, start_date, end_date):
    if n_clicks > 0:
        try:
            df = yf.download(ticker, start = start_date, end = end_date)
            print(f"Downloaded {len(df)} rows for {ticker}")
            print(df)
            
            # Handle MultiIndex columns (yfinance sometimes returns MultiIndex)
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.droplevel(1)
            
            # Ensure we have the required columns and data
            if df.empty or not all(col in df.columns for col in ['Open', 'High', 'Low', 'Close']):
                return go.Figure(), {'visibility': 'hidden'}

            fig = go.Figure(data = [go.Candlestick(
                x = df.index, 
                open = df['Open'], 
                close = df['Close'], 
                high = df['High'], 
                low = df['Low']
            )])

            # Toggle rangeslider visibility - convert to boolean
            show_rangeslider = "slider" in rangeslider_value if rangeslider_value else False

            fig.update_layout(
                title=f'CandleStick Chart of {ticker}',
                xaxis_title ='Date',
                yaxis_title='Price (USD)',
                xaxis_rangeslider_visible=show_rangeslider,
                template='plotly_dark',
                height=600,
                paper_bgcolor='#000000',
                plot_bgcolor='#111111'
            )

            return fig, {'visibility': 'visible'}

        except Exception as e:
            print(f"Error downloading data: {e}")
            return go.Figure(), {'visibility': 'hidden'}
    
    return go.Figure(), {'visibility': 'hidden'}

    



# Run the app
if __name__ == '__main__':
    app.run(debug=True)