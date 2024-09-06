# ECMWF Client
client = Client(source="ecmwf")

# Definovanie krokov (forecast steps) a parametrov na stiahnutie (teplota a zrážky)
steps = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 
         42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 
         72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 
         102, 105, 108, 111, 114, 117, 120, 123, 
         126, 129, 132]  # Forecast kroky v hodinách

# Stiahnutie celého GRIB súboru
client.retrieve(
    stream="oper",
    type="fc",
    step=steps,  # Forecast kroky
    param="2t/tp",  # 2m teplota a celkové zrážky
    target="full_data.grib2",  # Uloženie GRIB súboru
)

# Získanie aktuálneho času
download_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Výpis času stiahnutia
print(f"Full GRIB file downloaded successfully at {download_time}.")