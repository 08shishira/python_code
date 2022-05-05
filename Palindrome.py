#Method-1

def pali(s):
    return s == s[::-1]

s = "malayalam"
ans = pali(s)
if ans:
    print("Yes")
else:
    print("No")

#Method-2
# def pali(s):
#     rev = "".join(reversed(s))
#     if s == rev:
#         return True
#     return False
# s = "shishira"
# result = pali(s)
# print(result)

#Method-3
# s = "shishira"
# rev = ""
# for i in s:
#     rev = i+rev
#
# if s == rev:
#     print("Yes")
# else:
#     print("No")
