inputSet = {0}
starting_freq = 0

def check_frequency(num):
    if num in inputSet:
        return True
    inputSet.add(num)

def find_repeated_freq(freq):
    with open('input.txt', 'r') as f:
        for num in f:
            freq += int(num)
            if check_frequency(freq) == True:
                print(freq)
                return
        find_repeated_freq(freq)

find_repeated_freq(starting_freq)