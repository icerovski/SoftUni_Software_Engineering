'''
You will receive 2 lines of input. On the first line, you will receive a single string of integers, separated by a comma and a space ", ".
On the second line, you will receive a count of beggars.
Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last number in the list.

For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5], the second one collects [2, 4].
The same list with 3 beggars would produce a better outcome for the second beggar: 5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].

Also, note that not all beggars have to take the same amount of "offers", meaning that the length of the list is not necessarily a multiple of n. The list length could be even shorter - i.e., the last beggars will take nothing (0).
'''

def recursive_sum(start, step, accumulated_sum):
    if start + step < len(money_list):
        accumulated_sum += money_list[start + step]
        return recursive_sum(start + step, step, accumulated_sum)
    return accumulated_sum

money_list = list(map(int, input().split(', ')))
count = int(input())

# Solution 01, Time: 0.05s
profit_list = []
for beggar in range(count):
    profit = 0
    if beggar < len(money_list):
        first_profit = money_list[beggar]
        profit = recursive_sum(beggar, count, first_profit)
    profit_list.append(profit)
print(profit_list)

# Solution 02, Time: 0.08s
profit_list_02 = []
for beggar in range(count):
    middle_list = money_list[beggar::count]
    profit_list_02.append(sum(middle_list))

print(profit_list_02)