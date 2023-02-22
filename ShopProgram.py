import ShopClass as sc

customerJohn = sc.Customer(
    'John Doe', '123 Main St. Waco TX 76706', '214-555-1112')
print(
    f'Customer: {customerJohn.get_name()}   Address: {customerJohn.get_address()}   Phone: {customerJohn.get_phone()}')

carJohn = sc.Car('Honda', 'Accord LX', '2016')
print(
    f'Car Make: {carJohn.get_make()}   Car Model: {carJohn.get_model()}   Car Year: {carJohn.get_year()}')

quoteJohn1 = sc.ServiceQuote(1210.50, 765)
print('Service Quote')
print(f'Parts: ${quoteJohn1.get_parts_charges():,.2f}')
print(f'Labor: ${quoteJohn1.get_labor_charges():,.2f}')
print(
    f'Sales Tax: ${(quoteJohn1.get_sales_tax()*quoteJohn1.get_total_charges()):,.2f}')
print(
    f'Total Charges: ${quoteJohn1.get_total_charges()*(1+quoteJohn1.get_sales_tax()):,.2f}')
