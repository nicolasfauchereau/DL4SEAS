def shift_time(time, shift='Month End'):
    """
    shift_time shift a time index to the beginning of the end of the month

    [extended_summary]

    Parameters
    ----------
    time : DatetimeIndex or compatible object
        The index to shift 
    shift : str, optional
        can be 'Month End' or 'Month Begin', by default 'Month End'

    Returns
    -------
    time
        the shifted datetime index 

    Example
    -------

    >> dates = pd.date_range(start='1990-01-01', periods=5, freq='MS')
    
    >> dates

    DatetimeIndex(['1990-01-01', '1990-02-01', '1990-03-01', '1990-04-01',
               '1990-05-01'],
              dtype='datetime64[ns]', freq='MS')

    >> shift_time(dates, 'Month End') 

    DatetimeIndex(['1990-01-31', '1990-02-28', '1990-03-31', '1990-04-30',
               '1990-05-31'],
              dtype='datetime64[ns]', freq=None)



    """

    import pandas as pd

    if shift == 'Month End':
        time = time + pd.offsets.MonthEnd(0)
    elif shift == 'Month Begin': 
        time = time + pd.offsets.MonthBegin(-1)
    return time 