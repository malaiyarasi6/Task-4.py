class myClass:
    a = 33;
    def __privMeth(self):
        print("i'm inside class myclass")
    def hello(self):
        print("private variable value:",myClass.a)
foo = myClass()
foo.hello()
foo.a
