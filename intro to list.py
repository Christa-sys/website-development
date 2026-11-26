empty_list = []
print(empty_list)
new_list = [1,2,3,4,5]
print(new_list)
triples = [1,2,3] * 3
print(triples)
odd_list = [9,8,7,6,5,4,3,2,1] 
print(odd_list[::-1]) 

activity_list = [2,3,7,4,5,6,1,10,9,8]
print(activity_list)
count = 0
for i in activity_list:
    count += i
print(count)

average = count / len(activity_list)
print(average)

sorted_list = sorted(activity_list)
print(sorted_list)

activity_list.sort()
print(activity_list)

smallest = min(activity_list)
print(smallest)
largest = max(activity_list)
print(largest)

smallest_index = activity_list[0]
print(smallest_index)