""" all below strings should get passed
123
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
1aaaaaaa1aaaaaaaa1aaaaaaaaa
qA2
#$%@^&*
#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000

"""
s = "qA2"
alpha = False
alnum = False
digit = False
lower = False
upper = False

for i in s:
    if i.isupper():
        upper = True
    elif i.islower():
        lower = True
    elif i.isdigit():
        digit = True

for i in s:
    if i.isalnum():
        alnum = True

for i in s:
    if i.isalpha():
        alpha = True

if alnum:
    print("True")
else:
    print("False")

if alpha:
    print("True")
else:
    print("False")

if digit:
    print("True")
else:
    print("False")

if lower:
    print("True")
else:
    print("False")

if upper:
    print("True")
else:
    print("False")

# Another Solution, use of any

print(any(map(str.isalnum, s)))
print(any(map(str.isalpha, s)))
print(any(map(str.isdigit, s)))
print(any(map(str.islower, s)))
print(any(map(str.isupper, s)))

print(any(a.isalnum() for a in s))
print(any(a.isalpha() for a in s))
print(any(a.isdigit() for a in s))
print(any(a.islower() for a in s))
print(any(a.isupper() for a in s))

