import pandas as pd
from students import students

# Goals 
# master use of .melt() to reshape data frame 
# the use of .duplicates and get rid of them 
# split column values into different columns 
# update data frame with only desire columns 
# use .str.get() for strings and .str[:] for characters 
# convert objects into int or floats to make calculations using .replace([''], '' , regex=True)
# more string parsing .replace (\d+) d= [0-9] '+' = one or more 
# dealing with missing values, either deleting rows with missing values or replacing them 




print('Initial Data Frame:'+str(students.columns))
# using melt to change the data frame 
# frame: the DataFrame you want to melt
# id_vars: the column(s) of the old DataFrame to preserve
# value_vars: the column(s) of the old DataFrame that you want to turn into variables
# value_name: what to call the column of the new DataFrame that stores the values
# var_name: what to call the column of the new DataFrame that stores the variables

students = pd.melt(frame=students,\
                     id_vars=['full_name','gender_age','grade'],\
                     value_vars=['fractions', 'probability'],\
                     value_name='score',\
                     var_name='exam')



# getting the new reshaped data frame, column names and exam value counts
print('Reshaped Data Frame:\n'+str(students.head()))
print(students.columns)
print(students.exam.value_counts())

# seeing how many students have been duplicated True means there are duplicates 
duplicates = students.duplicated()

print('\nStudents with  duplicates:')

print(duplicates.value_counts())

# df.drop_duplicates() deletes the duplicates in the data frame 
students = students.drop_duplicates()
duplicates = students.duplicated()
print('\nStudents with no duplicates:')
print(duplicates.value_counts())

# separate gender_age into two different columns 
students['gender'] = students.gender_age.str[0]
students['age'] = students.gender_age.str[1:]

print(students.head())

# gender_age column no longer needed so update students data frame 
students = students[['full_name','grade', 'exam','score', 'gender','age']]
print('\nStudents data frame without gender_age column:\n'+str(students.head()))


# namesplit will split the column 'full_name' so that we can create new columns, first_name and last_name using .str.get() and .str.split()
name_split = students['full_name'].str.split(" ")

students['first_name'] = name_split.str.get(0)
students['last_name'] = name_split.str.get(1)
print('\nStudents data frame with columns first_name and last_name:')
print(students.head())

# convert score column to a float for calculation 
students.score = students['score'].replace(['\%'], '', regex = True)
# now convert student.score into numeric values 

print('\nStudent data frame with numeric value for column score for calculations:')
students.score = pd.to_numeric(students.score )

# get grade  numeric value to eventually get the average 
students.grade = students['grade'].str.split('(\d+)', expand = True)[1]
students.grade = pd.to_numeric(students.grade)
print('/nStudents data types:')
print(students.dtypes)

grade_average = students.grade.mean()
print('\nAverage student grade:\n' +str(round(grade_average,0)))

# filling up empty score values, changes the average/mean
print('Score Mean:'+str(students.score.mean()))
students = students.fillna(value = {'score': 0})
# another easy way is .fillna(0) but this is for all Nan values, not specific columns 
print('Score Mean:'+str(students.score.mean()))
