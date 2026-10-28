import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)






import requests

url = "https://httpbin.org/post"

# The data you want to send to the server
payload = {
    "name": "Alice",
    "email": "alice@example.com",
    "city": "Paris"
}

# Send the POST request with JSON data
response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())





import requests

# Let's say we are updating user ID 42
url = "https://httpbin.org/put"

# The updated information
updated_data = {
    "id": 42,
    "name": "Alice",
    "city": "Lyon"  # Changed city from Paris to Lyon
}

# Send the PUT request
response = requests.put(url, json=updated_data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())