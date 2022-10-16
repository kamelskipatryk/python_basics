from urllib import request, response
import requests

coins_list = None
currency = 'pln'

def get_coins_list():
    global coins_list
    # [0] -> {'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}}
    response = requests.get('https://api.coingecko.com/api/v3/coins/list?include_platform=true')
    if response.ok == True:
        print('response ok')
        data = response.json()
        print('Pierwszy element pobranych danych:',data[0])
        print('Ilość kryptowalut na serwerze:', len(data))
        coins_list = data

def find_coin_by_symbol(symbol):
    # {'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'platforms': {}}
    symbol = symbol.lower().strip() # zmiana na małe znaki i usuwanie białych znaków na początku i na końcu
    for coin in coins_list:
        if coin['symbol'] == symbol:
            return coin
    else:
        return None  

def get_coin_last_market_data(coin_id):
    # {'bitcoin': {'pln': 111171, 'pln_24h_vol': 104713884775.95422, 'pln_24h_change': 1.2891796125847792, 'last_updated_at': 1660424999}}
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+coin_id+'&vs_currencies='+currency+'&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true')
    if response.ok:
        data = response.json()
        return data
    else:
        return None

def get_coin_price_in_currency(coin_id, currency):
    currency = currency.lower().strip()
    market_data = get_coin_last_market_data(coin_id)
    return market_data[coin_id][currency]

get_coins_list()
btc_data = find_coin_by_symbol('BTC')
print('btc_data:',btc_data)

market_data = get_coin_last_market_data(btc_data['id'])
print('market_data:',market_data)

coin_price = get_coin_price_in_currency(btc_data['id'], currency )
print( 'Coin price in', currency, coin_price)

print('Witamy w crypto exchange')

while True:
    crypto_symbol_to_buy = input('Wybierz symbol krypto do kupienia (np. btc) lub exit, aby zakończyć: ')
    crypto_symbol_to_buy = crypto_symbol_to_buy.lower().strip()
    if crypto_symbol_to_buy == 'exit': break

    coin_data = find_coin_by_symbol( crypto_symbol_to_buy )
    if coin_data == None:
        print('Nie ma takiej kryptowaluty')
        continue

    coin_price = get_coin_price_in_currency(coin_data['id'], currency) # globalna currency czyli 'pln'
    print('Cena', str(coin_data['id']), coin_price, currency)

    money_to_buy_crypto = float( input('Ile chcesz wydać: ') )
    bought_crypto = money_to_buy_crypto / coin_price

    print('\nGratulacje kupiłeś', str(bought_crypto), crypto_symbol_to_buy)


