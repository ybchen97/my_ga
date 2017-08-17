'''
Lesson on file reading using Airline Safety Data
https://github.com/fivethirtyeight/data/tree/master/airline-safety
'''

# read the whole file at once, return a single string (including newlines)
# 'rU' mode (read universal) converts different line endings into '\n'
f = open('/Users/yuanbo/Desktop/my_ga/week1/lab/data/airline-safety.csv', mode='rU')
file_string = f.read()
f.close()

# use a context manager to automatically close your file
with open('/Users/yuanbo/Desktop/my_ga/week1/lab/data/airline-safety.csv', mode='rU') as f:
    file_string = f.read()

# read the file into a list (each list element is one row)
with open('/Users/yuanbo/Desktop/my_ga/week1/lab/data/airline-safety.csv', mode='rU') as f:
    file_list = []
    for row in f:
        file_list.append(row)

# do the same thing using a list comprehension
with open('/Users/yuanbo/Desktop/my_ga/week1/lab/data/airline-safety.csv', mode='rU') as f:
    file_list = [row for row in f]

# side note: splitting strings
'hello DAT students'.split()
'hello DAT students'.split('e')

# split each string (at the commas) into a list
with open('/Users/yuanbo/Desktop/my_ga/week1/lab/data/airline-safety.csv', mode='rU') as f:
    file_nested_list = [row.split(',') for row in f]    # note split() auto returns a list
                                                        # this method includes the \n at the end of each line

# do the same thing using the csv module
import csv
with open('/Users/yuanbo/Desktop/my_ga/week1/lab/data/airline-safety.csv', mode='rU') as f:
    file_nested_list = [row for row in csv.reader(f)]

# separate the header and data
header = file_nested_list[0]
data = file_nested_list[1:]

'''
EXERCISES:

1. Create a list containing the average number of incidents per year for each airline.
Example for Aer Lingus: (2 + 0)/30 = 0.07
Expected output: [0.07, 2.73, 0.23, ...]

2. Create a list of airline names (without the star).
Expected output: ['Aer Lingus', 'Aeroflot', 'Aerolineas Argentinas', ...]

3. Create a list (of the same length) that contains 1 if there's a star and 0 if not.
Expected output: [0, 1, 0, ...]

4. BONUS: Create a dictionary in which the key is the airline name (without the star)
   and the value is the average number of incidents.
Expected output: {'Aer Lingus': 0.07, 'Aeroflot': 2.73, ...}
'''

# Part 1
incidents = [round((int(row[2]) + int(row[5])) / float(30), 2) for row in data]

# Parts 2 and 3
airlines = []
starred = []
for row in data:
    if row[0][-1] == '*':
        starred.append(1)
        airlines.append(row[0][:-1])
    else:
        starred.append(0)
        airlines.append(row[0])

# Part 4
airline_incidents = dict(zip(airlines, incidents))

# my answers:
import csv
with open('/Users/yuanbo/Desktop/my_ga/week1/lab/data/airline-safety.csv', mode='rU') as f:
    file_nested_list = [row for row in csv.reader(f)]

for row in file_nested_list:
    print row

header = file_nested_list[0]
data = file_nested_list[1:]

# Practice 1:
ave_incidents = [round(((float(row[2]) + float(row[5])) / float(30)), 2) for row in data]
print ave_incidents

# Practice 2:
starred = []
non_starred = []

for row in data:
    if row[0][-1] == '*':
        starred.append(row[0][0:-1])
    else:
        non_starred.append(row[0])

print non_starred

# Practice 3:
binary_list = []

for row in data:
    if row[0][-1] == '*':
        binary_list.append(1)
    else:
        binary_list.append(0)

print binary_list

if len(binary_list) == len(data):
    print 'True'

# Practice 4:
clean_list = [row[0][0:-1] if row[0][-1] == '*' else row[0] for row in data]

'''
clean_list = []
for rows in data:
    if rows[0][-1] == '*':
        clean_list.append(rows[0][0:-1])
    else:
        clean_list.append(rows[0])
'''

final_list = dict(zip(clean_list, ave_incidents))

print final_list

'''
A few extra things that will help you with the homework
'''

# 'set' data structure is useful for gathering unique elements
my_list = [1, 2, 1]
set(my_list)            # returns a set of 1, 2
len(set(my_list))       # count of unique elements

# 'in' statement is useful for lists
1 in my_list            # True
3 in my_list            # False

# 'in' is useful for strings (checks for substrings)
my_string = 'hello there'
'the' in my_string      # True
'then' in my_string     # False

# 'in' is useful for dictionaries (checks keys but not values)
my_dict = {'name':'Kevin', 'title':'instructor'}
'name' in my_dict       # True
'Kevin' in my_dict      # False

# 'count' method for strings counts how many times a character appears
my_string.count('e')    # 3
