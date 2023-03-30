# -*- coding: UTF-8 -*-
# """PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
import pandas
import prettytable
from pathlib import Path
from prettytable import PrettyTable

pt = PrettyTable()

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('')
sales_filepath = Path('')

csv_menu_data = ""
csv_sales_data = ""

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []
report = {}
inv_report = {}
item_details = {}

# @TODO: Read in the menu data into the menu list
menu_filepath = Path("./PyRamen/Resources/menu_data.csv")
sales_filepath = Path("./PyRamen/Resources/sales_data.csv")
# print(f"the menu data is in {menu_filepath}")
# print(f"the sales data is in {sales_filepath}")

print(menu_filepath)
lst = []

# open the menu data file for reading
with open(menu_filepath, 'r') as csv_menu:
    csv_menu_data = csv.reader(csv_menu)
    menu_header = next(csv_menu_data)
    
    # read all the menu data
    for line in csv_menu_data:
        lst = []
        lst.append(line[0])     # item
        lst.append(line[1])     # category
        lst.append(line[2])     # description
        lst.append(line[3])     # price        
        lst.append(line[4])     # cost
# create a list of the line items
        item_details[line[0]] = {"category": line[1], "description": line[2], "price" : float(line[3]), "cost" : float(line[4])}

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
# to report the results from the sales per menu item.
        inv_report[line[0]] = {"01-count" : 0, "02-revenue" : 0, "03-cogs" : 0, "04-profit" : 0}


#    for key in item_details:
#        print(f" + The item {key} has a price of {item_details[key]['price']} and a cost of {item_details[key]['cost']}")
# the total different menu items available
# print(f"\nreport has {len(inv_report)} elements ")

# open the sales data file for reading    
with open(sales_filepath, 'r') as csv_sales:
    csv_sales_data = csv.reader(csv_sales)
    sales_header = next(csv_sales_data)
    
    # @TODO: Loop over every row in the sales list object
    # @TODO: Read in the sales data into the sales list
    for line in csv_sales_data:
        lst = []
        lst.append(line[0])     # line item
        lst.append(line[1])     # Date
        lst.append(line[2])     # cc_number
        lst.append(line[3])     # quantity
        lst.append(line[4])     # menu item

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
        sales.append(lst)

for idx in range(0, len(sales)):
# for idx in range(0, 50):
    item = sales[idx][4]
    count = int(sales[idx][3])
    price = item_details[sales[idx][4]]['price']
    cost = item_details[sales[idx][4]]['cost']
    # print(f"\n the {item} has a cost of {cost}, and a price of {price}")

    # @TODO: Cumulatively add up the metrics for each item key
    # @TODO: Calculate profit of each item in the menu data
    inv_report[item]['01-count'] += count
    inv_report[item]['02-revenue'] += count * price
    inv_report[item]['03-cogs'] += count * cost
    profit = count * (price - cost)
    inv_report[item]['04-profit'] += profit

# Initialize a row counter variable
row_count = 0

# @TODO:
# If the item value not in the report, add it as a new entry with initialized metrics
# Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

count = 0
for item in inv_report:
    if inv_report[item]['01-count'] != 0:
        count += 1
        print(f"\n the total count for {item} is {inv_report[item]['01-count']}")
        print(f" the total revenue is $ {inv_report[item]['02-revenue']:,.2f}")
        print(f" the total cost is $ {inv_report[item]['03-cogs']:,.2f}")
        print(f" the total profit is $ {inv_report[item]['04-profit']:,.2f}")

print(f" total number of products sold: {count}")

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    # Item,Category,Description,Price,Cost
    # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item

# @TODO: Print out matching menu data
print()
for item in inv_report:
    if inv_report[item]['01-count'] != 0:
        print(f"{item:^50} '01-count': {inv_report[item]['01-count']:,.2f}, '02-revenue': {inv_report[item]['02-revenue']:,.2f}, '03-cogs': {inv_report[item]['03-cogs']:,}, '04-profit': {inv_report[item]['04-profit']:,.2f}")

# @TODO: Print total number of records in sales data
print()
row_header = []
pt.field_names = ["item name", "01-count", "02-revenue", "03-cogs", "04-profit"]
for item in inv_report:
    if inv_report[item]['01-count'] != 0:
        pt.add_row([item, inv_report[item]['01-count'], inv_report[item]['02-revenue'], inv_report[item]['03-cogs'], inv_report[item]['04-profit']])
        row_header.append(item)

print(pt)

# @TODO: Create the data in the format to pass it to pandas to print a table
# Write out report to a text file (won't appear on the command line output)
#         print(f"print the data for pandas: {data}")
pd_data = []
headers = ["item name", "01-count", "02-revenue", "03-cogs", "04-profit"]
for item in inv_report :
    line = []
    if inv_report[item]['01-count'] != 0:
        line.append(item)
        line.append(inv_report[item]['01-count'])
        line.append(inv_report[item]['02-revenue'])
        line.append(inv_report[item]['03-cogs'])
        line.append(inv_report[item]['04-profit'])
        
        # print list per line to be added to pandas dictionary line
        # print(line)
        pd_data.append(line)
        # add a dictionary of each line to DataFrame input
        # dict_line = {f'{item}' : line}
        # data = (dict_line)
    
df_table = pandas.DataFrame(pd_data, row_header, headers)   # (pd_data, row_header)
print(df_table)

# @TODO: Write out report to a text file (won't appear on the command line output)
fw = open("PyRamen/Resources/PyRamen_report.txt", "w")

# @TODO: Print out matching menu data
for item in inv_report:
    if inv_report[item]['01-count'] != 0:
        fw.write(f"\n{item:^50} '01-count': {inv_report[item]['01-count']:,.2f}, '02-revenue': {inv_report[item]['02-revenue']:,.2f}, '03-cogs': {inv_report[item]['03-cogs']:,}, '04-profit': {inv_report[item]['04-profit']:,.2f}")
fw.write(f"\n")
fw.close()
