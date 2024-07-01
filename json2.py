import requests


class BreweryInfo:
    BASE_URL = "https://api.openbrewerydb.org/breweries"

    def __init__(self, states):
        self.states = states
        self.breweries = self.fetch_data()

    def fetch_data(self):
        breweries = []
        for state in self.states:
            response = requests.get(f"{self.BASE_URL}?by_state={state}&per_page=100")
            if response.status_code == 200:
                breweries.extend(response.json())
            else:
                print(f"Error fetching data for state: {state}")
        return breweries

    def list_breweries_by_state(self):
        breweries_by_state = {state: [] for state in self.states}
        for brewery in self.breweries:
            state = brewery['state']
            if state in breweries_by_state:
                breweries_by_state[state].append(brewery['name'])
        for state, breweries in breweries_by_state.items():
            print(f"Breweries in {state}:")
            for name in breweries:
                print(f" - {name}")
            print()

    def count_breweries_by_state(self):
        count_by_state = {state: 0 for state in self.states}
        for brewery in self.breweries:
            state = brewery['state']
            if state in count_by_state:
                count_by_state[state] += 1
        for state, count in count_by_state.items():
            print(f"Number of breweries in {state}: {count}")

    def count_brewery_types_by_city(self):
        types_by_city = {}
        for brewery in self.breweries:
            city = brewery['city']
            if city not in types_by_city:
                types_by_city[city] = {}
            brewery_type = brewery['brewery_type']
            if brewery_type in types_by_city[city]:
                types_by_city[city][brewery_type] += 1
            else:
                types_by_city[city][brewery_type] = 1
        for city, types in types_by_city.items():
            print(f"Brewery types in {city}:")
            for brewery_type, count in types.items():
                print(f" - {brewery_type}: {count}")
            print()

    def count_breweries_with_websites(self):
        count_by_state = {state: 0 for state in self.states}
        for brewery in self.breweries:
            state = brewery['state']
            if state in count_by_state and brewery['website_url']:
                count_by_state[state] += 1
        for state, count in count_by_state.items():
            print(f"Number of breweries with websites in {state}: {count}")


if __name__ == "__main__":
    states = ["Alaska", "Maine", "New York"]
    brewery_info = BreweryInfo(states)

    # 1. List the names of all breweries present in the states of Alaska, Maine, and New York.
    brewery_info.list_breweries_by_state()

    # 2. What is the count of breweries in each of the states mentioned above?
    brewery_info.count_breweries_by_state()

    # 3. Count the number of types of breweries present in individual cities of the states mentioned above.
    brewery_info.count_brewery_types_by_city()

    # 4. Count and list how many breweries have websites in the states of Alaska, Maine, and New York.
    brewery_info.count_breweries_with_websites()
