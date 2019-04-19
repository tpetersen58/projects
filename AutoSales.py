import pandas as pd
import pymssql
import matplotlib.pyplot as plt

conn = pymssql.connect(server="127.0.0.1", user="taylorp",password='taylorp', port=1433)

stmt = '''SELECT CASE Make WHEN 'Mercedes Benz' THEN 'Benz' ELSE Make END AS Make
FROM CARS
GROUP BY Make
ORDER BY AVG(YearlyTotal) DESC
'''
stmt2 = ''' SELECT AVG(YearlyTotal)/1000000 as Sum
FROM CARS
GROUP BY Make
ORDER BY AVG(YearlyTotal) DESC'''

df = pd.read_sql(stmt, conn)
df2 = pd.read_sql(stmt2, conn)
Make = df.values.tolist()
Sum = df2.values.tolist()

colorList = ['seagreen','mediumpurple','goldenrod','mediumblue']
for i in range(len(Make)):
    plt.title("Avg US Auto Sales/Year")
    plt.ylabel('Auto Sales/Year (millions)')
    fig = plt.figure(1, figsize=(20,3))
    ax = plt.subplot(111)
    plt.xticks(rotation=90)
    plt.bar(Make[i], Sum[i]) #color=colorList[i%4])
    plt.tight_layout()

plt.show()
