import md5

code = "abbhdwsy"

num = 0
output = ""
output_2 = list("--------")

while len(output) != 8 or "-" in output_2:
    full_string = code + str(num)
    cur_hash = md5.new(full_string).hexdigest()

    if cur_hash[:5] == "00000":
        first = cur_hash[5]
        if len(output) != 8:
            output += first

        second = cur_hash[6]
        if first.isdigit() and int(first) in range(8):
            first = int(first)
            if output_2[first] == "-":
                output_2[first] = second

    num += 1

print output
print ''.join(output_2)

