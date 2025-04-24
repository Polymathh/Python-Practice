rates = {
    'KES' : 130.25,
    'EUR' :0.92,
    'GBP' : 0.79
}

usd = float(input('Enter amount in USD: '))

for currency, rate in rates.items():
    converted = usd * rate

    print(f"{usd} USD = {converted: 2f} {currency}")
    
