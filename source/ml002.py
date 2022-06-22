
import  pandas as pd
import os
import warnings
import matplotlib.pyplot as plt
import seaborn as sns


plt.rc('font',family='AppleGothic')
plt.rc('axes',unicode_minus=False)

warnings.filterwarnings('ignore')
# path = os.getcwd()
path =  '/Users/baeseongho/PycharmProjects/pythonML'
order_data = pd.read_csv(path+'/output_data/order_data.csv')
order_data = order_data.loc[(order_data['status']==1)|(order_data['status']==2)]
order_data.head()
order_data.columns
len(order_data)

analyze_data = order_data[['store_id', 'customer_id', 'coupon_cd', 'order_accept_date', 'delivered_date', 'total_amount',
                           'store_name', 'wide_area', 'narrow_area', 'takeout_name', 'status_name']]

analyze_data.shape
analyze_data.head()

analyze_data.describe()
analyze_data.dtypes

analyze_data[['store_id','coupon_cd']] = analyze_data[['store_id','coupon_cd']].astype(str)
analyze_data.dtypes

# 주문일자 타입을 문자에서 날짜 형으로 바꾸고 .. 월별로 자동 변환한 칼럼을 하나 추가 함 ..
analyze_data['order_accept_date'] = pd.to_datetime(analyze_data['order_accept_date'])
analyze_data['order_accept_month'] = analyze_data['order_accept_date'].dt.strftime('%Y%m')
analyze_data[['order_accept_date','order_accept_month']].head()

analyze_data['delivered_date'] = pd.to_datetime(analyze_data['delivered_date'])
analyze_data['delivered_month'] = analyze_data['delivered_date'].dt.strftime('%Y%m')
analyze_data[['delivered_date','delivered_month']].head()

month_data = analyze_data.groupby('order_accept_month')
month_data.head()
month_data.describe()
month_data.sum()

plt.hist(analyze_data['total_amount'],bins=24)
plt.show()

pre_data = pd.pivot_table(analyze_data,index='order_accept_month',columns='narrow_area',values='total_amount',aggfunc='mean')
pre_data

plt.plot(list(pre_data.index),pre_data['서울'],label='서울')
plt.plot(list(pre_data.index),pre_data['부산'],label='부산')
plt.plot(list(pre_data.index),pre_data['대전'],label='대전')
plt.plot(list(pre_data.index),pre_data['광주'],label='광주')
plt.plot(list(pre_data.index),pre_data['세종'],label='세종')
plt.show()

store_clustring = analyze_data.groupby('store_id').agg(['size','mean','median','max','min'])['total_amount']
store_clustring.reset_index(inplace=True,drop=True)
len(store_clustring)
store_clustring.head()
hexbin = sns.jointplot(x='mean',y='size',data=store_clustring,kind='hex')
plt.show()

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
store_clustring_sc = sc.fit_transform(store_clustring)

kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(store_clustring_sc)
store_clustring['cluster'] = clusters.labels_
print(store_clustring['cluster'].unique())
store_clustring.head()

store_clustring.columns = ['월 건수','월 평균값','월 중앙값','월 최댓값','월 최소값','cluster']
store_clustring.head()
store_clustring.groupby('cluster').count()
store_clustring.groupby('cluster').mean()

from sklearn.manifold import TSNE
tsne = TSNE(n_components=2,random_state=0)
x = tsne.fit_transform(store_clustring_sc)

tsne_df = pd.DataFrame(x)
tsne_df['cluster'] = store_clustring['cluster']
tsne_df.columns = ['axis_0','axis_1','cluster']
tsne_df.head()

tsne_graph = sns.scatterplot(x='axis_0',y='axis_1',hue='cluster',data=tsne_df)
plt.show()