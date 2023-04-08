#que 8
class Triangle:
    def _init_(self,x,y,z):
        self.s1=x
        self.s2=y
        self.s3=z
    def area(self):
        s=(self.s1+self.s2+self.s3)/2
        print((s*(s-self.s1)*(s-self.s2)*(s-self.s3))**(1/2))
    def peri(self):
        print(self.s1+self.s2+self.s3)
t1=Triangle(3,4,5)
t1.area()
t1.peri()
