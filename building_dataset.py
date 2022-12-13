
import pandas as pd
import numpy as np

stud_marks = pd.DataFrame([[103,'Person 1',15],[104,'Person 2',9],[105,'Person 3',15],[106,'Person 4',9],[107,'Person 5',8],
[108,'Person 6',17],[109,'Person 7',16],[110,'Person 8',20],[112,'JPerson 9',11],
[113,'Person 10',14],[114,'Person 11',9],[115,'Person 12',10],[116,'Person 13',11],[118,'Person 14',16],[119,'Person 15',13],[120,'Person 16',11],[121,'Person 17',13],[123,'Person 18',20]], 
columns=['Roll no','Name','Total (20)'])
# print(len(stud_marks))

stud_marks.to_csv('Mid_Term_Marks.csv', index = True)

