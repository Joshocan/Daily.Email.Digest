from urllib import request
import json
import datetime


class DailyDigestContents:

    def get_weather_forecast(self, city='Bergen', state='no'):
        try:
            with open('forecast_api.txt', 'r') as api:
                api_key = api.read()
            api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&APPID={api_key}&units=metric'
            data = json.load(request.urlopen(api_url))
            period = datetime.datetime.fromtimestamp(data['dt'])
            sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
            sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

            forecast_data = {'city': data['name'],
                        'country': data['sys']['country'],
                        'current_date': period,
                        'sunrise': sunrise,
                        'sunset': sunset,
                        'temperature': round(data['main']['temp']),
                        'min_temperature': round(data['main']['temp_min']),
                        'max_temperature': round(data['main']['temp_max']),
                        'humidity': round(data['main']['humidity']),
                        'weather_condition': data['weather'][0]['description']

                        }

            return forecast_data
#            return data_formatted
        except Exception as e:
            print(e)

    def get_sport_update(self):
        pass
    def get_political_update(self):
        pass
    def get_twitter_update(self):
        pass

if __name__ == '__main__':
    city = 'Ashaiman'
    state = 'Ghana'
    api_data = DailyDigestContents().get_weather_forecast(city,state)
    print('Printing the values of api data \n')
    print(api_data)






