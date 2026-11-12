import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# 1. Abrir el archivo de presión
ds = xr.open_dataset('era5_china_pressure_2022_JA.nc')

# 2. Seleccionar Z a 500 hPa y convertir a metros (gpm)
z500 = ds['z'].sel(pressure_level=500) / 9.80665
z500_media = z500.mean(dim='valid_time')

# 3. Configurar la figura con proyección geográfica (PlateCarree)
fig, ax = plt.subplots(figsize=(11, 7), subplot_kw={'projection': ccrs.PlateCarree()})

# 4. Pintar el campo de Z500 con transparencia para ver el fondo
contour = z500_media.plot.contourf(
    ax=ax, 
    transform=ccrs.PlateCarree(), 
    cmap='jet', 
    levels=15,
    cbar_kwargs={'label': 'Altura Geopotencial a 500 hPa (gpm)', 'shrink': 0.8}
)

# 5. Añadir capas geográficas de Cartopy
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.8)
ax.add_feature(cfeature.STATES, linestyle=':', edgecolor='gray', linewidth=0.5) # Límites provinciales

# 6. Marcar el epicentro de la ola de calor (Sichuan / Chongqing aprox. 30°N, 105°E)
ax.plot(106.5, 29.5, marker='*', color='red', markersize=12, transform=ccrs.PlateCarree(), label='Sichuan / Chongqing')

# Añadir rejilla de coordenadas (latitud/longitud)
gl = ax.gridlines(draw_labels=True, linestyle='--', alpha=0.5)
gl.top_labels = False
gl.right_labels = False

ax.set_title('Bloqueo Sinóptico Z500 y Cuenca de Sichuan (Verano 2022)', fontsize=12, pad=15)
ax.legend(loc='lower left')

plt.savefig('mapa_bloqueo_china_con_fronteras.png', dpi=300, bbox_inches='tight')
print("¡Mapa profesional guardado como 'mapa_bloqueo_china_con_fronteras.png'!")
plt.show()
