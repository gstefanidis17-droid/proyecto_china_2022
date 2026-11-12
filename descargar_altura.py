import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': ['reanalysis'],
        'variable': [
            'geopotential',
            'u_component_of_wind',
            'v_component_of_wind',
            'vertical_velocity',
        ],
        'pressure_level': ['500', '850'],
        'year': ['2022'],
        'month': ['07', '08'],
        'day': [f"{d:02d}" for d in range(1, 32)],
        'time': ['00:00', '06:00', '12:00', '18:00'],
        'data_format': 'netcdf',
        'download_format': 'unarchived',
        'area': [50, 80, 15, 140],
    },
    'era5_china_pressure_2022_JA.nc'
)
