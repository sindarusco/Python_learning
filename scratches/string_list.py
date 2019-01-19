text = input("input string: ")
L = len(text)
m = int(0.5 * L)
# print(L)
# print(m)

for i in range(m):
    j = L - i - 1
    # print(i)
    # print(j)
if text[i] == text[j]:
    print("palindrome")
else:
    print("not palindrome")