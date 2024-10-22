## Inputs we need from the user
# Total Rent
# Total food ordered for snacking
#Electricity units spend
#Charge per Unit
#persons living rent in room/flat
def main():
    Rent = int(input("Enter The Rent : "))
    food = int(input("Enter the amount of food ordered : "))
    electricity_spend = int(input("Enter the total of electricity spend : "))
    charge_per_unit = int(input("Enter the charger per unit in your area : "))
    total_electricity_bill = electricity_spend*charge_per_unit
    persons = int(input("Enter The person living in room/flat : "))
    total_bill = food+total_electricity_bill+Rent
    one_person_share = total_bill/persons
    print(f"Total Bill is {total_bill}")
    print(f"Each Person Will Pay : {one_person_share}")
main()