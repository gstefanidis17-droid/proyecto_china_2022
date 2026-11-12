import cdsapi

c = cdsapi.Client()

# 1. Climatología de superficie (1991-2020)
c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type': ['monthly_averaged_reanalysis'],
        'variable': ['2m_temperature', 'total_precipitation'],
        'year': [str(y) for y in range(1991, 2021)],
        'month': ['07', '08'],
        'time': ['00:00'],
        'data_format': 'netcdf',
        'download_format': 'unarchived',
        'area': [50, 80, 15, 140],
    },
    'era5_china_clim_surface_1991_2020.nc'
)

# 2. Climatología en altura a 500 hPa (1991-2020)
c.retrieve(
    'reanalysis-era5-pressure-levels-monthly-means',
    {
        'product_type': ['monthly_averaged_reanalysis'],
        'variable': ['geopotential'],
        'pressure_level': ['500'],
        'year': [str(y) for y in range(1991, 2021)],
        'month': ['07', '08'],
        'time': ['00:00'],
        'data_format': 'netcdf',
        'download_format': 'unarchived',
        'area': [50, 80, 15, 140],
    },
    'era5_china_clim_pressure_1991_2020.nc'
)
