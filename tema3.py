def ordered_ints(list_of_objects: list):
    return_list= []
    for i in list_of_objects:
        if type(i)== tuple:
            return_list.append(len(i))
        else:
            return_list.append(int(i))
    return_list.sort(reverse=True)
    return return_list

print(ordered_ints([1, True, '123', False, 6, ()]))




def sum_of_squares_2(n):
    result = 0
    for n in range(1,n + 1):
        result = result + n**2
    return result
print(sum_of_squares_2(10))


def factorial_of_squares(n):
    result = 1
    for i in range(n):
        i += 1
        result *= i ** 2
    return result

print(factorial_of_squares(5))



text_str  = "(1,2,3) , (4,5,6) , (3,4,5)"

print(text_str)
print(type(text_str))

result = tuple(eval(text_str))
print(result)
print(type(result))

print("1 2 3,text". split())
print("text_de_t_de" . title())
print("text_de_t_de".upper())
print("text de t " . replace("text de t","Text_de_t"))

my_tuple = ("Text_de_t")
print(my_tuple)




