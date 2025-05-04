from dataclasses import dataclass
import random
import logging
import json

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

_COUNTRY_NAME_PROPERTY_NAME = "country"
_CITY_NAME_PROPERTY_NAME = "city"

@dataclass
class ToolProperty:
    propertyName: str
    propertyType: str
    description: str

tool_properties_get_cities_object = [
    ToolProperty(_COUNTRY_NAME_PROPERTY_NAME, "string", "The name of the country.")
]

tool_properties_get_weather_object = [
    ToolProperty(_CITY_NAME_PROPERTY_NAME, "string", "The name of the city.")
]

# Convert the tool properties to JSON
tool_properties_get_cities_json = json.dumps([prop.__dict__ for prop in tool_properties_get_cities_object])
tool_properties_get_weather_json = json.dumps([prop.__dict__ for prop in tool_properties_get_weather_object])

@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="get_cities",
    description="Get list of cities for a given country.",
    toolProperties=tool_properties_get_cities_json,
)
def get_cities(context) -> str:
    """
    Get list of cities for a given country.

    Args:
        context: The trigger context (not used in this function).
        country: The name of the country.

    Returns:
        List of cities
    """

    content = json.loads(context)     
    if "arguments" not in content:
        return "No arguments provided"

    country_name_from_args = content["arguments"].get(_COUNTRY_NAME_PROPERTY_NAME)
    if not country_name_from_args:
        return "No country name provided"
    
    cities_by_country = {
        "usa": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
        "canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"],
        "uk": ["London", "Manchester", "Birmingham", "Leeds", "Glasgow"],
        "australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
        "india": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"],
        "portugal": ["Lisbon", "Porto", "Braga", "Faro", "Coimbra"]
    }

    cities = cities_by_country.get(country_name_from_args.lower(), [])
    return str(cities) 

@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="get_weather",
    description="Get weather information for a given city.",
    toolProperties=tool_properties_get_weather_json,
)
def get_weather(context) -> str:
    """
    Get weather information for a given city.

    Args:
        context: The trigger context (not used in this function).
        city: The name of the city.

    Returns:
        Weather information
    """

    content = json.loads(context)     
    if "arguments" not in content:
        return "No arguments provided"

    city_name_from_args = content["arguments"].get(_CITY_NAME_PROPERTY_NAME)
    if not city_name_from_args:
        return "No country name provided"

    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]
    temperature = random.uniform(-10, 35)  # Random temperature between -10 and 35 degrees Celsius
    humidity = random.uniform(20, 100)  # Random humidity between 20% and 100%

    weather_info = {
        "city": city_name_from_args,
        "condition": random.choice(weather_conditions),
        "temperature": round(temperature, 2),
        "humidity": round(humidity, 2),
    }
    logging.info("Retrieved weather: %s", str(weather_info))
    return str(weather_info)