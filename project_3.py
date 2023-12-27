# Conversion functions
def convert_length(value, from_unit, to_unit):
    units = {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "ft": 0.3048, "in": 0.0254, "yd": 0.9144}
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {"kg": 1, "g": 0.001, "mg": 0.000001, "lb": 0.453592, "oz": 0.0283495}
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        if to_unit == "F":
            return value * 9/5 + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32

def convert_time(value, from_unit, to_unit):
    units = {"s": 1, "ms": 0.001, "us": 0.000001, "min": 60, "h": 3600, "d": 86400}
    return value * units[from_unit] / units[to_unit]
def convert_currency(value, from_unit, to_unit):
  units={"rs":1,"USD":81.72976,"SGD":61.63241,"EUR":91.6242,"dollars":81.72976}
  return value * units[from_unit] / units[to_unit]
  

# User input
value = float(input("Enter a value: "))
from_unit = input("Enter the unit to convert from: ")
to_unit = input("Enter the unit to convert to: ")

# Determine conversion type
if from_unit in ["m", "cm", "mm", "km", "ft", "in", "yd"] and to_unit in ["m", "cm", "mm", "km", "ft", "in", "yd"]:
    conversion_type = "length"
elif from_unit in ["kg", "g", "mg", "lb", "oz"] and to_unit in ["kg", "g", "mg", "lb", "oz"]:
    conversion_type = "weight"
elif from_unit in ["C", "F", "K"] and to_unit in ["C", "F", "K"]:
    conversion_type = "temperature"
elif from_unit in ["s", "ms", "us", "min", "h", "d"] and to_unit in ["s", "ms", "us", "min", "h", "d"]:
    conversion_type = "time"
elif from_unit in["rs","USD","SGD","EUR","dollars"] and to_unit in ["rs","USD","SGD","EUR","dollars"]:
    conversion_type="currency"
  
else:
    print("Invalid units.")
    exit()

# Perform conversion
if conversion_type == "length":
    result = convert_length(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")
elif conversion_type == "weight":
    result = convert_weight(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")
elif conversion_type == "temperature":
    result = convert_temperature(value, from_unit, to_unit)
    print(f"{value} {from_unit}")
elif conversion_type=="currency":
    result=  convert_currency(value,from_unit,to_unit)
    print(f"{value} {from_unit}={result} {to_unit}")