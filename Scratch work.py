import sankey as sk
import pandas as pd

art = pd.DataFrame({'nationality':['A', 'A', 'B', 'C'],
                   'gender':['M', 'M', 'F', 'M'],
                   'decade':['1930', '1940', '1930', '1940']})


print(art)



# extract out nationality and gender, stack them

e = art[['nationality', 'gender']]
e.columns = ['src' , 'targ']

print(e)
y = art[['gender', 'decade']]
y.columns = ['src' , 'targ']
print(y)


stacked = pd.concat([e, y], axis = 0)  #concat vert

print(stacked)






dict = {"Souren": [10, 20, 30],

        "Hello": [12, 20, 50]}
for key, value in dict.items():
    print(value[1])