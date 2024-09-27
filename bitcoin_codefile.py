def get_season(month):
    """Define a function to map months to seasons"""
    import pandas as pd
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'

def day_name(day_of_week):
    """Categorizing weekends and weekdays"""
    import pandas as pd
    if day_of_week >= 5:
        return "Weekend"
    else:
        return  "Weekday"