import requests


class Insult:
    def __init__(self) -> None:
        self.url = (
            'https://evilinsult.com/generate_insult.php?lang=en&type=json'
        )

    def get_random_insult(self):
        try:
            request = requests.get(self.url)
            request.raise_for_status()
            request = request.json()
            return request['insult']
        except requests.exceptions.ConnectionError:
            print(f"Unable to connect to api {self.url}.")
