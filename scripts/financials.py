import requests, sys

defaultKeyStatistics = requests.get('https://query2.finance.yahoo.com/v10/finance/quoteSummary/'+sys.argv[1]+'?formatted=true&crumb=8ldhetOu7RJ&lang=en-US&region=US&modules=defaultKeyStatistics%2CfinancialData%2CcalendarEvents&corsDomain=finance.yahoo.com')
summaryDetail = requests.get('https://query2.finance.yahoo.com/v10/finance/quoteSummary/'+sys.argv[1]+'?formatted=true&crumb=8ldhetOu7RJ&lang=en-US&region=US&modules=summaryDetail&corsDomain=finance.yahoo.com')
profile = requests.get('https://query1.finance.yahoo.com/v10/finance/quoteSummary/'+sys.argv[1]+'?modules=assetProfile')
defaultKeyStatistics = defaultKeyStatistics.json()
summaryDetail = summaryDetail.json()
profile = profile.json()

print("totalCash " + str(defaultKeyStatistics['quoteSummary']['result'][0]['financialData']['totalCash']['raw']))
print("totalDebt " + str(defaultKeyStatistics['quoteSummary']['result'][0]['financialData']['totalDebt']['raw']))
print("freeCashflow " + str(defaultKeyStatistics['quoteSummary']['result'][0]['financialData']['freeCashflow']['raw']))
print("ebitda " + str(defaultKeyStatistics['quoteSummary']['result'][0]['financialData']['ebitda']['raw']))
print("grossMargins " + str(defaultKeyStatistics['quoteSummary']['result'][0]['financialData']['grossMargins']['raw']))
print("marketCap " + str(summaryDetail['quoteSummary']['result'][0]['summaryDetail']['marketCap']['raw']))
print("industry " + str(profile['quoteSummary']['result'][0]['assetProfile']['industry']))
print("fullTimeEmployees " + str(profile['quoteSummary']['result'][0]['assetProfile']['fullTimeEmployees']))

