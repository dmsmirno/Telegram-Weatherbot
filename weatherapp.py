from pyowm import OWM

key = OWM("dummykey")

def forecast(lat, lon):
    observation = key.three_hours_forecast_at_coords(lat, lon)
    forecasts = observation.get_forecast()

    location = forecasts.get_location()
    loc_name = location.get_name()
    loc_lat = location.get_lat()
    loc_lon = location.get_lon()

    results = []
    for forecast in forecasts:
        time = forecast.get_reference_time("iso")
        status = forecast.get_status()
        detailed = forecast.get_detailed_status()
        temperature = forecast.get_temperature()
        temp = temperature.get("temp")
        temp_min = temperature.get("temp_min")
        temp_max = temperature.get("temp_max")

        results.append("""Location : {} Lat : {} Lon : {}
        Time : {}
        Status : {}
        Detailed : {}
        Temperature : {}
        Min Temp : {}
        Max Temp : {}
        """.format(loc_name, loc_lat, loc_lon, time, status, detailed,
        temp, temp_min, temp_max))

        return "".join(results[:1])

