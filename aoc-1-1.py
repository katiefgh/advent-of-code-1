f = open("input.txt")

input_d = f.read().splitlines()

frequency = 0

count = {0:1}

while count[frequency]==1:
    for i in input_d:
        for o in i:
            if o == i[0]:
                if o == '+':
                    frequency += int(i[1:])
                    if frequency in count:
                        count[frequency] += 1
                        if count[frequency] == 2:
                            print(frequency)
                            break
                    else:
                        count[frequency] = 1
                else:
                    frequency -= int(i[1:])
                    if frequency in count:
                        count[frequency] += 1
                        if count[frequency] == 2:
                            print(frequency)
                            break
                    else:
                        count[frequency] = 1
            else:
                continue


