
import pandas as pd
from IPython.display import display, clear_output
from ipywidgets import Dropdown


path = '/Users/baeseongho/PycharmProjects/pythonML/'
m_store = pd.read_csv(path+'m_store.csv')
m_area = pd.read_csv(path+'m_area.csv')
order_date = pd.read_csv(path+'tbl_order_202104.csv')
order_date.head()

order_date.loc[order_date['takeout_flag']==0,'takeout_name'] = 'delivery'
order_date.loc[order_date['takeout_flag']==1,'takeout_name'] = 'takeout'

order_date.loc[order_date['status']==0,'status_name'] = '주문접수'
order_date.loc[order_date['status']==1,'status_name'] = '결재완료'
order_date.loc[order_date['status']==2,'status_name'] = '배달완료'
order_date.loc[order_date['status']==9,'status_name'] = '주문취소'

def order_by_store(val) :
    clear_output()
    display(dropdown)
    pick_data = order_date.loc[(order_date['store_name']==val('new')&order_date['status'].isin([1,2]))]
    display(pick_data.head())

store_list = m_store['store_name'].to_list()
dropdown = Dropdown(options=store_list,description='지역 선택 :')
dropdown.observe(order_by_store,names='value')
display(dropdown)