



import okex.Account_api as Account

import okex.Funding_api as Funding

import okex.Market_api as Market

import okex.Public_api as Public

import okex.Trade_api as Trade

import okex.subAccount_api as SubAccount

import okex.status_api as Status

import json

api_key = "XXXXX"

secret_key = "XXXXX"

passphrase = "@@pupu9521aA"

accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, '0')

fundingAPI = Funding.FundingAPI(api_key, secret_key, passphrase, False, '0')

marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, True, '0')

publicAPI = Public.PublicAPI(api_key, secret_key, passphrase, False, '0')

tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, '0')





result = marketAPI.get_tickers('SWAP')['data']

short = ""

long = ""

min = 0

max = 0

for i in result:

    if round(((float(i['last'])-(float(i['high24h'])+float(i['low24h']))/2)/float(i['last']))*1000+0.5, 5) < min:

        long = [str(round(((float(i['last'])-(float(i['high24h'])+float(i['low24h']))/2)/float(i['last']))*1000+0.5, 5))+"  "+i['instId']]

        min = round(((float(i['last'])-(float(i['high24h'])+float(i['low24h']))/2)/float(i['last']))*1000+0.5, 5)

    elif round(((float(i['last'])-(float(i['high24h'])+float(i['low24h']))/2)/float(i['last']))*1000+0.5, 5) > max:

        short = [str(round(((float(i['last'])-(float(i['high24h'])+float(i['low24h']))/2)/float(i['last']))*1000+0.5, 5))+"  "+i['instId']]

        max = round(((float(i['last'])-(float(i['high24h'])+float(i['low24h']))/2)/float(i['last']))*1000+0.5, 5)

print("long")

print(long)

print("\nshort")

print(short)
