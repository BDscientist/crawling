import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#차이점 이해!!!! self 에 대한 이해!!!
class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        #print(id(self))
        print("function2 called!")


f = SelfTest()
print(dir(f))
#self에 대한 개념 이해!!
#f.function1()
print(id(f))
f.function2()
#2234937229096    2234937229096  똑같음
