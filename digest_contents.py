from urllib import request
import json
import datetime
class DailyDigestContents:
    def get_weather_forecast(self, city='Bergen', state='no'):
        try:
            with open('forecast_api.txt', 'r') as api:
                api_key = api.read()
            forecast_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&APPID={api_key}&units=metric'
            data = json.load(request.urlopen(forecast_url))
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
                             'weather_condition': data['weather'][0]['description']}

            return forecast_data
#            return data_formatted
        except Exception as e:
            print(e)

    def get_sport_update(self, country='gb'):
        try:
            with open('sport_api.txt', 'r') as api:
                api_key = api.read()

            sport_url = f'http://newsapi.org/v2/top-headlines?country={country}&category=sports&apiKey={api_key}'
            data = json.load(request.urlopen(sport_url))
            top_data = dict()
            top_new = []
            for top in data['articles']:
                top_data.update({'source': top['source']['name'],
                                 'title': top['title'],
                                 'url': top['url'],
                                 'date_published': top['publishedAt']})

                top_new.append(top_data)

            return json.dumps(top_new, indent=4)
        except Exception as e:
            print(e)

    def get_political_update(self, country='gb'):
        try:
            with open('sport_api.txt', 'r') as api:
                api_key = api.read()

            politics_url = f'http://newsapi.org/v2/top-headlines?country={country}&category=sports&apiKey={api_key}'
            data = json.load(request.urlopen(politics_url))
            top_data = dict()
            top_new = []
            for top in data['articles']:
                top_data.update({'source': top['source']['name'],
                                 'title': top['title'],
                                 'url': top['url'],
                                 'date_published': top['publishedAt']})

                top_new.append(top_data)

            return json.dumps(top_new, indent=4)
        except Exception as e:
            print(e)



    def get_twitter_update(self):
        try:
            pass
        except Exception as err:
            print(err)

if __name__ == '__main__':
    city = 'Ashaiman'
    state = 'Ghana'
    forecast_data = DailyDigestContents().get_weather_forecast(city,state)
    print('Testing values from weather api data \n')
    print(forecast_data)

    country = 'gb'
    sport_data = DailyDigestContents().get_sport_update(country)
    print('Testing the top 20 sports headline  \n')
    print(sport_data)

    politics = DailyDigestContents().get_political_update(country='it')
    print(politics)










