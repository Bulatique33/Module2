def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')


    test1 = inner_function()
    print(test1)

test2 = test_function()
print(test2)
test3 = inner_function()
print(test3)