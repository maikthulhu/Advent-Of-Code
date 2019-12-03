import sys

def process_intcode(intcode):
    intcode_len = len(intcode)

    x = 0
    while x <= intcode_len:
        # OPCODE 1 - Add
        if intcode[x] == 1:
            intcode[intcode[x+3]] = intcode[intcode[x+1]] + intcode[intcode[x+2]]
        # OPCODE 2 - Multiply
        elif intcode[x] == 2:
            intcode[intcode[x+3]] = intcode[intcode[x+1]] * intcode[intcode[x+2]]
        # OPCODE 99 - DIE
        elif intcode[x] == 99:
            return intcode
        else:
            raise Exception
        # Move the cursor forward 4
        x += 4

    raise Exception

def get_intcode_from_file(intcode_file_path):
    intcode = []
    with open(intcode_file_path) as f:
        #intcode = f.read().split(',')
        intcode = [int(x) if x.isdigit() else x for x in f.read().split(',')]
    
    return intcode

def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <intcode_input>")
        return -1

    # Remember day2pt1 says to replace position 1 with 12 and position 2 with 2 (ie. 1202)
    intcode = get_intcode_from_file(sys.argv[1])

    print(process_intcode(intcode))

if __name__ == '__main__':
    main()