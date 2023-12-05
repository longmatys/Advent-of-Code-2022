import os
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            #print(line)
            marker = 14
            for i in range(len(line)-marker-1):
                a= set(line[i:i+marker])
                if len(set(line[i:i+marker]))==marker:
                    print(f'Nasel jsem diff na {i}.pozici, odpoved je {i+marker}')
                    break
if __name__ == '__main__':
    main()