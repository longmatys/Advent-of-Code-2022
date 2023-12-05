import os
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            #print(line)
            for i in range(len(line)-3):
                a= set(line[i:i+4])
                if len(set(line[i:i+4]))==4:
                    print(f'Nasel jsem diff na {i}.pozici, odpoved je {i+4}')
                    break
if __name__ == '__main__':
    main()