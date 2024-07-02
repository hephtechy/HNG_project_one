from flask import Flask, request, jsonify
import requests


app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
    url = "https://api.geoapify.com/v1/ipinfo?apiKey=1b12fda6b84d4f658f751913397c291f"

    response = requests.get(url)

    message=response.json()

    client_ip = message['ip']
    location = message["city"]["name"]

    latitude = message['location']['latitude']
    longitude = message['location']['longitude']

    key = 'f1a9d0152acc4c86be2067de2f512b79'
    temp_url = 'https://api.weatherbit.io/v2.0/current?lat={}&lon={}&key={}'

    try:
        result = requests.get(temp_url.format(latitude,longitude,key)).json()
    except:
        print('try again')

    temperature = result['data'][0]['temp']

    visitor_name = request.args.get('visitor_name')


    greeting = f"Hello, {visitor_name[1:-1]}!, the temperature is {temperature} degrees Celcius in {location}"

    return {
      "client_ip": client_ip,
      "location": location,
      "greeting": greeting
    }



# if __name__ == '__main__':
#     app.run(debug=True)
