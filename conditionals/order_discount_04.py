item_cost = 500.0
item_qty = 3
special_client = 1 # 1 = special | 0 not special
total_order_cost = item_cost * item_qty

if total_order_cost >= 1000:

    # nested if condition
    if special_client == 1:
        discount_pct = 20
    elif special_client == 0:
        discount_pct = 10

discount_val = total_order_cost * discount_pct / 100
print(f'Total Order Cost \
       \n\tBefore Discount = {total_order_cost}')
total_order_cost = total_order_cost - discount_val
print(f'Total Order Cost After Discount = {total_order_cost}')

print(f'Discount Pct = {discount_pct}');
print(f'Discount Val = {discount_val}');
