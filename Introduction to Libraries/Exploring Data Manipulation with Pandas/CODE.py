import pandas as pd
import numpy as np

# ex1

dict= {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df = pd.DataFrame(dict);
print(df)

# ex2

exam_data= {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print(df)

# ex3
print(df[0:3])

# ex4
print(df[['name', 'score']])

# ex5
print(df[df['attempts']>2])

# ex6
print(df[df['score'].isnull()])

# ex7
print(df[df['score']>=15])

# ex8
print(df[(df['attempts'] < 2) & (df['score'] > 15)])

# ex9
df['score']['d'] = 11.5

# ex10
print (df['attempts'].sum())

# ex11
print (df[ 'score' ].mean())

# ex12
df.loc['k'] =  ['Anthony', 16, 2, 'yes']

# ex13
df['students'] = 'yes'
