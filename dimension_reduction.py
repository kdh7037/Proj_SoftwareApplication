# -*- coding: utf-8 -*-
"""amenity_red.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kgUDUhqa_2oQ-gVOQuIu7d8l4n3LySpk
"""


# Commented out IPython magic to ensure Python compatibility.
# %cd drive/My Drive/Colab Notebooks

import pandas as pd

df = pd.read_csv('data_cleansed_final.csv')

from sklearn.feature_selection import VarianceThreshold

#특징 선택 
X = df.to_numpy()
sel = VarianceThreshold(threshold = (.8*(1.-.8)))
X = sel.fit_transform(X)

from sklearn.preprocessing import StandardScaler

#표준화
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

from sklearn.decomposition import PCA

#특징 추출 (PCA)
pca = PCA(n_components=0.8)

X_reduced = pca.fit_transform(X_scaled)

print(X_reduced)


print('eigen_value :', pca.explained_variance_)
print('explained variance ratio :', pca.explained_variance_ratio_)

#축소된 데이터 저장
pd.DataFrame(X_reduced).to_csv('reduced_data_36.csv', index=False)
from google.colab import files
print('complete')
#files.download('reduced_data_36.csv')

'''
#famd 차원축소방법(사용하지 않았다.)
famd = prince.FAMD(n_components=10, n_iter=3, copy=True, check_input=True, engine='auto', random_state=42 )
famd = famd.fit(data)
famd.row_coordinates(data)
'''

#36차원으로 축소된 데이터를 t-SNE로 2차원으로 차원축소 및 시각화
data36 = pd.read_csv('reduced_data_36.csv', encoding='utf-8', header=0)
projection = TSNE().fit_transform(data36)
plot_kwds = {'alpha' : 0.5, 's' : 1, 'linewidths':0}
plt.scatter(*projection.T, **plot_kwds)