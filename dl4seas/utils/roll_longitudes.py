def roll_longitudes(dset): 
    """
    Roll the longitudes in a `xarray.Dataset` to go from -180 to 180 TO 0 to 360 

    Args: 

    dset (xarray.Dataset): The input dataset  

    Returns:

    dset (xarray.Dataset): The output dataset
    """

    import xarray as xr

    if not 'lon' in dset.coords:
        try: 
            dset = dset.rename({'longitude':'lon', 'latitude':'lat'}) 
            dset = dset.rename({'longitudes':'lon', 'latitudes':'lat'})
            dset = dset.rename({'long':'lon', 'latg':'lat'}) 
            dset = dset.rename({'lons':'lon', 'lats':'lat'}) 
        except: 
            pass 
    
    dset_out = dset.assign_coords(lon=(dset['lon'] % 360)).roll(lon=(dset.dims['lon'] // 2), roll_coords=True)

    return dset_out
