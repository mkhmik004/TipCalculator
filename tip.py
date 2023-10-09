#MKHABELE MMM
#28/06/2023
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent #conversion
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d[1::])#removes the currency
def percent_to_float(p):
    p=p[:-1]#removes the percentage sign
    return float(p)/100
main()
