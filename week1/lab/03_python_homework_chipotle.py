'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

# specify that the delimiter is a tab character
# make 'file_nested_list' = list of rows
with open('/Users/yuanbo/Desktop/my_ga/week1/lab/data/order.tsv', mode='rU') as tsv_f:
    file_nested_list = [row for row in csv.reader(tsv_f, delimiter='\t')]


'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header = file_nested_list[0]
data = file_nested_list[1:]



'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

# count the number of unique order_id's
count = 1

for row in data:
    if int(row[0]) > count:
        count += 1
print count

# note: you could assume this is 1834 since that's the maximum order_id, but it's best to check

# create a list of prices
prices = [float(row[-1][1:-1]) for row in data]
print prices

# calculate the average price of an order and round to 2 digits
total_price = 0
for i in prices:
    total_price += i
    i += 1

ave_price = round(total_price / count, 2)
print ave_price

# $18.81


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

# if 'item_name' includes 'Canned', append 'choice_description' to 'sodas' list
# sodas = []
'''
for row in data:
    if 'Canned' in row[2]:              # take note strings are case-sensitive
        sodas.append(row[3][1:-1])
'''

# equivalent list comprehension (using an 'if' condition)
sodas = [row[3][1:-1] for row in data if 'Canned' in row[2]]            # list comprehensions don't need .append()
print sodas
# create a set of unique sodas

unique_sodas = []

for item in sodas:
    if item not in unique_sodas:
        unique_sodas.append(item)
print unique_sodas

# unique_sodas = [item for item in sodas if item not in unique_sodas]

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
burrito_count = 0
toppings_count = 0

for row in data:
    if 'Burrito' in row[2]:
        burrito_count += 1
        topping = row[3].count(',') + 1
        toppings_count += topping

ave_toppings = round(float(toppings_count) / burrito_count, 2)
print ave_toppings

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

# start with an empty dictionary
chips = {}

for row in data:
    if 'Chips' in row[2]:
        if row[2] not in chips:
            chips[row[2]] = 1 * int(row[1])
        else:
            chips[row[2]] += 1 * int(row[1])

print chips

# defaultdict saves you the trouble of checking whether a key already exists



'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
