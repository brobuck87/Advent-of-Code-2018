def find_repeated_chars():
    with open('input.txt', 'r') as f:
        twice = 0
        thrice = 0
        for line in f:
            chars = {}
            for c in line:
                if c in chars.keys():
                    chars[c] = chars[c] + 1
                else: 
                    chars[c] = 1
            if 2 in chars.values():
                twice += 1
            if 3 in chars.values():
                thrice +=1
            # print (chars)
        print (twice * thrice)
            
find_repeated_chars()