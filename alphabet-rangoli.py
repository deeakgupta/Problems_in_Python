import string
alpha = string.ascii_lowercase
L=[]
def print_rangoli(n):
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3,'-'))
    print('\n'.join(L[:0:-1]+L))
print_rangoli(5)

'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''