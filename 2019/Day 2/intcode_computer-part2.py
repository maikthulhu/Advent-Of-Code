import sys

def process_intcode(intcode):
    intcode_len = len(intcode)

    x = 0
    while x <= intcode_len:
        try:
            # OPCODE 1 - Add
            if intcode[x] == 1:
                intcode[intcode[x+3]] = intcode[intcode[x+1]] + intcode[intcode[x+2]]
            # OPCODE 2 - Multiply
            elif intcode[x] == 2:
                intcode[intcode[x+3]] = intcode[intcode[x+1]] * intcode[intcode[x+2]]
            # OPCODE 99 - DIE
            elif intcode[x] == 99:
                return intcode
            #else:
                #raise Exception
            # Move the cursor forward 4
            x += 4
        except Exception:
            pass

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

    intcode = get_intcode_from_file(sys.argv[1])

    # Brute force this thing until you find the factors of the magic number below
    while True:
        # Set up a working copy
        for x in range(99):
            for y in range(99):
                # wi = listcode is a reference, use list() to create a new list
                wi = list(intcode)
                wi[1] = x
                wi[2] = y
                wi = process_intcode(wi)
                if wi[0] == 19690720:
                    print(f"[+] Eureka: {x}, {y}")
                    return
                else:
                    print(99*x + y)
                
if __name__ == '__main__':
    main()