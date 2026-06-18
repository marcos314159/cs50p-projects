import requests
import sys
import json
try:
    response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=1548f7c48c52d45eb00f7f6a4606fb10f6c6a780c905d5000909adb40420f2bd')
    o = response.json()
    data = o['data']
    value = data['priceUsd']

    if len(sys.argv) == 2:
        try:
            input = float(sys.argv[1])
            value = float(value)
            total = value * input
            total = float('{:.4f}'.format(total))
            total = '{:,}'.format(total)
            print(f'${total}')

        except ValueError:
            sys.exit('Command-line argument is not a number')
    else:
        sys.exit('Missing command-line argument')



except requests.RequestException:
    sys.exit('unable to connect')


