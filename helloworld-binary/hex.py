from sys import argv

def write_binary(filename, newFileBytes):
    fout = open(filename, 'wb')
    fout.write((''.join(chr(i) for i in newFileBytes)).encode('charmap'))

def main(fin, fout):
    new_bytes = []
    prev = None
    with open(fin, 'r') as file:
        for line in file:
            for c in line:
                if c == '#': break
                if c.isspace(): continue
                if prev == None: prev = c
                else:
                    new_bytes.append(int(c + prev, 16))
                    prev = None
    if prev != None:
        print('uneven number of hex characters in file')
        exit(-1)
    write_binary(fout, new_bytes)

"""
write hex string to binary file
input: filename ending in .hex
"""
if __name__ == '__main__':
    fin = argv[1]
    assert fin.endswith('.hex')
    fout = fin[:-4]
    main(fin, fout)
