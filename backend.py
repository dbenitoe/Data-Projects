import requests

API_KEY = "40567eb7618a82791855bb5b51ee8c47"


def get_data(place, forcast_days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    if option == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if option == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forcast_days=5,option="Temperature"))
