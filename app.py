import plotly_express as px
import plotly.graph_objs as go

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
from dash.dependencies import Input, Output, State
import dash_table
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.FLATLY]
)

app.config['suppress_callback_exceptions'] = True

navbar = dbc.NavbarSimple(
    children=[],
    brand="Beetle",
    color="primary",
    dark=True
)

card_content_1 = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

card_content_2 = dbc.CardBody(
    [
        html.Blockquote(
            [
                html.P(
                    "A learning experience is one of those things that says, "
                    "'You know that thing you just did? Don't do that.'"
                ),
                html.Footer(
                    html.Small("Douglas Adams", className="text-muted")
                ),
            ],
            className="blockquote",
        )
    ]
)

card_content_3 = [
    dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
    dbc.CardBody(
        [
            html.H5("Card with image", className="card-title"),
            html.P(
                "This card has an image on top, and a button below",
                className="card-text",
            ),
            dbc.Button("Click me!", color="primary"),
        ]
    ),
]


cards = dbc.CardColumns(
    [
        dbc.Card(card_content_1, color="primary", inverse=True),
        dbc.Card(card_content_2, body=True),
        dbc.Card(card_content_1, color="secondary", inverse=True),
        dbc.Card(card_content_3, color="info", inverse=True),
        dbc.Card(card_content_1, color="success", inverse=True),
        dbc.Card(card_content_1, color="warning", inverse=True),
        dbc.Card(card_content_1, color="danger", inverse=True),
        dbc.Card(card_content_3, color="light"),
        dbc.Card(card_content_1, color="dark", inverse=True),
    ]
)


app.layout = html.Div(
    [
        navbar,
        dbc.Row([dbc.Col(
            cards
    )])
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)