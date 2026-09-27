
def calculate_bill(customer_name, quantity, unit_price):
  total_bill = quantity*unit_price
  customer_bill = customer_name + ", your total bill is: " + str(total_bill) + "taka"
  return customer_bill

name = input("your name please: ")
quantity = float(input("enter your qty: "))
unit_price = float(input("enter unit price: "))
bill = calculate_bill(name, quantity, unit_price)

# every input you give using input() function, the input is stored as texts/strings (str) / লিখা
# to convert text to number, we use a function from python. that function is
# float(the_text_you_want_to_convert)
# str(the_number_you_want_to_convert_to_text)

print(bill)
if 5 > 2:
  print("Yes")



def calculate_bill(customer_name, quantity, unit_price):
  total_bill = quantity*unit_price
  customer_bill = customer_name + ", your total bill is: " + str(total_bill) + "taka"
  return customer_bill


# str(the_number_you_want_to_convert_to_text)

print(bill)


