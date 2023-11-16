#Practical 1: Gradient Descent Algorithm

def gradient_descent_fun(start,grad_fun,no_of_iteration,learning_rate):
    s=[start]
    x=start
    for i in range(no_of_iteration):
        step_size=learning_rate*grad_fun(x)
        #grad_fun(x) computes the derivative of value-x
        
        x=x-step_size
        s.append(x)
    
    return s,x,learning_rate

def gradient_function(x):
    return (8*x)

s,x,lr=gradient_descent_fun(3,gradient_function,100,0.01)

print(s)
print(x)
print(lr)
