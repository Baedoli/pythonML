import os
import  glob
import pandas as pd
import numpy as np

# 작업 폴더 지정 ..
# 대리점 및 지역 코드 데이터 프레임 생성 ...
path = '/Users/baeseongho/PycharmProjects/pythonML/'
m_store = pd.read_csv(path+'m_store.csv')
m_area = pd.read_csv(path+'m_area.csv')

# 작업 폴더에 tbl_order_로 시작사는 csv 매출 데이터 파일 목록을 가지는 변수 생성 ..
os.listdir(path)
tbl_order_file = os.path.join(path,'tbl_order_*.csv')
tbl_order_files = glob.glob(tbl_order_file)

# 폴더에 매출 데이터 일괄로 order_all 로 생성 ..
order_all = pd.DataFrame()
for file in tbl_order_files :
    order_data = pd.read_csv(file)
    print((f'{file} : {len(order_data)}'))
    order_all = pd.concat([order_all,order_data],ignore_index=True)

order_all.isnull().sum()
order_all.describe()