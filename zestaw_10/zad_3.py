# Create pd.DataFrame for the periodic table (ten elements).
# Column names are 'Name', 'Symbol', 'Weight'. 'index' starts from 1 for hydrogen.

import pandas as pd


def create_periodic_table_of_ten_elements():
    elements = [
        {'Name': 'Hydrogen', 'Symbol': 'H', 'Weight': 1.008},
        {'Name': 'Helium', 'Symbol': 'He', 'Weight': 4.0026},
        {'Name': 'Lithium', 'Symbol': 'Li', 'Weight': 6.94},
        {'Name': 'Beryllium', 'Symbol': 'Be', 'Weight': 9.0122},
        {'Name': 'Boron', 'Symbol': 'B', 'Weight': 10.81},
        {'Name': 'Carbon', 'Symbol': 'C', 'Weight': 12.011},
        {'Name': 'Nitrogen', 'Symbol': 'N', 'Weight': 14.007},
        {'Name': 'Oxygen', 'Symbol': 'O', 'Weight': 15.999},
        {'Name': 'Fluorine', 'Symbol': 'F', 'Weight': 18.998},
        {'Name': 'Neon', 'Symbol': 'Ne', 'Weight': 20.180},
    ]

    #Alternative way:
    # elements = {
    #     'Name': [
    #         'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron',
    #         'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'
    #     ],
    #     'Symbol': [
    #         'H', 'He', 'Li', 'Be', 'B',
    #         'C', 'N', 'O', 'F', 'Ne'
    #     ],
    #     'Weight': [
    #         1.008, 4.0026, 6.94, 9.0122, 10.81,
    #         12.011, 14.007, 15.999, 18.998, 20.180
    #     ]
    # }

    return pd.DataFrame(elements, index=range(1, len(elements) + 1))

if __name__ == "__main__":
    periodic_ten_elements_df = create_periodic_table_of_ten_elements()
    print(periodic_ten_elements_df)
