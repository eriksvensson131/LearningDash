import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
subdf = df.iloc[100:120, :]

years = subdf.columns[100:-20]
long_df = pd.melt(subdf, id_vars='country', value_vars=years, var_name='year', value_name='gdp')

app.layout = html.Div([
    dcc.Graph(
        id='gdp-by-year',
        figure={
            'data': [
                dict(
                    x=long_df[long_df['country'] == i]['year'],
                    y=long_df[long_df['country'] == i]['gdp'],
                    mode='markers',
                    opacity=1.0,
                    marker={
                        'size': 3,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in long_df.country.unique()
            ],
            'layout': dict(
                xaxis={'title': 'year'},
                yaxis={'type': 'log', 'title': 'gdp'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)