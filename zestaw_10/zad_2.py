# Create pd.Series where 'index' contains days of the current month (numpy.datetime64 instances or pandas.DatetimeIndex)
# and 'data' contains some numbers (temperatures at noon, currency rates, ...).

import pandas as pd
import numpy as np

def get_month_bounds(date: pd.Timestamp = None):
    if date is None:
        date = pd.Timestamp.today()
    start = date.replace(day=1)
    end = start + pd.offsets.MonthEnd(1)
    return start, end


start_of_month, end_of_month = get_month_bounds()

days_of_curr_month = pd.date_range(start=start_of_month, end=end_of_month, freq='D')
temperatures = np.random.uniform(low=2, high=22, size=len(days_of_curr_month))

temperature_series = pd.Series(data=temperatures, index=days_of_curr_month, name='Temperature (°C)')

if __name__ == "__main__":
    print(temperature_series)
