import pandas as pd
customer_master = pd.read_csv('customer_master.csv')
customer_master.head()
for customer in customer_master:
	print(customer)