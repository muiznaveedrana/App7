import requests

API_Key = "28ea11e54b5618c5d9c8cc20a758de96"

def get_data(place, days = 1, kind = "temperature"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data

if __name__ == "__main__":
    get_data("Tokyo")