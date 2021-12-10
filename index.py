#Dependencies
import dash;
from dash import dcc, html;
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc

# Initialisation

app = dash.Dash('', external_stylesheets=[dbc.themes.BOOTSTRAP])

product_df = pd.read_csv('data/product_df.csv')
performance_df = pd.read_csv('data/performance_df.csv')
per_hour_df = pd.read_csv('data/per_hour_df.csv')
profit_df = pd.read_csv('data/profitable_branches_df.csv')
branch_expenses_df = pd.read_csv('data/branch_expenses.csv')
branch_list_df = pd.read_csv('data/branch_list_df.csv')



# Setting Up Layout

app.layout=html.Div([
    #Title
        dbc.Row(dbc.Col(
                html.H1("Consumer Behaviour App"), className='header'

    # Product & Product Categories graph

        )),
           dbc.Row(dbc.Col(
                html.H4("Products and Product Categories Sales"), className='graph_header'
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

    # Performance graph
        dbc.Row(dbc.Col(
                html.H4("Branch Performance"), className='graph_header'
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
                        max=10,
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
                    dcc.Graph(id='lowest_performance_graph'),      
                    dcc.Slider(
                        min=1,
                        max=10,
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
                        value=5, id='lowest_performance_slider'
                    )              
                    ])),
            ], className='graph-container'
        ),
        html.Br(),
        html.Br(),

    # Per Hour Sales for top 10 branches per year
        dbc.Row(dbc.Col(
                html.H4("Per Hour Sales"), className='graph_header'
        )),
        dbc.Row(dbc.Col(
                html.Div([ 
                dbc.Row(
                        [  
                        dbc.Col(html.Div([
                            html.H6('Choose a year to load graph'),
                            dcc.Graph(id='top_per_hour_graph', className='line-graph'),
                            dcc.Slider(
                                min=24,
                                max=240,
                                step=12,
                                marks={
                                    24: '1',
                                    48: '2',
                                    72: '3',
                                    96: '4',
                                    120: '5',
                                    144: '6',
                                    168: '7',
                                    192: '8',
                                    216: '9',
                                    240: '10',
                                
                                },
                                value=120, id='top_per_hour_slider', className='per-hour-slider'
                            )                     
                            ])),
                    ], className='graph-container'
                )]))),
        dbc.Row(dbc.Col(
                html.Div([
                    html.H6('Year Selector', className="year_selector_h6"),
                    dcc.Slider(
                                min=2010,
                                max=2020,
                                step=1,
                                marks={
                                    2010: '2010',
                                    2011: '2011',
                                    2012: '2012',
                                    2013: '2013',
                                    2014: '2014',
                                    2015: '2015',
                                    2016: '2016',
                                    2017: '2017',
                                    2018: '2018',
                                    2019: '2019',
                                    2020: '2020',                         
                                },
                                value=0, id='per_hour_year_slider', className='per-hour-slider'),
                ])
        )),
        dbc.Row(dbc.Col(
                html.Div([ 
                dbc.Row(
                        [  
                        dbc.Col(html.Div([
                            dcc.Graph(id='lowest_per_hour_graph', className='line-graph'),      
                            dcc.Slider(
                                min=24,
                                max=240,
                                step=1,
                                marks={
                                    24: '1',
                                    48: '2',
                                    72: '3',
                                    96: '4',
                                    120: '5',
                                    144: '6',
                                    168: '7',
                                    192: '8',
                                    216: '9',
                                    240: '10',
                                
                                },
                                value=120, id='lowest_per_hour_slider', className='per-hour-slider'
                            )                   
                            ])),
                    ], className='graph-container'
                )]))),
                html.Br(),
                html.Br(),
   
    # Profitability by Branch
        dbc.Row(dbc.Col(
                html.H4("Branch Profitability"), className='graph_header'
        )),
        dbc.Row(dbc.Col(
                html.Div([ 
                dbc.Row(
                        [  
                        dbc.Col(html.Div([
                            html.H6('Choose a year to load graph', className='year_selector_h6' ),
                            dcc.Graph(id='top_profit_graph', className='line-graph'),
                            dcc.Slider(
                                min=1,
                                max=10,
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
                                    10: '10',
                                
                                },
                                value=10, id='top_profit_slider', className='profit-slider'
                            )                     
                            ])),
                    ], className='graph-container'
                )]))),
        dbc.Row(dbc.Col(
                html.Div([
                    html.H6('Year Selector', className="year_selector_h6"),
                    dcc.Slider(
                                min=2010,
                                max=2020,
                                step=1,
                                marks={
                                    2010: '2010',
                                    2011: '2011',
                                    2012: '2012',
                                    2013: '2013',
                                    2014: '2014',
                                    2015: '2015',
                                    2016: '2016',
                                    2017: '2017',
                                    2018: '2018',
                                    2019: '2019',
                                    2020: '2020',                         
                                },
                                value=0, id='profit_year_slider', className='profit-slider'),
                ])
        )),
        dbc.Row(dbc.Col(
                html.Div([ 
                dbc.Row(
                        [  
                        dbc.Col(html.Div([
                            dcc.Graph(id='lowest_profit_graph', className='line-graph'),      
                            dcc.Slider(
                                min=1,
                                max=10,
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
                                    10: '10',
                                
                                },
                                value=10, id='lowest_profit_slider', className='profit-slider'
                            )                   
                            ])),
                    ], className='graph-container'
                )]))),
        
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
        figure = px.bar(top_product,x=data_select, y= 'quantity', title=f'Most Purchased {data_select} In {county_select}')
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
        figure = px.bar(least_product,x=data_select, y= 'quantity', title=f'{region_select} Least Purchased {data_select}',color_discrete_sequence=["green"])
        return figure
    elif (data_select and county_select) is not None:
        regional_product_search = product_df.loc[product_df['county'] == county_select]
        least_product = regional_product_search.groupby(data_select)['quantity'].max().reset_index()
        least_product = least_product.nsmallest(slider_select,'quantity')
        figure = px.bar(least_product,x=data_select, y= 'quantity', title=f'Least Purchased {data_select} In {county_select}',color_discrete_sequence=["green"])
        return figure
    return {}

# Performance Callbacks

@app.callback(
    Output(component_id='top_performance_graph', component_property='figure'),
    Input(component_id='performance-region-selector', component_property='value'),
    Input(component_id='performance-county-selector', component_property='value'),
    Input(component_id='top_performance_slider', component_property='value') 
)
def top_performance_graph(region_select, county_select, slider_select):
    if region_select is not None:
        performance_df['best_performing'] = performance_df.quantity + performance_df.amount_in_gbp
        performance_df.sort_values(by='best_performing', ascending=False) 
        top_regional_performance = performance_df.loc[performance_df['region'] == region_select].nlargest(slider_select,'best_performing')
        figure = px.bar(top_regional_performance, x='branch_name', y='best_performing', title='Top Regional Branch Performance')
        return figure
    elif county_select is not None:
        performance_df['best_performing'] = performance_df.quantity + performance_df.amount_in_gbp
        performance_df.sort_values(by='best_performing', ascending=False) 
        top_county_performance = performance_df.loc[performance_df['county'] == county_select].nsmallest(slider_select,'best_performing')
        figure = px.bar(top_county_performance, x='branch_name', y='best_performing', title='Top County Branch Performance')
        return figure
    return {}

@app.callback(
    Output(component_id='lowest_performance_graph', component_property='figure'),
    Input(component_id='performance-region-selector', component_property='value'),
    Input(component_id='performance-county-selector', component_property='value'),
    Input(component_id='lowest_performance_slider', component_property='value') 
)
def worst_performance_graph(region_select, county_select, slider_select):
    if region_select is not None:
        performance_df['best_performing'] = performance_df.quantity + performance_df.amount_in_gbp
        performance_df.sort_values(by='best_performing', ascending=False) 
        lowest_regional_performance = performance_df.loc[performance_df['region'] == region_select].nsmallest(slider_select,'best_performing')
        figure = px.bar(lowest_regional_performance, x='branch_name', y='best_performing', title='Lowest Regional Branch Performance',color_discrete_sequence=["green"])
        return figure
    elif county_select is not None:
        performance_df['best_performing'] = performance_df.quantity + performance_df.amount_in_gbp
        performance_df.sort_values(by='best_performing', ascending=False) 
        lowest_county_performance = performance_df.loc[performance_df['county'] == county_select].nsmallest(slider_select,'best_performing')
        figure = px.bar(lowest_county_performance, x='branch_name', y='best_performing', title='Lowest County Branch Performance',color_discrete_sequence=["green"])
        return figure
    return {}

# Per Hour Callbacks

@app.callback(
    Output(component_id='top_per_hour_graph', component_property='figure'),
    Input(component_id='per_hour_year_slider', component_property='value'),
    Input(component_id='top_per_hour_slider', component_property='value') 
)
def top_performance_graph(year_select, branch_select):
    if (year_select >= 2010):
        year_filtered_df = per_hour_df.loc[per_hour_df['year']== year_select]
        year_filtered_df.sort_values(by=['branch_name', 'hour'])

        branch_hour_grouped_df = year_filtered_df.groupby(['branch_name', 'hour'])['amount_in_gbp'].sum().reset_index()

        top_branches = branch_hour_grouped_df.groupby('branch_name')['amount_in_gbp'].sum().reset_index()
        top_branches = top_branches.rename(columns={"amount_in_gbp":"total_gbp"})

        merged_per_hour = branch_hour_grouped_df.merge(top_branches.set_index('branch_name'), on='branch_name').reset_index()
        
        top_merged_per_hour = merged_per_hour.sort_values(['total_gbp', 'hour'], ascending=True)
        top_merged_per_hour = top_merged_per_hour.nlargest(branch_select, 'total_gbp')
        figure = px.line(top_merged_per_hour, 
        x='hour', 
        y='amount_in_gbp', 
        title=f'Top Branch Per Hour Sales For {year_select} ' ,
        line_group='branch_name',
        hover_name="branch_name",
        orientation="h",
        markers=True)
        return figure
    return {}

@app.callback(
    Output(component_id='lowest_per_hour_graph', component_property='figure'),
    Input(component_id='per_hour_year_slider', component_property='value'),
    Input(component_id='lowest_per_hour_slider', component_property='value') 
)
def top_performance_graph(year_select, branch_select):
    if (year_select >= 2010):
        year_filtered_df = per_hour_df.loc[per_hour_df['year']== year_select]
        year_filtered_df.sort_values(by=['branch_name', 'hour'])

        branch_hour_grouped_df = year_filtered_df.groupby(['branch_name', 'hour'])['amount_in_gbp'].sum().reset_index()

        top_branches = branch_hour_grouped_df.groupby('branch_name')['amount_in_gbp'].sum().reset_index()
        top_branches = top_branches.rename(columns={"amount_in_gbp":"total_gbp"})

        merged_per_hour = branch_hour_grouped_df.merge(top_branches.set_index('branch_name'), on='branch_name').reset_index()
        
        lowest_merged_per_hour = merged_per_hour.sort_values(['total_gbp', 'hour'], ascending=True)
        lowest_merged_per_hour = lowest_merged_per_hour.nsmallest(branch_select, 'total_gbp')
        figure = px.line(lowest_merged_per_hour, 
        x='hour', 
        y='amount_in_gbp', 
        title=f'Lowest Branch Per Hour Sales For {year_select} ',
        line_group='branch_name',
        hover_name="branch_name",
        orientation="h",
        markers=True,
        color_discrete_sequence=["green"])
        return figure
    return {}

    # 
 
#Profitability

@app.callback(
    Output(component_id='top_profit_graph', component_property='figure'),
    Input(component_id='profit_year_slider', component_property='value'),
    Input(component_id='top_profit_slider', component_property='value') 
)
def top_performance_graph(year_select, branch_select):
    if (year_select >= 2010):
        year_filtered_df = profit_df.loc[profit_df['year']== year_select]
        year_filtered_df.sort_values(by=['year','amount_in_gbp'],ascending=False)
        top_year_filtered_df = year_filtered_df.nlargest(10, 'amount_in_gbp')
        branch_expenses_df['total_expenses'] = branch_expenses_df.apply(lambda row: row.operational_cost + row.staff_bonuses + row.misc_expenses + row.waste_cost, axis=1)
        total_branch_expenses =branch_expenses_df.groupby('branch_name')['total_expenses'].sum().reset_index()
        branch_total_df = top_year_filtered_df.merge(total_branch_expenses.set_index('branch_name'), on='branch_name') 
        branch_total_df['profitability'] = branch_total_df.apply(lambda row: row.amount_in_gbp - row.total_expenses, axis=1)
        branch_total_df['profitability'] = branch_total_df.amount_in_gbp - branch_total_df.total_expenses
        branch_total_df.sort_values(by='profitability', ascending=False)
        branch_total_df.sort_values(by='profitability', ascending=False)
        top_profitability_stores = branch_total_df.nlargest(branch_select, 'profitability')
        figure = px.bar(top_profitability_stores, x='branch_name', y='profitability', title=f'Top Branch Profits in {year_select}' )


        return figure
    return {}

@app.callback(
    Output(component_id='lowest_profit_graph', component_property='figure'),
    Input(component_id='profit_year_slider', component_property='value'),
    Input(component_id='lowest_profit_slider', component_property='value') 
)
def top_performance_graph(year_select, branch_select):
    if (year_select >= 2010):
        year_filtered_df = profit_df.loc[profit_df['year']== year_select]
        year_filtered_df.sort_values(by=['year','amount_in_gbp'],ascending=False)
        top_year_filtered_df = year_filtered_df.nlargest(10, 'amount_in_gbp')
        branch_expenses_df['total_expenses'] = branch_expenses_df.apply(lambda row: row.operational_cost + row.staff_bonuses + row.misc_expenses + row.waste_cost, axis=1)
        total_branch_expenses =branch_expenses_df.groupby('branch_name')['total_expenses'].sum().reset_index()
        branch_total_df = top_year_filtered_df.merge(total_branch_expenses.set_index('branch_name'), on='branch_name') 
        branch_total_df['profitability'] = branch_total_df.apply(lambda row: row.amount_in_gbp - row.total_expenses, axis=1)
        branch_total_df['profitability'] = branch_total_df.amount_in_gbp - branch_total_df.total_expenses
        branch_total_df.sort_values(by='profitability', ascending=False)
        branch_total_df.sort_values(by='profitability', ascending=False)
        lowest_profitability_stores = branch_total_df.nsmallest(branch_select, 'profitability')
        # figure = px.bar(least_product,x=data_select, y= 'quantity', title=f'{county_select} Least Purchased {data_select}',color_discrete_sequence=["green"])

        figure = px.bar(lowest_profitability_stores, x='branch_name', y='profitability', title=f'Lowest Branch Profits in {year_select}' ,color_discrete_sequence=["green"])


        return figure
    return {}


# Run

app.run_server(debug=True)








