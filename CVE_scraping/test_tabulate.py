import pandas as pd
from tabulate import tabulate

dict_test = {
    'col1': [1, 2, 3, 4, 5],
    'col2': ['Apple', 'Banana', 'Watermelon', 'Grape', 'Melon'],
    'col3': ['a', 'b', 'c', 'd', 'e'],
}

df_test = pd.DataFrame(dict_test)
print(tabulate(df_test, headers='keys', tablefmt='fancy_grid', showindex=True))