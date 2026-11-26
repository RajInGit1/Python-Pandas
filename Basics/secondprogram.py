import pandas as pd

data = {
    'Spend': [1000, 1500, 2000],
    'Impressions': [50000, 60000, 80000],
    'Link Clicks': [1000, 1500, 2000],
    'Purchases': [50, 75, 100],
    'Purchase Value': [5000, 7500, 12000]
}

df = pd.DataFrame(data)


total_spend = df['Spend'].sum()
total_impressions = df['Impressions'].sum()
total_clicks = df['Link Clicks'].sum()
total_purchases = df['Purchases'].sum()
total_purchase_value = df['Purchase Value'].sum()

CPM = (total_spend / total_impressions) * 1000

CPC = total_spend / total_clicks

CPR = total_spend / total_purchases

CTR = (total_clicks / total_impressions) * 100

Purchase_Rate = (total_purchases / total_clicks) * 100

ROAS = total_purchase_value / total_spend
