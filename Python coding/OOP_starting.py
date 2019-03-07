#define class
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' %(self.name,self.score))

#creat instanse
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

#export instanses' information(method)
bart.print_score()
lisa.print_score()