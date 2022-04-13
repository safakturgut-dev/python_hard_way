# Ex 19 study
def bill_detail(base_cost, extra_text, extra_minute):
    tax = (base_cost + extra_text + extra_minute) * 5 / 100
    print(f"The base cost for your phone bill is ${base_cost}.")
    print(
        f'If you use more text message then your plan has, each costs ${extra_text}.')
    print(f'Extra minute charge is ${extra_minute}.')
    print(f'Tax will be 5% of entire bill which is ${tax:.2f}')


bill_detail(15.00, 0.25, 0.50)
