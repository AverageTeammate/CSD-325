# Jacob Cannamela
# CSD325
#11/30/2024

# Creating the main function

def city_country(city, country, population=None, language=None):
    """Returns a formatted string of the form 'City, Country - population xxx, Language',
    but omits the population and/or language if not provided."""
    # Build the base string with city and country
    result = f"{city}, {country}"
    # Add population if provided
    if population:
        result += f" - population {population}"
    # Add language if provided
    if language:
        result += f", {language}"
    return result

# Calling the function three times with different cities, countries, and populations
print(city_country('Santiago', 'Chile'))
print(city_country('Paris', 'France'))
print(city_country('Tokyo', 'Japan'))

