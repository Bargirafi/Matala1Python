# Bar Girafi - 316582758
###############Q1

def my_func(x1,x2,x3):
        if x1+x2+x3 == 0 :
            return "Not a number – denominator equals zero"   
        listi = [x1,x2,x3]
        for i in listi:
            if type(i) != float :
                return "Error: parameters should be float"
        calculate = ((x2+x3)*x3)
        return calculate
    
print(my_func(5.3,3.0,7.4))






