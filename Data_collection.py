import pandas as pd

df1 = pd.read_csv('C:/Users/kdh70/Software/Asheville.csv', encoding='ANSI', header=0)
df2 = pd.read_csv('C:/Users/kdh70/Software/Austin.csv', encoding='ANSI', header=0)
df3 = pd.read_csv('C:/Users/kdh70/Software/Boston.csv', encoding='ANSI', header=0)
df4 = pd.read_csv('C:/Users/kdh70/Software/Cambridge.csv', encoding='ANSI', header=0)
df5 = pd.read_csv('C:/Users/kdh70/Software/Chicago.csv', encoding='ANSI', header=0)
df6 = pd.read_csv('C:/Users/kdh70/Software/Clark.csv', encoding='ANSI', header=0)
df7 = pd.read_csv('C:/Users/kdh70/Software/Columbus.csv', encoding='ANSI', header=0)
df8 = pd.read_csv('C:/Users/kdh70/Software/Denver.csv', encoding='ANSI', header=0)
df9 = pd.read_csv('C:/Users/kdh70/Software/Jersey.csv', encoding='ANSI', header=0)
df10 = pd.read_csv('C:/Users/kdh70/Software/Hawaii.csv', encoding='ANSI', header=0)
df11 = pd.read_csv('C:/Users/kdh70/Software/LosAngeles.csv', encoding='ANSI', header=0)
df12 = pd.read_csv('C:/Users/kdh70/Software/Nashville.csv', encoding='ANSI', header=0)
df13 = pd.read_csv('C:/Users/kdh70/Software/Broward.csv', encoding='ANSI', header=0)
df14 = pd.read_csv('C:/Users/kdh70/Software/New Orleans.csv', encoding='ANSI', header=0)
df15 = pd.read_csv('C:/Users/kdh70/Software/New York.csv', encoding='ANSI', header=0)
df16 = pd.read_csv('C:/Users/kdh70/Software/Oakland.csv', encoding='ANSI', header=0)
df17 = pd.read_csv('C:/Users/kdh70/Software/Pacific.csv', encoding='ANSI', header=0)
df18 = pd.read_csv('C:/Users/kdh70/Software/Portland.csv', encoding='ANSI', header=0)
df19 = pd.read_csv('C:/Users/kdh70/Software/Rhode.csv', encoding='ANSI', header=0)
df20 = pd.read_csv('C:/Users/kdh70/Software/Salem.csv', encoding='ANSI', header=0)
df21 = pd.read_csv('C:/Users/kdh70/Software/San Diego.csv', encoding='ANSI', header=0)
df22 = pd.read_csv('C:/Users/kdh70/Software/San Francisco.csv', encoding='ANSI', header=0)
df23 = pd.read_csv('C:/Users/kdh70/Software/San Mateo.csv', encoding='ANSI', header=0)
df24 = pd.read_csv('C:/Users/kdh70/Software/Santa Clara.csv', encoding='ANSI', header=0)
df25 = pd.read_csv('C:/Users/kdh70/Software/Santa Cruz.csv', encoding='ANSI', header=0)
df26 = pd.read_csv('C:/Users/kdh70/Software/Seattle.csv', encoding='ANSI', header=0)
df27 = pd.read_csv('C:/Users/kdh70/Software/Twin.csv', encoding='ANSI', header=0)
df28 = pd.read_csv('C:/Users/kdh70/Software/Washinton.csv', encoding='ANSI', header=0)

#흩어진 데이터들을 하나로 합침
all_data = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df24, df25, df26, df27, df28], axis=0, sort=False)
all_data.to_csv("C:/Users/kdh70/Software/all data.csv", mode='w')

data = pd.read_csv('C:/Users/kdh70/Software/all data.csv', encoding='ANSI', header=0)





