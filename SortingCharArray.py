'''
Sample 1) Input:-
abcabcbacabc

Output:-
aaaabbbbcccc

2) Input:-
xyzxxyyxxzzzxyzzz

Output:-
xxxxxxyyyyzzzzzzz
'''
def sort(array, l):
    item_1=min(l)
    item_3=max(l)
    l.remove(item_1)
    item_2=min(l)
    a=b=c=0
    for i in array:
        if i == item_1:
            a += 1
        elif i == item_2:
            b += 1
        else:
            c += 1
    return a*item_1 + b*item_2  + c*item_3

input_str = input()
l=set(input_str)
print(sort(list(input_str), l))