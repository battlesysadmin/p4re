hrs = raw_input("Enter Hours: ")
h = float(hrs)
pay = raw_input("Enter Pay: ")
p = float(pay)
ot = p * 1.5
if h <= 40:
    print h * p
else:
    reg_p = p * 40
    ot_hours = h - 40
    ot_p = ot_hours * ot
    print ot_p + reg_p
