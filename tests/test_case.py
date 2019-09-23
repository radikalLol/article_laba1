import http.client
conn = http.client.HTTPConnection("localhost:5000")

def case1():
 conn.request("GET", "/")
 r1 = conn.getresponse()
 print('Status Test 1: ',r1.status)
 data1 = r1.read()
 print('GET Test 1:',data1, '\n')


def case2():
 conn.request("GET", "/add?name=test&author=test&published=01.01.2010")
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
 conn.request("GET", "/get/4")
 r2 = conn.getresponse()
 print('Status Test 4: ',r2.status)
 data2 = r2.read()
 print('GET Test 4: ',data2, '\n')


case1()
case2()
case3()
case4()
conn.close()