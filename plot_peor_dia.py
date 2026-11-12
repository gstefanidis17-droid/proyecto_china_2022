import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd

# 1. Abrir el archivo de presión
ds = xr.open_dataset('era5_china_pressure_2022_JA.nc')

# 2. Seleccionar Z a 500 hPa y convertir a metros (gpm)
z500 = ds['z'].sel(pressure_level=500) / 9.80665

# 3. Definir la caja geográfica de Sichuan y Chongqing (aprox. 28°N-32°N, 103°E-110°E)
sichuan_box = z500.where((z500.latitude >= 28) & (z500.latitude <= 32) & 
                         (z500.longitude >= 103) & (z500.longitude <= 110), drop=True)

# 4. Encontrar el momento exacto con el geopotencial medio más alto en esa región
box_mean = sichuan_box.mean(dim=['latitude', 'longitude'])
peak_time = box_mean.idxmax(dim='valid_time')
print(f"¡El pico máximo de bloqueo se registró el: {pd.to_datetime(peak_time.values).strftime('%Y-%m-%d %H:%M')}!")

# 5. Extraer el mapa completo para ese día/hora pico
z500_peak = z500.sel(valid_time=peak_time)

# 6. Generar el mapa profesional con Cartopy
fig, ax = plt.subplots(figsize=(11, 7), subplot_kw={'projection': ccrs.PlateCarree()})

contour = z500_peak.plot.contourf(
    ax=ax, 
    transform=ccrs.PlateCarree(), 
    cmap='jet', 
    levels=15,
    cbar_kwargs={'label': 'Altura Geopotencial a 500 hPa (gpm)', 'shrink': 0.8}
)

ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.8)
ax.add_feature(cfeature.STATES, linestyle=':', edgecolor='gray', linewidth=0.5)

ax.plot(106.5, 29.5, marker='*', color='red', markersize=14, transform=ccrs.PlateCarree(), label='Sichuan / Chongqing (Epicentro)')

fecha_str = pd.to_datetime(peak_time.values).strftime('%d de %B de %Y')
ax.set_title(f'Pico de Bloqueo Sinóptico Z500 - {fecha_str}', fontsize=12, pad=15)
ax.legend(loc='lower left')

gl = ax.gridlines(draw_labels=True, linestyle='--', alpha=0.5)
gl.top_labels = False
gl.right_labels = False

plt.savefig('mapa_peor_dia_bloqueo.png', dpi=300, bbox_inches='tight')
print("¡Mapa del peor día guardado como 'mapa_peor_dia_bloqueo.png'!")
plt.show()
