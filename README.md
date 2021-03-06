# Consumer Behaviour Dash App

---

## Deployment

I deployed this app through Heroku with gunicorn and whitenoise, click below to view:

[Consumer Behaviour App](https://consumer-behaviour-dash-lees.herokuapp.com/)



---

## Introduction

This project is for a fictitious retail organization who wanted an interactive dashboard that took their raw data from branch and regional managers and converted it into an easily readable and visually attractive graphs. 
I will achieve this by cleaning and transforming the raw data through Python and exporting it to a dashboard for the client to interact with.
My priorities are to deliever a stable and bug-free dashboard that is visually up to the standard require. In order to not feature-creep, I will take a simplistic approach which will allow for additional features in later iterations.

Key points they need:
  - Ability to track the most purchased and least purchased products & product categories overall, per region and per city. Limited to top and bottom 5
  - Ability to track the best performing branches overall per region and per city, limited to top and bottom 10. Performance will be measure in both item quaitity sold and monetary value of sales made.

- Ability to track per hour sales for the top 10 branches identified

- Ability to identify the highest and lowest
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
- sync virtual enviroment
- run the dash app 


 
---

### Planning through Miro

In order to keep track of myy progress and make sure I was not feature creeping, I used Miro to organise the project into bitsize pieces as well as create a wire frame. 
I wanted to create an interface that was very simplistic and easy. 

You can view the page here: [Miro](https://miro.com/app/board/uXjVOdLqfzg=/?invite_link_id=520433487136)

![Dashboard WireFrame](https://user-images.githubusercontent.com/86611109/145681108-ffbaa307-566b-4416-b679-fcfabde2c61e.png)


---

## Development process and problem-solving strategy

My approach to to this project was to use bootstrap to create the layout.

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

For the most part, I found the routing of the the layout to the callbacks fairly simple to navigate. Understanding how Input, Output and State works felt easier when the routes are direct. When I needed to use a for loop it took a bit more trail and error but was totally do-able!

A good example was populating the dropdown menu with regions and counties without hardcoding. 

see below:

```
 dcc.Dropdown(options=[
                       {'label': y, 'value': y}
                        for y in sorted(branch_list_df.county.unique())
                    ], 
                    id='product-county-selector',
                    className= 'county-selector',
                    value="",
                    placeholder='Select County'
                ),

```

I put most of my effort and attnetion into getting the first graphs and options correct, from that point on it was far more about replicating what I had done, while changing the ouput code to create the right graphs.
I then was able to play around with the colouring the graphs. I did this right at the end so I could make sure the page flowed. i use the same colour shceme for all tops and bottoms and changed the line graph colour from a numerical value to the branch names so the client could track more easily. I reversed the colour directino with '_r' added to the end so hgihest numbers had a brighter colour
Top colours:
```
            color='quantity',
            color_continuous_scale=px.colors.sequential.Bluyl_r)
```
Bottom colours:
```
            color='quantity',
            color_continuous_scale=px.colors.sequential.matter_r)
```

---

## Future Iterations

- I would like to expand the graphs, I dont believe having only two graphs showed all the data in the best light. Potnetially for the Per Hour graph and the Profitability graph I would have like to have been able to have 4 graphs that include stacked bar graphs, But time and necessity did not permit that.

- I would like the sliders to be responsive to the graph shown, If time had permitted I would have used etl.limit to get the rows and equate it to the possible range. With more time, I would have done this.

- a loading bar incase loading took longer than expected. The dataframe files were very small so loading was very quick but would be important for future iterations

