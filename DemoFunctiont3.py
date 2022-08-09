# DemoFunctiont3.py
# 정의되지 않은 인자: 필수 + 옵션
def userURIBuilder(server, port, **user):
    strURL = "http://" + server +":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL
# 호출
print( userURIBuilder("test.com", "80", id="kin", name="mike") )
print( userURIBuilder("test.com", "80", id="kin", name="mike", age="30") )

#람다 함수
print("##람다함수##") 
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )

print( (lambda x:x*x)(3) )
print( globals() )