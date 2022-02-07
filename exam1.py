import matplotlib.pyplot as plt

x= [38,62,18,75,38,59,66,92,52,75,48]
y= [74,44,85,19,88,69,50,33,29,32,56]
plt.scatter(x,y)
plt.xlabel('maths marks')
plt.ylabel('english marks')
plt.legend(['x=maths  y=english'])
plt.title("scatter graph")
plt.scatter(x,y,color='blue', marker= '*', label='Standard Normal')
plt.scatter(x,y,color= 'red', marker='v', label='Chi-Square')
plt.show()