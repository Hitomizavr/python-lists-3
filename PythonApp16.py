# максимальная масса, которую может выдержать одна лодка
m = int(input());
# количество рыбаков
n = int(input());
a =[]
for _ in range(n):
    a.append(int(input()));

# вывести минимальное количество лодок, необходимых для переправки
print((2 * min(a) <= m) + len([x for x in a if x + min(a) > m]));
