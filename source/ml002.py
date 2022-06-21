
import  pandas as pd
import os

path = os.getcwd()
order_data = pd.read_csv(path+'/output_data/order_data.csv')
order_data.head()
order_data = order_data.loc[(order_data['status']==1)|(order_data['status']==2)]
order_data.head()
order_data.columns