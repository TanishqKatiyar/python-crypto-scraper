if __name__ == '__main__':
    print('Running scraper...')

def fetch_data(url):
    response = requests.get(url)
    return response.json()

