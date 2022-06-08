import pandas as pd
import os 
m_store = pd.read_csv('m_store.csv')
len(m_store)
m_store.head()

m_area = pd.read_csv('m_area.csv')
m_area

tbl_order_4 = pd.read_csv('tbl_order_202104.csv')
tbl_order_4

tbl_order_5 = pd.read_csv('tbl_order_202105.csv')
tbl_order_5

tbl_order_6 = pd.read_csv('tbl_order_202106.csv')
tbl_order_6

order_all = pd.concat([tbl_order_4,tbl_order_5,tbl_order_6],ignore_index=True)
order_all

current_dir = os.getcwd()
os.listdir(current_dir)

tbl_order_file = os.path.join(current_dir,'tbl_order_*.csv')
tbl_order_file

import glob
tbl_order_files = glob.glob(tbl_order_file)
tbl_order_files

order_all = pd.DataFrame()
for file in tbl_order_files :
    order_data = pd.read_csv(file)
    print(f'{file} : {len(order_data)}')
    order_all = pd.concat([order_all, order_data],ignore_index=True)

order_all
order_all.isnull().sum()
