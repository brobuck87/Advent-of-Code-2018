import re 

# Open file
with open('./input.txt', 'r') as f:
    SYMBOL = '.'
    grid = []
    count = 0
    overlapping_id = set()
    # Create grid
    for x in range(1000):
        grid.append([])
        for y in range(1000):
            grid[x].append(SYMBOL)
 # Split the input text using Regex
    for line in f:
        regex_id = r'\d+'
        nums = re.findall(regex_id, line)
# Turn all pieces of regex into ints
        id, x, y, w, h = list(map(lambda num: int(num), nums))
# Add ids to set
        overlapping_id.add(id)
# Logic to replace "." with ids or 'x'
        for i in range(y, y+h):
            for j in range(x, x+w):
                if type(grid[i][j]) == int:
                    overlapping_id.discard(grid[i][j])
                    overlapping_id.discard(id)
                    grid[i][j] = 'X'
                    count += 1
                elif grid[i][j] == ".": 
                    grid[i][j] = id
                elif grid[i][j] == 'X':
                    overlapping_id.discard(id)
    print(count)
    print(overlapping_id.pop())