# Furniture Store Catalog System Project - 12 Apr 22
# Loveseat Description
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
#Loveseat Cost
lovely_loveseat_price = float(254.00)
# Stylish Settee Description
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
# Stylish Settee Price using Float because of Decimal
stylish_settee_price = float(180.50)
# Luxurious Lamp Description
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = float(52.15)
# Sales Tax for Store - 8.8 %
sales_tax = float(0.088)
#
### Customer 1
customer_one_total = int(0)
customer_one_itemization = ""
customer_one_total += (lovely_loveseat_price * 1)
print (customer_one_total)
customer_one_itemization += (lovely_loveseat_description)
print (customer_one_itemization)
customer_one_total += (luxurious_lamp_price)
print (customer_one_total)
customer_one_itemization += (luxurious_lamp_description)
print (customer_one_itemization)
customer_one_tax = (customer_one_total * sales_tax)
print ("Sales Tax:" , customer_one_tax)
customer_one_total += (customer_one_tax)

print ("")
print ("Customer Total including Tax:","$",customer_one_total)

#Customer Receipt
print ("****Customer Sales Receipt****")
print ("Item Description")
print ("Customer One Items")
print (customer_one_itemization)
print ("Customer One Total:")
print ("$" , customer_one_total)

