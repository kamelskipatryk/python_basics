# program do odczytywania kursu walut ze strony nbp

import requests

response = requests.get('https://api.nbp.pl/api/exchangerates/tables/a?format=json')

if response.ok == True:
    data = response.json()[0]
    print(data)

    table = data['table']
    no = data['no']
    effectiveDate = data['effectiveDate']

    print('Exchange rates:', table, no, effectiveDate)

    rates = data['rates']

    for rate in rates:
        currency = rate['currency']
        code = rate['code']
        mid = rate['mid']
        zloty = 1/mid
        print('Waluta', currency, '\nKod:', code, 'Kurs:', mid, '1 zł to:', round(zloty, 2), code,'\n')
