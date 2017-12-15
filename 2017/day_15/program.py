a_fac = 16807
b_fac = 48271
div = 2147483647

#a_st = 65
#b_st = 8921
a_st = 116
b_st = 299

times = 40000000

count = 0
for _ in range(times):
    a_st = (a_st * a_fac) % div
    b_st = (b_st * b_fac) % div

    if a_st % 65536 == b_st % 65536:
	count += 1
print count

times = 5000000

a_list = []
b_list = []
count = 0
while len(a_list) <= times or len(b_list) <= times:
    a_st = (a_st * a_fac) % div
    b_st = (b_st * b_fac) % div

    if a_st % 4 == 0:
	a_list.append(a_st)
    if b_st % 8 == 0:
	b_list.append(b_st)

for index in range(times):
     if a_list[index] % 65536 == b_list[index] % 65536:
	 count += 1

print count
