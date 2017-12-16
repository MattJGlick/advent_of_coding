import json
data = json.load(open('input_file.txt'))

def get_count(to_check):
    total = 0
    if isinstance(to_check, int):
        return to_check
    if isinstance(to_check, str):
        return 0
    if isinstance(to_check, list):
        for check in to_check:
            total += get_count(check)
    if isinstance(to_check, dict):
        for key in to_check.keys():
            if "red" not in to_check.values():
                total += get_count(to_check[key])

    return total


print get_count(data)



