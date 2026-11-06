# This is my first project in my software engineering study plan.
#
# This is a CLI calculator converter built with Python.
# It converts the following: Mass, Temperature, Area, Length,
# Volume, Time, Speed.

def calculator_converter() -> any:
    # Type of conversion
    conversion_type = input("Enter the type of conversion (Mass(m), Temperature(temp), Area(a), Length(l), Volume(v), Time(t), Speed(s)): ")
    
    if conversion_type == "m":
        mass_conversion_logic()
    elif conversion_type == "temp":
        temperature_conversion_logic()
    elif conversion_type == "a":
        area_conversion_logic()
    elif conversion_type == "l":
        length_conversion_logic()
    elif conversion_type == "v":
        volume_conversion_logic()
    elif conversion_type == "t":
        time_conversion_logic()
    elif conversion_type == "s":
        speed_conversion_logic()
    else:
        print("Invalid conversion type entered.")


def mass_conversion_logic() -> any:
    # Mass conversion logic
    mass_value = float(input("Enter the mass value: "))
    mass_unit = input("Enter the mass unit (kg, g, lb): ")
    
    if mass_unit == "kg":
        converted_value_to_grams = mass_value * 1000  # Convert kg to g
        converted_value_to_pounds = mass_value * 2.20462  # Convert kg to lb
        print(f"{mass_value} kg is equal to {converted_value_to_grams}g")
        print(f"{mass_value} kg is equal to {converted_value_to_pounds}lb")
    elif mass_unit == "g":
        converted_value_to_kg = mass_value / 1000  # Convert g to kg
        converted_value_to_pounds = mass_value * 0.00220462  # Convert g to lb
        print(f"{mass_value} g is equal to {converted_value_to_kg}kg")
        print(f"{mass_value} g is equal to {converted_value_to_pounds}lb")
    elif mass_unit == "lb":
        converted_value_to_kg = mass_value * 0.453592  # Convert lb to kg
        converted_value_to_grams = mass_value * 453.592  # Convert lb to g
        print(f"{mass_value} lb is equal to {converted_value_to_kg}kg")
        print(f"{mass_value} lb is equal to {converted_value_to_grams}g")
    else:
        print("Invalid mass unit entered.")
        

def temperature_conversion_logic() -> any:
    # Temperature conversion logic
    temp_value = float(input("Enter the temperature value: "))
    temp_unit = input("Enter the temperature unit (C, F, K): ")

    if temp_unit == "C":
        converted_value_to_F = (temp_value * 9/5) + 32  # Convert Celsius to Fahrenheit
        converted_value_to_K = temp_value + 273.15  # Convert Celsius to Kelvin
        print(f"{temp_value}°C is equal to {converted_value_to_F}°F")
        print(f"{temp_value}°C is equal to {converted_value_to_K}K")
    elif temp_unit == "F":
        converted_value_to_C = (temp_value - 32) * 5/9  # Convert Fahrenheit to Celsius
        converted_value_to_K = (temp_value - 32) * 5/9 + 273.15  # Convert Fahrenheit to Kelvin
        print(f"{temp_value}°F is equal to {converted_value_to_C}°C")
        print(f"{temp_value}°F is equal to {converted_value_to_K}K")
    elif temp_unit == "K":
        converted_value_to_C = temp_value - 273.15  # Convert Kelvin to Celsius
        converted_value_to_F = (temp_value - 273.15) * 9/5 + 32  # Convert Kelvin to Fahrenheit
        print(f"{temp_value}K is equal to {converted_value_to_C}°C")
        print(f"{temp_value}K is equal to {converted_value_to_F}°F")
    else:
        print("Invalid temperature unit entered.")

def area_conversion_logic() -> any:
    # This Area conversion logic converts between Hectare(ha), acre, Square Kilometer(km2), Square Meter(m2), Square Mile(mi2)
    area_value = float(input("Enter the area value: "))
    area_unit = input("Enter the area unit (Hectare(ha), acre, Square Kilometer(km2), Square Meter(m2), Square Mile(mi2)): ")

    if area_unit == "ha":
        converted_value_to_acre = area_value * 10000  # Convert ha to acre
        converted_value_to_km2 = area_value * 107639  # Convert ha to km²
        converted_value_to_m2 = area_value * 10000  # Convert ha to m²
        converted_value_to_mi2 = area_value * 0.00386102  # Convert ha to mi²
        
        print(f"{area_value} ha is equal to {converted_value_to_acre} acre")
        print(f"{area_value} ha is equal to {converted_value_to_km2} km²")
        print(f"{area_value} ha is equal to {converted_value_to_mi2} mi²")
        print(f"{area_value} ha is equal to {converted_value_to_m2} m²")
    elif area_unit == "acre":
        converted_value_to_ha = area_value / 10000  # Convert acre to ha
        converted_value_to_km2 = area_value * 0.00107639  # Convert acre to km²
        converted_value_to_m2 = area_value * 4046.86  # Convert acre to m²
        converted_value_to_mi2 = area_value * 0.000001  # Convert acre to mi²
        
        print(f"{area_value} acre is equal to {converted_value_to_ha} ha")
        print(f"{area_value} acre is equal to {converted_value_to_km2} km²")
        print(f"{area_value} acre is equal to {converted_value_to_m2} m²")
        print(f"{area_value} acre is equal to {converted_value_to_mi2} mi²")
    elif area_unit == "km2":
        converted_value_to_ha = area_value * 0.092903  # Convert km² to ha
        converted_value_to_acre = area_value * 929.03  # Convert km² to acre
        converted_value_to_m2 = area_value * 1000000  # Convert km² to m²
        converted_value_to_mi2 = area_value * 0.386102  # Convert km² to mi²
        
        print(f"{area_value} km² is equal to {converted_value_to_ha} ha")
        print(f"{area_value} km² is equal to {converted_value_to_acre} acre")
        print(f"{area_value} km² is equal to {converted_value_to_m2} m²")
        print(f"{area_value} km² is equal to {converted_value_to_mi2} mi²")
    elif area_unit == "m2":
        converted_value_to_ha = area_value * 0.0001  # Convert m² to ha
        converted_value_to_acre = area_value * 0.000247105  # Convert m² to acre
        converted_value_to_km2 = area_value * 0.000001  # Convert m² to km²
        converted_value_to_mi2 = area_value * 0.000000386102  # Convert m² to mi²
        
        print(f"{area_value} m² is equal to {converted_value_to_ha} ha")
        print(f"{area_value} m² is equal to {converted_value_to_acre} acre")
        print(f"{area_value} m² is equal to {converted_value_to_km2} km²")
        print(f"{area_value} m² is equal to {converted_value_to_mi2} mi²")
    elif area_unit == "mi2":
        converted_value_to_ha = area_value * 258.999  # Convert mi² to ha
        converted_value_to_acre = area_value * 640  # Convert mi² to acre
        converted_value_to_km2 = area_value * 2.58999  # Convert mi² to km²
        converted_value_to_m2 = area_value * 2589988.11  # Convert mi² to m²
        
        print(f"{area_value} mi² is equal to {converted_value_to_ha} ha")
        print(f"{area_value} mi² is equal to {converted_value_to_acre} acre")
        print(f"{area_value} mi² is equal to {converted_value_to_km2} km²")
        print(f"{area_value} mi² is equal to {converted_value_to_m2} m²")
    else:
        print("Invalid area unit entered.")

def length_conversion_logic() -> any:
    # Length conversion logic
    length_value = float(input("Enter the length value: "))
    length_unit = input("Enter the length unit (m, km, in, ft, yd, mi): ")

    if length_unit == "m":
        converted_value_to_km = length_value / 1000  # Convert m to km
        converted_value_to_in = length_value * 39.3701  # Convert m to in
        converted_value_to_ft = length_value * 3.28084  # Convert m to ft
        converted_value_to_yd = length_value * 1.09361  # Convert m to yd
        converted_value_to_mi = length_value * 0.000621371  # Convert m to mi
        
        print(f"{length_value} m is equal to {converted_value_to_km} km")
        print(f"{length_value} m is equal to {converted_value_to_in} in")
        print(f"{length_value} m is equal to {converted_value_to_ft} ft")
        print(f"{length_value} m is equal to {converted_value_to_yd} yd")
        print(f"{length_value} m is equal to {converted_value_to_mi} mi")
    elif length_unit == "km":
        converted_value_to_m = length_value * 1000  # Convert km to m
        converted_value_to_in = length_value * 39370.1  # Convert km to in
        converted_value_to_ft = length_value * 3280.84  # Convert km to ft
        converted_value_to_yd = length_value * 1093.61  # Convert km to yd
        converted_value_to_mi = length_value * 0.621371  # Convert km to mi
        
        print(f"{length_value} km is equal to {converted_value_to_m} m")
        print(f"{length_value} km is equal to {converted_value_to_in} in")
        print(f"{length_value} km is equal to {converted_value_to_ft} ft")
        print(f"{length_value} km is equal to {converted_value_to_yd} yd")
        print(f"{length_value} km is equal to {converted_value_to_mi} mi")
    elif length_unit == "in":
        converted_value_to_m = length_value * 0.0254  # Convert in to m
        converted_value_to_km = length_value * 0.0000254  # Convert in to km
        converted_value_to_ft = length_value * 0.0833333  # Convert in to ft
        converted_value_to_yd = length_value * 0.0277778  # Convert in to yd
        converted_value_to_mi = length_value * 0.0000157828  # Convert in to mi
        
        print(f"{length_value} in is equal to {converted_value_to_m} m")
        print(f"{length_value} in is equal to {converted_value_to_km} km")
        print(f"{length_value} in is equal to {converted_value_to_ft} ft")
        print(f"{length_value} in is equal to {converted_value_to_yd} yd")
        print(f"{length_value} in is equal to {converted_value_to_mi} mi")
    elif length_unit == "ft":
        converted_value_to_m = length_value * 0.3048  # Convert ft to m
        converted_value_to_km = length_value * 0.0003048  # Convert ft to km
        converted_value_to_in = length_value * 12  # Convert ft to in
        converted_value_to_yd = length_value * 0.333333  # Convert ft to yd
        converted_value_to_mi = length_value * 0.000189394  # Convert ft to mi
        
        print(f"{length_value} ft is equal to {converted_value_to_m} m")
        print(f"{length_value} ft is equal to {converted_value_to_km} km")
        print(f"{length_value} ft is equal to {converted_value_to_in} in")
        print(f"{length_value} ft is equal to {converted_value_to_yd} yd")
        print(f"{length_value} ft is equal to {converted_value_to_mi} mi")
    elif length_unit == "yd":
        converted_value_to_m = length_value * 0.9144  # Convert yd to m
        converted_value_to_km = length_value * 0.0009144  # Convert yd to km
        converted_value_to_in = length_value * 36  # Convert yd to in
        converted_value_to_ft = length_value * 3  # Convert yd to ft
        converted_value_to_mi = length_value * 0.000568182  # Convert yd to mi
        
        print(f"{length_value} yd is equal to {converted_value_to_m} m")
        print(f"{length_value} yd is equal to {converted_value_to_km} km")
        print(f"{length_value} yd is equal to {converted_value_to_in} in")
        print(f"{length_value} yd is equal to {converted_value_to_ft} ft")
        print(f"{length_value} yd is equal to {converted_value_to_mi} mi")
    elif length_unit == "mi":
        converted_value_to_m = length_value * 1609.34  # Convert mi to m
        converted_value_to_km = length_value * 1.60934  # Convert mi to km
        converted_value_to_in = length_value * 63360  # Convert mi to in
        converted_value_to_ft = length_value * 5280  # Convert mi to ft
        converted_value_to_yd = length_value * 1760  # Convert mi to yd
        
        print(f"{length_value} mi is equal to {converted_value_to_m} m")
        print(f"{length_value} mi is equal to {converted_value_to_km} km")
        print(f"{length_value} mi is equal to {converted_value_to_in} in")
        print(f"{length_value} mi is equal to {converted_value_to_ft} ft")
        print(f"{length_value} mi is equal to {converted_value_to_yd} yd")
    else:
        print("Invalid length unit entered.")

def volume_conversion_logic() -> any:
    # Volume conversion logic
    volume_value = float(input("Enter the volume value: "))
    volume_unit = input("Enter the volume unit (L, gal): ")
    
    if volume_unit == "L":
        converted_value_to_gal = volume_value * 0.264172  # Convert L to gal
        
        print(f"{volume_value} L is equal to {converted_value_to_gal} gal")
    elif volume_unit == "gal":
        converted_value_to_L = volume_value * 3.78541  # Convert gal to L
        
        print(f"{volume_value} gal is equal to {converted_value_to_L} L")
    else:
        print("Invalid volume unit entered.")
        
def time_conversion_logic() -> any:
    # Time conversion logic
    time_value = float(input("Enter the time value: "))
    time_unit = input("Enter the time unit (s, min, h): ")
    
    if time_unit == "s":
        converted_value_to_min = time_value / 60  # Convert s to min
        converted_value_to_h = time_value / 3600  # Convert s to h
        
        print(f"{time_value} s is equal to {converted_value_to_min} min")
        print(f"{time_value} s is equal to {converted_value_to_h} h")
    elif time_unit == "min":
        converted_value_to_s = time_value * 60  # Convert min to s
        converted_value_to_h = time_value / 60  # Convert min to h
        
        print(f"{time_value} min is equal to {converted_value_to_s} s")
        print(f"{time_value} min is equal to {round(converted_value_to_h), 2} h")
    elif time_unit == "h":
        converted_value_to_s = time_value * 3600  # Convert h to s
        converted_value_to_min = time_value * 60  # Convert h to min
        
        print(f"{time_value} h is equal to {converted_value_to_s} s")
        print(f"{time_value} h is equal to {converted_value_to_min} min")
    else:
        print("Invalid time unit entered.")

def speed_conversion_logic() -> any:
    # Speed conversion logic
    speed_value = float(input("Enter the speed value: "))
    speed_unit = input("Enter the speed unit (m/s, km/h, mph, knot): ")
    
    if speed_unit == "m/s":
        converted_value_to_kmh = speed_value * 3.6  # Convert m/s to km/h
        converted_value_to_mph = speed_value * 2.23694  # Convert m/s to mph
        converted_value_to_knot = speed_value * 1.94384  # Convert m/s to knot
        
        print(f"{speed_value} m/s is equal to {converted_value_to_kmh} km/h")
        print(f"{speed_value} m/s is equal to {converted_value_to_mph} mph")
        print(f"{speed_value} m/s is equal to {converted_value_to_knot} knot")
    elif speed_unit == "km/h":
        converted_value_to_ms = speed_value / 3.6  # Convert km/h to m/s
        converted_value_to_mph = speed_value * 0.621371  # Convert km/h to mph
        converted_value_to_knot = speed_value * 0.539957  # Convert km/h to knot

        print(f"{speed_value} km/h is equal to {converted_value_to_ms} m/s")
        print(f"{speed_value} km/h is equal to {converted_value_to_mph} mph")
        print(f"{speed_value} km/h is equal to {converted_value_to_knot} knot")
    elif speed_unit == "mph":
        converted_value_to_ms = speed_value * 0.44704  # Convert mph to m/s
        converted_value_to_kmh = speed_value * 1.60934  # Convert mph to km/h
        converted_value_to_knot = speed_value * 0.868976  # Convert mph to knot
        
        print(f"{speed_value} mph is equal to {converted_value_to_ms} m/s")
        print(f"{speed_value} mph is equal to {converted_value_to_kmh} km/h")
        print(f"{speed_value} mph is equal to {converted_value_to_knot} knot")
    elif speed_unit == "knot":
        converted_value_to_ms = speed_value * 0.514444  # Convert knot to m/s
        converted_value_to_kmh = speed_value * 1.852  # Convert knot to km/h
        converted_value_to_mph = speed_value * 1.15078  # Convert knot to mph

        print(f"{speed_value} knot is equal to {converted_value_to_ms} m/s")
        print(f"{speed_value} knot is equal to {converted_value_to_kmh} km/h")
        print(f"{speed_value} knot is equal to {converted_value_to_mph} mph")
    else:
        print("Invalid speed unit entered.")

calculator_converter()
