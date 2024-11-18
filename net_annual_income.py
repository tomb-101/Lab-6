def annual_net_income(gross_salary):
    # complete your function implementation here...
    net_salary=0
    if gross_salary>=45000:
        net_salary=gross_salary*0.5
    elif gross_salary<45000 and gross_salary>=30000:
        net_salary=gross_salary*0.7
    else:
        net_salary=gross_salary*0.85
    return net_salary

# print(annual_net_income(45000))