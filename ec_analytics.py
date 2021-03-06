import pandas as pd

# CSV読み込み 
customer_master = pd.read_csv('customer_master.csv')
print(customer_master.head())

item_master = pd.read_csv('item_master.csv')
print(item_master.head())

transaction_1 = pd.read_csv('transaction_1.csv')
print(transaction_1.head())

transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')
print(transaction_detail_1.head())

# 結合(ユニオン)
transaction_2 = pd.read_csv('transaction_2.csv')
transaction = pd.concat([transaction_1,transaction_2], ignore_index=True)
print(transaction.head())
print(len(transaction_1))
print(len(transaction_2))
print(len(transaction))

transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')
transaction_detail = pd.concat([transaction_detail_1,transaction_detail_2], ignore_index=True)
print(transaction_detail.head())
print(len(transaction_detail_1))
print(len(transaction_detail_2))
print(len(transaction_detail))

# 結合(ジョイン)
join_data = pd.merge(transaction_detail, transaction[["transaction_id","payment_date","customer_id"]],on="transaction_id",how="left")
print(join_data.head())
print(len(transaction_detail))
print(len(transaction))
print(len(join_data))

# マスターのジョイン
join_data = pd.merge(join_data, customer_master, on="customer_id",how="left")
join_data = pd.merge(join_data, item_master, on="item_id",how="left")
print(join_data.head())
