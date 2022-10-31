input_array = []
with open('input.txt', 'r') as f:
    for box_id in f:
        input_array.append(box_id.rstrip('\n'))
# print (input_array)

def find_shared_letters(str1, str2):
    final_string = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            final_string += str1[i]
    return final_string

def check_for_mismatch(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            box_id1 = arr[i]
            box_id2 = arr[j]
            mismatched_chars = 0
            for k in range(len(box_id1)):
                if box_id1[k] != box_id2[k]:
                    mismatched_chars += 1
            if mismatched_chars == 1:
                return find_shared_letters(box_id1, box_id2)

print(check_for_mismatch(input_array))

        