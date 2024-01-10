import calendar
import csv
from datetime import datetime
from dateutil import relativedelta

def solve_contract_payment_type(payment_type_text):
    if payment_type_text == 'ANNUAL':
        return 12
    elif payment_type_text == 'HALF_ANNUAL':
        return 6
    elif payment_type_text == 'QUARTER':
        return 3
    elif payment_type_text == 'MONTHLY':
        return 1

def solve_working_days(input_date, jump_days):
    jump_days = int(jump_days)
    input_date = input_date + relativedelta.relativedelta(days=jump_days)
    if input_date.weekday() in [4, 5]:
        # if the day is fri or sat then find the nearest sunday
        input_date = input_date + relativedelta.relativedelta(weekday=calendar.SUNDAY)
    return input_date

def solve_installments_count(contract_end_date, contract_start_date, jump_months):
    # calc no. of installments :  months between end date and start date / jump_months
    differ = relativedelta.relativedelta(contract_end_date, contract_start_date)
    total_months_between = differ.years * 12 + differ.months
    installments_count = total_months_between / jump_months
    return installments_count

def solve_install_pay_each(contract_total_payment, deposit_value, installments_count):

    if deposit_value != '':
        deposit_value = float(deposit_value)
    else:
        deposit_value = 0
    install_payment_each = (float(contract_total_payment) - deposit_value) / installments_count
    return install_payment_each


contracts_list = []
# Read data from contracts.csv into contracts_list
with open('C:\\MY_FILES\\project\\Contracts.csv', 'r') as read_from_file:
    reader = csv.reader(read_from_file)
    reader.__next__()
    for row in reader:
        contracts_list.append(row)

# Loop over contracts_list
for contract in contracts_list:
    print(contract)
    contract_id, contract_start_date, contract_end_date, contract_total_payment, deposit_value\
        , client_name, contract_payment_type, max_grace_period = contract
    output_file_name = contract_id+'-'+client_name+' - installments'+'.csv'
    with open('C:\\MY_FILES\\project\\solution\\'+output_file_name, 'w', newline='') as write_to_file:
        writer = csv.writer(write_to_file)
        writer.writerow(['Installment Serial', 'Installment Date', 'Installment Amount', 'Max Grace Date'])
        jump_months = solve_contract_payment_type(contract_payment_type) #  Annual, Quarter ...
        contract_start_date = datetime.strptime(contract_start_date, '%d/%m/%Y')  #  : contract start date
        contract_end_date = datetime.strptime(contract_end_date, '%d/%m/%Y') #  : contract end date
        installments_count = solve_installments_count(contract_end_date, contract_start_date, jump_months)
        install_pay_each = solve_install_pay_each(contract_total_payment, deposit_value, installments_count)
        installment_date = contract_start_date
        sheet_serial = 1
        while True: # installments Loop
            max_grace_date = solve_working_days(installment_date, max_grace_period)
            writer.writerow([sheet_serial, installment_date.date(),
                             install_pay_each, max_grace_date.date()])
            sheet_serial = sheet_serial + 1
            installment_date = installment_date + relativedelta.relativedelta(months=jump_months)
            if installment_date >= contract_end_date:
                break   # exit installments Loop
