max = 4000000
switch = True
fibSum = 2
x = 1
y = 1
z = 2

while switch:
    x = y + z
    y = z + x
    z = x + y

    if z > max:
        switch = False
    else:
        fibSum += z

print fibSum
