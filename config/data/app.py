import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from pipeline import TradingPipeline
from strategies import bollinger_bands_strategy, keltner_channels_strategy

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Trading Dashboard", className="text-center mb-4"),

    # Pipeline per multi-ticker
    dbc.Row([
        dbc.Col([
            html.H4("Pipeline Multi-Ticker"),
            dcc.Dropdown(
                id="pipeline-strategy-selector",
                options=[
                    {"label": "Bollinger Bands", "value": "Bollinger Bands"},
                    {"label": "Keltner Channels", "value": "Keltner Channels"}
                ],
                placeholder="Seleziona Strategia"
            ),
            dcc.Input(id="pipeline-tickers", type="text", placeholder="Tickers separati da virgola (es. AAPL, MSFT)", className="mb-2"),
            dbc.Button("Avvia Pipeline", id="run-pipeline-btn", color="primary", className="mb-2"),
            html.Div(id="pipeline-status"),
        ], width=4),
        dbc.Col([
            html.H4("Log della Pipeline"),
            html.Div(id="pipeline-log")
        ], width=8)
    ])
])

@app.callback(
    [Output("pipeline-status", "children"),
     Output("pipeline-log", "children")],
    Input("run-pipeline-btn", "n_clicks"),
    [State("pipeline-strategy-selector", "value"),
     State("pipeline-tickers", "value")]
)
def run_pipeline(n_clicks, strategy, tickers_input):
    if n_clicks is None or not strategy or not tickers_input:
        return "Selezionare strategia e tickers.", ""

    try:
        # Prepara i tickers
        tickers = [ticker.strip() for ticker in tickers_input.split(",")]

        # Configura la pipeline
        if strategy == "Bollinger Bands":
            parameter_grid = {"Bollinger Window": range(10, 30, 5), "Num Std Dev": [1, 2, 3]}
            pipeline = TradingPipeline(strategy, tickers, parameter_grid, bollinger_bands_strategy)
        elif strategy == "Keltner Channels":
            parameter_grid = {"Keltner EMA Window": range(10, 30, 5), "ATR Multiplier": [1, 2, 3]}
            pipeline = TradingPipeline(strategy, tickers, parameter_grid, keltner_channels_strategy)
        else:
            return "Strategia non supportata.", ""

        # Esegui la pipeline
        pipeline.run()
        return "Pipeline completata con successo.", f"Pipeline per {strategy} completata su {', '.join(tickers)}."

    except Exception as e:
        return f"Errore: {str(e)}", ""
