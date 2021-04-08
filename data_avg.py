# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/drive/My Drive/SWAPP'

data = pd.read_csv('data_cleansed_final.csv', encoding='utf-8', header=0)
clu = pd.read_csv('prosize2000_clulabel.csv', names=['cluster_label'], header = None, encoding='utf-8',)
#데이터에 클러스터 그룹 목록을 추가한 DataFrame 생성
data = pd.concat([data, clu], axis=1)

#클러스터 최대 그룹 계산
max = data['cluster_label'].max()

#클러스터 그룹별 각 항목의 평균 계산
outsider = data[data['cluster_label'] == -1]
result = pd.DataFrame()
for i in range(0, max + 1):
    temp = data[data['cluster_label'] == i].mean()
    result = pd.concat([result, temp], axis=1, ignore_index=True)
result.to_csv("/content/drive/My Drive/SWAPP/2000_clu_cha.csv", mode='w')