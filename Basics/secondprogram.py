import pandas as pd

data = {
    'Spend': [1000, 1500, 2000],
    'Impressions': [50000, 60000, 80000],
    'Link Clicks': [1000, 1500, 2000],
    'Purchases': [50, 75, 100],
    'Purchase Value': [5000, 7500, 12000]
}

df = pd.DataFrame(data)
