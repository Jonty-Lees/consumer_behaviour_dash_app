# Consumer Behaviour Dash App
<!-- 
In this project for a well know retail store, the client wanted an interactive dashboard that took their raw data from branch and reginon managers and convert it into a 
easily readable and pictoral format.
I would achieve this by using a cleaning and transformational python project, importing the outcome and building a dashboard for the client to interact with. 
creating something simple, easy to use and, whilst not the focus, easy on the eyes while using.

Key points they needed:
  - Ability to track the most purchased and least purchased products & product categories overall, per region and per city (limit to top 5 and least 5)
  - Ability to track the best performing branches overall per region and per city (performance is measured in both item quantity sold and monetary value of sales made, limit to best 10 and worst 10)
  - Ability to track per hour sales for the top 10 branches identified
  - Ability to identify the top 10 and bottom 10 profitable branches and indicate how profitable they are.  -->
---

## Technologies

1. Python
2. Dash
3. Pandas
4. Plotly Express
5. Dash Bootstrap
6. Flask
7. gunicorn
8. Heroku
9. GitHub
10. Miro
11. Jupyter Notebook
12. Matplotlib.pyplot
13. nbformatm


---

## Installation Instructions

To use this dashbord,
- Git Clone this repository
- CD into file
- create a vitual enviroment 
- Install dash, pandas, plotly, matplotlibs
- run the dash app 


 
---

### Planning through Miro

In order to keep track of progress and make sure I was on the right track, I used Miro to organise the project into bitsize pieces as well as create a wire frame. 
I wanted to create an interface that was very simplistic and easy. 

You can view the page here: [Miro](https://miro.com/app/board/uXjVOdLqfzg=/?invite_link_id=520433487136)


---

## Development process and problem-solving strategy

My approach to to this project was to use bootstrap to create the layout (as was under the impression that style was less important than data representation).

I wanted to give each graph multiple options so the user could interactivly change the graphs and where there were coloumn options, like region and county, I wanted the user to be able to see both, choose their column field which then would disable to possibility of selecting the other. I wanted to reduce any confusion by forcing the drop down menu to disable when the other is selected.

I had trouble with that code, the issues that I had to work out was that, when the page loaded, the drop down menu was never empty, the value when loaded was "". I had to figure out this was the case and then use and if statment inside an if statement for the callback function.

See below:

```
@app.callback(
    Output(component_id="performance-county-selector", component_property="disabled"),
    Output(component_id="performance-region-selector", component_property="disabled"),
    Input(component_id='performance-region-selector', component_property='value'),
    Input(component_id='performance-county-selector', component_property='value'),
)
def performance_disable_change(region, county):
    if region is not None:
        if region == "":
            return False, False
        else:
            return True, False
    elif county is not None:
        if county == "":
            return False, False
        else:
            return False, True
    return False, False

```



see below:

```
performance_df = branch_df[['region', 'county', 'branch_name', 'quantity','amount_in_gbp']]

regional_performance = performance_df.groupby(['region', 'county', 'branch_name'])[['quantity', 'amount_in_gbp']].sum().sort_values(by='region', ascending=False).reset_index()

regional_performance.to_csv('testing_output/performance_df.csv')

```

Once this became quicker and easier to work with, finding all the information needed to plot the graph became easier, then replicating the process meant in a much shorter time than before, i had grouped files that 
were workable and easy to use in the dash app.


