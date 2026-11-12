import xarray as xr
import glob

for archivo in glob.glob("*.nc"):
    try:
        ds = xr.open_dataset(archivo)
        print(f"[OK] {archivo} se lee perfectamente.")
        ds.close()
    except Exception as e:
        print(f"[X] {archivo} ha fallado: {e}")
