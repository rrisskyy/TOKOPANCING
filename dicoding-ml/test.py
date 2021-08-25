import pandas as pd 


def describe_variables(ice_cream, price):

    # TODO: describe the categorical variable ice_cream
    ice_cream_stats = None
    
    # TODO: describe the numeric variable price
    price_stats = None

    return ice_cream_stats, price_stats
    
x = describe_variables(
    pd.Series(['mango', 'vanilla', 'chocolate', 'banana', 'banana', 'vanilla', 'strawberry', 'pistachio', 'mint_chocolate', 'pistachio']), 
    pd.Series([2.5, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 2.5, 3.0]))

print(pd.count(x))