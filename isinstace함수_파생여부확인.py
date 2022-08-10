class Person: # class Person(object) 동일, object 클래스가 기본적으로 들어가기 때문에 생략
    pass
class Bird:
    pass
class Student(Person): #Person을 Student가 상속
    pass
p, s = Person(), Student()

print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))