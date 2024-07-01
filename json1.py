import requests


class CountryInfo:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

    def display_country_info(self):
        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            currency_info = ', '.join([f"{cur} ({details.get('symbol', 'N/A')})"
                                       for cur, details in currencies.items()])
            print(f"Country: {name}, Currencies: {currency_info}")

    def display_countries_with_currency(self, currency_name):
        for country in self.data:
            currencies = country.get('currencies', {})
            if any(currency_name in cur for cur in currencies.keys()):
                name = country.get('name', {}).get('common', 'N/A')
                print(name)

    def display_countries_with_dollar(self):
        print("Countries with Dollar as currency:")
        self.display_countries_with_currency('Dollar')

    def display_countries_with_euro(self):
        print("Countries with Euro as currency:")
        self.display_countries_with_currency('Euro')


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    country_info = CountryInfo(url)

    # Display name of countries, currencies & currency symbols
    country_info.display_country_info()

    # Display countries with Dollar as currency
    country_info.display_countries_with_dollar()

    # Display countries with Euro as currency
    country_info.display_countries_with_euro()
