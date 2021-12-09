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
branch_list_df = pd.read_csv('data/branch_list_df.csv')



# Setting Up Layout

app.layout=html.Div([

    # Product & Product Categories graph
        dbc.Row(dbc.Col(
                html.H2("Consumer Behaviour App"), className='header'
        )),
           dbc.Row(dbc.Col(
                html.H5("Products and Product Categories Sales"), className='graph_header'
        )),
          dbc.Row(dbc.Col(
                html.Div([ 
                dcc.Dropdown(options=[
                        {'label': 'Product', 'value': 'product'},
                        {'label': 'Product Category', 'value': 'category'}
                    ],  
                    id='product-data-selector',
                    value='',
                    placeholder='Select Data'
                )
                ]))),
          dbc.Row(dbc.Col(
                html.Div([
                dcc.Dropdown(options=[
                       {'label': x, 'value': x}
                        for x in sorted(branch_list_df.region.unique())
                    ], 
                    id='product-region-selector',
                    className='region-selector',
                    value='',
                    disabled= False,
                    placeholder='Select Region'
                ),
                dcc.Dropdown(options=[
                       {'label': y, 'value': y}
                        for y in sorted(branch_list_df.county.unique())
                    ], 
                    id='product-county-selector',
                    className= 'county-selector',
                    value="",
                    disabled = False,
                    placeholder='Select County'
                ),
                ]))),
        dbc.Row(
            [  
                dbc.Col(html.Div([
                    dcc.Graph(id='top_product_and_cat_graph'),
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
            ], className='graph-container'
        ),
        html.Br(),
        html.Br(),

    # Product & Product Categories graph
        dbc.Row(dbc.Col(
                html.H5("Branch Performance"), className='graph_header'
        )),
        dbc.Row(dbc.Col(
                html.Div([ 
          dbc.Row(dbc.Col(
                html.Div([
                dcc.Dropdown(options=[
                       {'label': x, 'value': x}
                        for x in sorted(branch_list_df.region.unique())
                    ], 
                    id='performance-region-selector',
                    className='region-selector',
                    value='',
                    disabled= False,
                    placeholder='Select Region'
                ),
                dcc.Dropdown(options=[
                       {'label': y, 'value': y}
                        for y in sorted(branch_list_df.county.unique())
                    ], 
                    id='performance-county-selector',
                    className='county-selector',
                    value="",
                    disabled = False,
                    placeholder='Select County'
                ),
                ])))]))),
        dbc.Row(
            [  
                dbc.Col(html.Div([
                    dcc.Graph(id='top_performance_graph'),
                    dcc.Slider(
                        min=1,
                        max=5,
                        step=1,
                        marks={
                            1: '1',
                            2: '2',
                            3: '3',
                            4: '4',
                            5: '5',
                            6: '6',
                            7: '7',
                            8: '8',
                            9: '9',
                            10:'10'
                        },
                        value=5, id='top_performance_slider'
                    )                
                    ])),
                dbc.Col(html.Div([
                    dcc.Graph(id='worst_performance_graph'),      
                    dcc.Slider(
                        min=1,
                        max=5,
                        step=1,
                        marks={
                            1: '1',
                            2: '2',
                            3: '3',
                            4: '4',
                            5: '5',
                            6: '6',
                            7: '7',
                            8: '8',
                            9: '9',
                            10:'10'
                        },
                        value=5, id='bottom_performance_slider'
                    )              
                    ])),
            ], className='graph-container'
        ),
        html.Br(),
        html.Br(),
])

# Callbacks

    # Products Callbacks

@app.callback(
    Output(component_id='top_product_and_cat_graph', component_property='figure'),
    Input(component_id='product-data-selector', component_property='value'),
    Input(component_id='product-region-selector', component_property='value'),
    Input(component_id='product-county-selector', component_property='value'),
    Input(component_id='top_product_slider', component_property='value') 
)
def top_product_graph(data_select, region_select, county_select, slider_select):
    if (data_select and region_select) is not None:
        regional_product_search = product_df.loc[product_df['region'] == region_select]
        top_product = regional_product_search.groupby(data_select)['quantity'].max().reset_index()
        top_product = top_product.nlargest(slider_select,'quantity')
        figure = px.bar(top_product,x=data_select, y= 'quantity', title=f'{region_select} Most Purchased {data_select}')
        return figure
    elif (data_select and county_select) is not None:
        regional_product_search = product_df.loc[product_df['county'] == county_select]
        top_product = regional_product_search.groupby(data_select)['quantity'].max().reset_index()
        top_product = top_product.nlargest(slider_select,'quantity')
        figure = px.bar(top_product,x=data_select, y= 'quantity', title=f'{county_select} Most Purchased {data_select}')
        return figure
    return {}

@app.callback(
    Output(component_id='bottom_product_and_cat_graph', component_property='figure'),
    Input(component_id='product-data-selector', component_property='value'),
    Input(component_id='product-region-selector', component_property='value'),
    Input(component_id='product-county-selector', component_property='value'),
    Input(component_id='bottom_product_slider', component_property='value') 
)
def least_product_graph(data_select, region_select, county_select, slider_select):
    if (data_select and region_select) is not None:
        regional_product_search = product_df.loc[product_df['region'] == region_select]
        least_product = regional_product_search.groupby(data_select)['quantity'].max().reset_index()
        least_product = least_product.nsmallest(slider_select,'quantity')
        figure = px.bar(least_product,x=data_select, y= 'quantity', title=f'{region_select} Least Purchased {data_select}')
        return figure
    elif (data_select and county_select) is not None:
        regional_product_search = product_df.loc[product_df['county'] == county_select]
        least_product = regional_product_search.groupby(data_select)['quantity'].max().reset_index()
        least_product = least_product.nsmallest(slider_select,'quantity')
        figure = px.bar(least_product,x=data_select, y= 'quantity', title=f'{county_select} Least Purchased {data_select}')
        return figure
    return {}

# Performance Callbacks


# Run

app.run_server(debug=True)








