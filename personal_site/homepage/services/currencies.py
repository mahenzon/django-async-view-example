import decimal
from decimal import Decimal

import httpx

CURRENCIES_API_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currency}.json"


async def get_exchange_rate(currency: str) -> dict[str, Decimal]:
    currency = currency.lower()
    url = CURRENCIES_API_URL.format(currency=currency)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    data = response.json(parse_float=decimal.Decimal)
    return data[currency]


async def get_exchange_rates(
    source_currency: str,
    *to_currencies: str,
) -> dict[str, Decimal]:
    rates = await get_exchange_rate(source_currency)
    res = {}
    for to_currency in to_currencies:
        res[to_currency] = rates[to_currency]
    # return {
    #     currency: rate for currency, rate in rates.items() if currency in to_currencies
    # }
    return res
