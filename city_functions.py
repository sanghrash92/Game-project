def get_formatted_city_country(city, country, population=''):
    """Generate a neatly formatted city and country."""
    if population:
        fullname = f"{city}, {country}, {population}"
    else:
        fullname = f"{city}, {country}"
    return fullname.title()

