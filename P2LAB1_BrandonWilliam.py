gas_mileage = float(input())
cost_of_gas = float(input())

total1 = 20 * (cost_of_gas / gas_mileage)
total2 = 75 * (cost_of_gas / gas_mileage)
total3 = 500 * (cost_of_gas / gas_mileage)
print(f'{total1:.2f} {total2:.2f} {total3:.2f}')