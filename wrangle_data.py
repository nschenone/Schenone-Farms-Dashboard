import pandas as pd
import plotly.graph_objs as go


def get_df(path):
    # Read CSV
    df = pd.read_csv(path)

    # Set column datatypes
    df['Date'] =  pd.to_datetime(df['Date'])
    df['Field Tag'] =  pd.to_numeric(df['Field Tag'])
    df['Receiving Tag'] =  pd.to_numeric(df['Receiving Tag'])
    df['Lot'] =  pd.to_numeric(df['Lot'])
    df['Bins Received'] =  pd.to_numeric(df['Bins Received'])
    df['Bucket Price'] =  pd.to_numeric([i.strip()[1:] for i in df['Bucket Price']])
    df['Bucket Weight'] =  pd.to_numeric(df['Bucket Weight'])
    df['Price/Lb For Picker'] =  pd.to_numeric(df['Price/Lb For Picker'])
    df['Charge w 40%'] =  pd.to_numeric(df['Charge w 40%'])
    df['Weight (Dumped) By Field Tag'] =  pd.to_numeric([i.replace(",", "") for i in df['Weight (Dumped) By Field Tag']])
    df['Picking Charge'] =  pd.to_numeric([i.strip()[1:].replace(",", "") for i in df['Picking Charge']])
    df['Crew Cost (Per Lb)'] =  pd.to_numeric([i.strip()[1:] for i in df['Crew Cost (Per Lb)']])
    df['Crew Cost (Subtotal)'] =  pd.to_numeric([i.strip()[1:] for i in df['Crew Cost (Subtotal)']])
    
    return df



def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    df = get_df("myapp/data/Sample.csv")
    
    df_query = df[df["Variety"] == "Coral"]
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = df_query['Date'],
      y = df_query["Crew Cost (Subtotal)"],
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Crew Cost Over Time (Coral)',
                xaxis = dict(title = 'Date'),
                yaxis = dict(title = 'Crew Cost (Subtotal)'),
    )
  
    graph_two = []

    graph_two.append(
      go.Bar(
      x = ['a', 'b', 'c', 'd', 'e'],
      y = [12, 9, 7, 5, 1],
      )
    )

    layout_two = dict(title = 'Chart Two',
                xaxis = dict(title = 'x-axis label',),
                yaxis = dict(title = 'y-axis label'),
                )


    graph_three = []
    graph_three.append(
      go.Scatter(
      x = [5, 4, 3, 2, 1, 0],
      y = [0, 2, 4, 6, 8, 10],
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Chart Three',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label')
                       )

    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = [20, 40, 60, 80],
      y = [10, 20, 30, 40],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Chart Four',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
