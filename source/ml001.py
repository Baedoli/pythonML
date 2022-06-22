import os
import glob
import pandas as pd

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
len(order_all)

order_all['total_amount'].describe()

# 불필요한 마스터 데이터 제거 999 ( 유지보수 지점용 데이터 )
order_data = order_all.loc[order_all['store_id']!=999]

# 마스터 데이터 결함 ..
order_data = pd.merge(order_data,m_store,on='store_id',how='left')
order_data = pd.merge(order_data,m_area,on='area_cd',how='left')

# 수령방법 이름 설정 ..
order_data.loc[order_data['takeout_flag']==0,'takeout_name'] = 'delivery'
order_data.loc[order_data['takeout_flag']==1,'takeout_name'] = 'takeout'

# 주문상태 이름 설정 ..
order_data.loc[order_data['status']==0,'status_name'] = '주문 접수'
order_data.loc[order_data['status']==1,'status_name'] = '지불 완료'
order_data.loc[order_data['status']==2,'status_name'] = '배달 완료'
order_data.loc[order_data['status']==9,'status_name'] = '주문 취소'

#  파일 저장  ...
output_dir = os.path.join(path,'output_data')
os.makedirs(output_dir,exist_ok=True)
output_file = os.path.join(output_dir,'order_data.csv')
order_data.to_csv(output_file,index=False)

