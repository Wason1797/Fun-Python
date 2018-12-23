def sum_five(a,e,i,o,u):
    return a+e+i+o+u
cases = int(input())
input_arr = []
for i in range(cases):
    input_arr.append(input())
    
sub_dict = {}
result_arr = []
for word in input_arr:
    count = 0
    _len= len(word)
    for i in range (_len):
        for j in range(i, _len):
            new_word = word[i:j+1]
            if new_word in sub_dict:
                count += sub_dict[new_word]
            else:
                current_count = sum_five(*map(new_word.count, "aeiou"))
                count+= current_count
                sub_dict.update({new_word: current_count})
    result_arr.append(str(count))

print("\n".join(result_arr))