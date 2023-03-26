

# if __name__ == '__main__':
#     n = int(input())
#     print(n)
#     integer_list = map(int, input().split())
#     print(integer_list)
#     print((hash(tuple(integer_list))))
#
# #We need to convert our list of ints to a tuple of ints (as a list is not hashable, but a tuple is)
#
# numbers = raw_input().strip().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# T = tuple(numbers)
# print hash(T)


def swap_case(s):
    output = ""
    for i in s:
        if str(i).islower():
            output = output + str(i).upper()
        elif str(i).isupper():
            output = output + str(i).lower()
        else :
            output = output + str(i)

    return output


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


    def mutate_string(string, position, character):
        str2 = list(string)
        str2[position] = character
        string = ''.join(str2)
        return string