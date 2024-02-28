import phonenumbers
from phonenumbers import geocoder
from geopy.geocoders import Nominatim
import folium

phone_number = phonenumbers.parse("+17173798809")
country_name = geocoder.description_for_number(phone_number, "en")

geolocator = Nominatim(user_agent="phone_locator")
location = geolocator.geocode(country_name)

if location:
    state_info = (location.raw.get("address", {}).get("state") or
                  location.raw.get("address", {}).get("state_district", ""))
    
    location_info = f"{state_info}, {country_name}"

    phone_map = folium.Map(location=[location.latitude, location.longitude], zoom_start=5)
    folium.Marker(location=[location.latitude, location.longitude], popup=location_info).add_to(phone_map)
    
    phone_map.save("phone_location_map.html")
    print(f"Map saved as phone_location_map.html for {location_info}")
else:
    print(f"Could not determine coordinates for {country_name}")
