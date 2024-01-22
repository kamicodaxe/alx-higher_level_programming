#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        div_result = 0
        try:
            div_result = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("division by zero")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(div_result)

    return result
