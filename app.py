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
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ]
)

app.config['suppress_callback_exceptions'] = True

navbar = dbc.NavbarSimple(
    children=[],
    brand="Beetle",
    color="primary",
    dark=True
)

icon_name = ['static/facebook.png', 'static/twitter.png', 'static/insta.png']
url_list = ['https://www.facebook.com/i80846dx2/',
            'https://twitter.com/i80486dx23419', 'https://www.instagram.com/takuya3419/']

my_img = dbc.CardColumns([
    dbc.Card(
        [dbc.CardImg(src="/static/face.png", top=True),
         dbc.CardBody([
             html.H5("Beetle", className="card-title"),
             dbc.Button(
                 "Contact",
                 color="primary",
                 id="collapse-button"
             ),
             dbc.Collapse(
                 [
                     dbc.Row([
                         dbc.Col(
                             html.A(
                                 html.Img(src=icon,
                                          height="50px"),
                                 href=link
                             )
                         )
                         for icon, link in zip(icon_name, url_list)])
                 ],
                 id="collapse",
                 style={'padding': '10pt 0 0 0',
                        'borderWidth': '0'}
             )
         ])]
    )
])

hobby_list = ['ドライブ', 'サイクリング', 'サカナクション', 'KIRINJI']
hobby = [
    dbc.CardHeader("趣味", style={'font-weight': 'bold'}),
    dbc.CardBody(
        [
            html.Li(
                key,
                className="card-text",
            )
            for key in hobby_list
        ]
    )
]

keyword = ['python', 'Raspberry Pi', 'IoT', 'plotly', 'Dash']
skills = [
    dbc.CardHeader('キーワード', style={'font-weight': 'bold'}),
    dbc.CardBody(
        [
            html.Li(
                key,
                className="card-text",
            )
            for key in keyword]
    )
]

sv = [
    dbc.CardImg(src="/static/sv.png", top=True),
    dbc.CardBody(
        [
            html.H5("シリコンバレー", className="card-title"),
            html.P(
                "シリコンバレーに２週間滞在し、現地で企業見学をしたりコワーキングスペースでIoTデバイスを開発したりした。"
            ),
            dbc.Button(dbc.CardLink(
                'Read more', href='https://i80486dx2.blogspot.com/'), color="light"),
        ]
    ),
]

nz = [
    dbc.CardImg(src="/static/nz.png", top=True),
    dbc.CardBody(
        [
            html.H5("ニュージーランド", className="card-title"),
            html.P(
                "ニュージーランドのワイカトにて、３週間に渡る語学研修に参加した。",
                className="card-text",
            ),
            dbc.Button(dbc.CardLink(
                'Read more', href='https://docs.google.com/presentation/d/1fwsToLe9pwLEZ9H8nWkKPj5uiYi_l79lv-2rPHA5yOQ/edit?usp=sharing'), color="light"),
        ]
    ),
]

e_2018 = ['6月 会津の未来を考える提言（アイデアソン）優秀賞受賞',
          '12月 Yahoo! Hack Day 2018　(学外ハッカソン) 出場']
e_2019 = ['2月 TDKハッカソン (学内ハッカソン)　優勝', '6月 Spa Jam　仙台予選 (学外ハッカソン) 出場', '7月 令和初ハッカソン　出場',
          '10月 健康作りハッカソン（学内ハッカソン）優秀賞受賞', '11月 目指せ愛されキャラ!推しキャラハッカソン （学外ハッカソン）最優秀賞受賞', '12月 GUGEN　一次審査突破　作品展示(東京)']
e_2020 = ['5月 コロナウイルスにITで立ち向かおう!　グッドアイディア賞 グッドプロトタイプ賞　受賞']

data = ['2018']
data.append(html.Br())
for y1 in e_2018:
    data.append(
        html.P(
            y1,
            className="card-text",
        )
    )
data.append('2019')
for y2 in e_2019:
    data.append(
        html.P(
            y2,
            className="card-text",
        )
    )
data.append(html.Br())
data.append('2020')
for y3 in e_2020:
    data.append(
        html.P(
            y3,
            className="card-text",
        )
    )
data.append(html.Br())

event = [
    dbc.CardHeader('出場イベント', style={'font-weight': 'bold'}),
    dbc.CardBody(
        [
            html.P(
                'アイデアソン：１件',
                className="card-text",
            ),
            html.P(
                'ハッカソン：８件',
                className="card-text",
            ),
            dbc.Button(
                "Read more",
                color="light",
                id="collapse-button2"
            ),
            dbc.Collapse(
                data,
                id="collapse2",
                style={'padding': '10pt 0 0 0'}
            )
        ]
    )
]

cards = html.Div([
    dbc.CardColumns([
        dbc.Card(hobby, color="primary", inverse=True),
        dbc.Card(skills, color="dark", inverse=True),
        dbc.Card(hobby, color="secondary", inverse=True),
        dbc.Card(sv, color="info", inverse=True),
        dbc.Card(hobby, color="light", inverse=True),
        dbc.Card(hobby, color="warning", inverse=True),
        dbc.Card(event, color="danger", inverse=True),
        dbc.Card(nz, color="success"),
        dbc.Card(hobby, color="dark", inverse=True),
    ])
])


app.layout = html.Div([
    navbar,
    dbc.Row([
        dbc.Col(
            [
                my_img
            ],
            style={'padding': '30pt 0 0 0'},
            width={'size': 6, 'offset': 3}
        ),
        dbc.Col(
            [
                cards
            ],
            style={'padding': '30pt 0 0 0'},
            width={'size': 6, 'offset': 3}
        )
    ]
    )
])


@ app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@ app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button2", "n_clicks")],
    [State("collapse2", "is_open")],
)
def toggle_collapse2(n, is_open):
    if n:
        return not is_open
    return is_open


def make_data():
    e_2018 = []
    e_2019 = []
    e_2020 = []

    data = ['2018']
    for y1 in e_2018:
        data.append(
            html.P(
                y1,
                className="card-text",
            )
        )
    data.append('2019')
    for y2 in e_2019:
        data.append(
            html.P(
                y2,
                className="card-text",
            )
        )
    data.append('2020')
    for y3 in e_2019:
        data.append(
            html.P(
                y3,
                className="card-text",
            )
        )


if __name__ == '__main__':
    make_data()
    app.run_server(debug=True)
