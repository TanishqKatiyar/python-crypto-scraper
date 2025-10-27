try:
    results = parse_html(content)
except Exception as e:
    logging.error(f'Error parsing: {e}')

if __name__ == '__main__':
    print('Running scraper...')

