import requests

API_Key = "28ea11e54b5618c5d9c8cc20a758de96"

def get_data(place, days = 1, kind = "Temperature"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]

    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    else:
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data("Tokyo"))