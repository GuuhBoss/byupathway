# Data Analysis of Life Expectancy
# Added The most common life expectancy (rounded) for the year of interest

year_of_interest = input("Enter the year of interest: ")

with open("life-expectancy.csv") as file:
    next(file)

    overall_min = {"country": "", "year": 0, "expectancy": float("inf")}
    overall_max = {"country": "", "year": 0, "expectancy": float("-inf")}

    year_data = {}
    for line in file:
        parts = line.strip().split(',')
        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])

        # Track overall min and max
        if life_expectancy < overall_min["expectancy"]:
            overall_min = {"country": country, "year": year, "expectancy": life_expectancy}
        if life_expectancy > overall_max["expectancy"]:
            overall_max = {"country": country, "year": year, "expectancy": life_expectancy}

        # Gather data for selected year
        if year == year_of_interest:
            year_data[country] = {"life_expectancy": life_expectancy}

# Calculate year-specific stats
if year_data:
    max_country = min_country = ''
    max_val = float('-inf')
    min_val = float('inf')
    total = 0
    common_life_expectancy = {}
    most_common_life_expectancy = {}
    counter = 0

    # Retrieve max, min, and average for the specified year
    for country, data in year_data.items():
        total += data["life_expectancy"]
        if data["life_expectancy"] > max_val:
            max_country = country
            max_val = data["life_expectancy"]

        if data["life_expectancy"] < min_val:
            min_country = country
            min_val = data["life_expectancy"]

        # Track life expectancy for all years
        rounded_life_expectancy = round(data["life_expectancy"])
        if rounded_life_expectancy not in common_life_expectancy:
            common_life_expectancy[rounded_life_expectancy] = {'counter': 0, 'countries': [], 'expectancy': rounded_life_expectancy}

        common_life_expectancy[rounded_life_expectancy]['counter'] += 1
        common_life_expectancy[rounded_life_expectancy]['countries'].append(country)

        for life_expectancy, common_life_expectancy_value in common_life_expectancy.items():
            if common_life_expectancy_value['counter'] > counter:
                counter = common_life_expectancy_value['counter']
                most_common_life_expectancy = common_life_expectancy[life_expectancy]
    avg = total / len(year_data)
    print()
    print(f"""The overall max life expectancy is: {overall_max['expectancy']} from {overall_max['country']} in {overall_max['year']}
The overall min life expectancy is: {overall_min['expectancy']} from {overall_min['country']} in {overall_min['year']}

For the year {year_of_interest}:
The average life expectancy across all countries was {avg:.2f}
The max life expectancy was in {max_country} with {max_val}
The min life expectancy was in {min_country} with {min_val}
The most common life expectancy was {most_common_life_expectancy['expectancy']} with {most_common_life_expectancy['counter']} countries. (Countries: {', '.join(most_common_life_expectancy['countries'])})""")
else:
    print(f"No data found for the year {year_of_interest}.")
