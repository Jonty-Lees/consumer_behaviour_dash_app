#Dependencies
import dash;
from dash import dcc, html;
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc

# Initialisation

app = dash.Dash('', external_stylesheets=[dbc.themes.BOOTSTRAP])

product_df = pd.read_csv('data/product_df.csv')


# Setting Up Layout

app.layout=html.Div([
    
        dbc.Row(dbc.Col(
                html.H2("Consumer Behaviour App"), className='header'
        )),
           dbc.Row(dbc.Col(
                html.H5("Products and Product Categories"), className='header'
        )),
          dbc.Row(dbc.Col(
                html.Div([

                dcc.Dropdown(options=[
                        {'label': 'Product', 'value': 'product'},
                        {'label': 'Category', 'value': 'category'}
                    ],  
                    id='product-data-selector',
                    value=''
                )
                ]))),
          dbc.Row(dbc.Col(
                html.Div([

                dcc.Dropdown(options=[
                        {'label': 'London', 'value': 'London'},
                        {'label': 'Scotland', 'value': 'Scotland'},
                        {'label': 'Wales', 'value': 'Wales'}
                    ], 
                    id='region-selector',
                    value=''
                ),
                ]))),
        dbc.Row(
            [
                dcc.Graph(id='top_product_and_cat_graph'),    
                dbc.Col(html.Div([
                    dcc.Slider(
                        min=1,
                        max=5,
                        step=1,
                        marks={
                            1: '1',
                            2: '2',
                            3: '3',
                            4: '4',
                            5: '5'
                        },
                        value=5, id='top_product_slider'
                    )                
                    ])),
                dbc.Col(html.Div([
                    dcc.Graph(id='bottom_product_and_cat_graph'),      
                    html.H1([], id='slider-value'),
                    dcc.Slider(
                        min=1,
                        max=5,
                        step=1,
                        marks={
                            1: '1',
                            2: '2',
                            3: '3',
                            4: '4',
                            5: '5'
                        },
                        value=5, id='bottom_product_slider'
                    )              
                    ])),
            ]
        ),
])

#Callbacks
@app.callback(
    Output(component_id='top_product_and_cat_graph', component_property='figure'),
    Input(component_id='product-data-selector', component_property='value'),
    Input(component_id='region-selector', component_property='value'),
    Input(component_id='top_product_slider', component_property='value') 

)
def something(data_select, region_select, slider_select):
    print(f'this is region:{region_select}')
    print(f'this is data:{data_select}')

    if (data_select and region_select) is not None:
        regional_product_search = product_df.loc[product_df['region'] == region_select]
        top_product = regional_product_search.groupby(data_select)['quantity'].max().reset_index()
        print(top_product)
        top_product = top_product.nlargest(slider_select,'quantity')
        figure = px.bar(top_product,x=data_select, y= 'quantity')
        return figure
    return {}
# Run

app.run_server(debug=True)








