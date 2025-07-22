temp = float(input("Enter the temperature: "))
unit = input("Is the temperature in Fahrenheit (F) or Celsius (C)? ").strip().upper()

while True:
    if unit not in ['F', 'C']:
        print("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
        unit = input("Is the temperature in Fahrenheit (F) or Celsius (C)? ").strip().upper()
    else:
        break

def wind_chill(temperature, wind_speed):
    # Calculate the wind chill index using the formula
    wind_chill_index = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return round(wind_chill_index, 2)

def unit_convertion(temperature):
    # Convert Celsius to Fahrenheit
    return (temperature * 9 / 5) + 32

if unit == 'C':
    temp = unit_convertion(temp)

for wind_speed in range(5, 65, 5):
    # Calculate and print the wind chill for each wind speed
    print(f'At temperature {temp}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill(temp, wind_speed)}F.')