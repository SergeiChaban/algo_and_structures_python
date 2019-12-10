"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib

#
# h = hashlib.sha1(b'password')
# print(h)
#

# h_2 = hashlib.sha1()
# h_2.update(b'password')
# print(h_2)
#
# h_3 = hashlib.sha1(b'password')
# print(h_3.hexdigest())
# print(h_3.digest())
#
# h_4 = hashlib.md5(b'password')
# p = h_4.hexdigest()
# print(p)
#
# h_5 = hashlib.pbkdf2_hmac('sha512', b'123456', b'654321', 10000)
# print(h_5)


s = input('Введите строку (маленькие латинские буквы)')
r = set()

n = len(s)
for i in range(n):
    if i == 0:
        n = len(s) - 1
    else:
        n = len(s)
    for j in range(n, i, -1):
        print(s[i:j])
        r.add(hashlib.sha1(s[i:j].encode('UTF-8')).hexdigest())
print(r)
print(s, len(r))