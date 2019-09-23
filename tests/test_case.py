import http.client
conn = http.client.HTTPConnection("laba1-db-heroku.herokuapp.com")

def case1():
 conn.request("GET", "/")
 r1 = conn.getresponse()
 print('Status Test 1: ',r1.status)
 data1 = r1.read()
 if data1 == b'Hello World':
    print('Test 1: status: Good')
 else:
     print('what')
 print('GET Test 2:',data1, '\n')


def case2():
 print('Введите название статьи:')
 a = input()
 print('Введите Имя автора:')
 b = input()
 print('Введите число публикации:')
 c = input()
 conn.request("GET", "/add?name="+a+"&author="+b+"&published="+c)
 r2 = conn.getresponse()
 print('Status Test 2: ',r2.status)
 data2 = r2.read()
 print('GET Test 2: ',data2, '\n')

def case3():
 conn.request("GET", "/getall")
 r2 = conn.getresponse()
 print('Status Test 3: ',r2.status)
 data2 = r2.read()
 print('GET Test 3: ',data2, '\n')

def case4():
 print('Введите номер id в базе данных:')
 a = input()
 conn.request("GET", "/get/"+a)
 r2 = conn.getresponse()
 print('Status Test 4: ',r2.status)
 data2 = r2.read()
 print('GET Test 4: ',data2, '\n')


case1()
case2()
case3()
case4()
conn.close()