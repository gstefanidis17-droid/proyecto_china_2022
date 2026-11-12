import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': ['reanalysis'],
        'variable': [
            '2m_temperature',
            'total_precipitation',
            'surface_solar_radiation_downwards',
        ],
        'year': ['2022'],
        'month': ['07', '08'],
        'day': [f"{d:02d}" for d in range(1, 32)],
        'time': [f"{h:02d}:00" for h in range(24)],
        'data_format': 'netcdf',
        'download_format': 'unarchived',
        'area': [50, 80, 15, 140],
    },
    'era5_china_surface_2022_JA.nc'
)
