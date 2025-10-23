import pandas as pd
import numpy as np

try:
    results = parse_html(content)
except Exception as e:
    logging.error(f'Error parsing: {e}')

