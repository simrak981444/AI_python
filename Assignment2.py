import numpy as np
import matplotlib.pyplot as plt


height = np.array([60, 65, 70, 72, 69])  #  in inches
weight = np.array([150, 170, 180, 200, 160])  #  in pounds


height_cm = height * 2.54 #inches to cm
weight_kg = weight * 0.453592 #pounds to kilo


meanheight = np.mean(height_cm)
meanweight = np.mean(weight_kg)


print("mean Height (cm):", meanheight)
print("mean Weight (kg):",meanweight)


print("converted Data:")
print(f"heights (in cm):" ,height_cm)
print(f"weights (in kg):", weight_kg)


plt.plot(height_cm, weight_kg ,color='blue', marker='o', linestyle='-', label='Height (cm) Histogram')
plt.xlabel('height (cm)')
plt.ylabel('frequency')
plt.title('histogram of Heights in Cm')
plt.grid()
plt.show()











import matplotlib.pyplot as plt
import numpy as np
x =np.array([7,8,9])
y=np.array([2,6,4])
vertical=np.vstack((x,y))
print(vertical)

horizontal=np.hstack((x,y))
print(horizontal)
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a=a.reshape(4,3)
n,m= np.shape(a)
print(a)
for i in range(n):
    for j in range(m):
        print("element", i,j, "is", a[i,j])



