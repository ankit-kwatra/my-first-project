from datetime import datetime

def days_between_dates(date1: str, date2: str, date_format: str = "%Y-%m-%d") -> int:
    """
    Returns the absolute difference in days between two dates.
    Args:
        date1 (str): First date as a string.
        date2 (str): Second date as a string.
        date_format (str): Format of the input date strings (default: "%Y-%m-%d").
    Returns:
        int: Absolute difference in days.
    """
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days)
