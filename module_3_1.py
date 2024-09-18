calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return (calls)


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            return True
            break
        else:
            return False
            continue


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
