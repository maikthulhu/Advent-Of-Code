from math import floor
import sys

def get_values_from_file(path):
    values = []
    with open(path) as f:
        for line in f:
            values.append(int(line))
    
    return values

def caclulate_fuel_requirements(mass_list):
    fuel_required = 0

    # Safely calculate module fuel requirement sum
    for v in mass_list:
        module_fuel_calculated = floor(v / 3) - 2
        # "Recursively" calculate additional fuel required based on calculated fuel mass until mass not > 0
        while module_fuel_calculated > 0:
            fuel_required += module_fuel_calculated
            module_fuel_calculated = floor(module_fuel_calculated / 3) - 2
    
    return fuel_required

def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <list_of_masses.txt>")
        return(-1)

    mass_list = get_values_from_file(sys.argv[1])
    fuel_required = caclulate_fuel_requirements(mass_list)

    print(f"This trip will require: {fuel_required} units of fuel.")

if __name__ == '__main__':
    main()