# from numpy import * 
# from pylab import *
# x=linspace(-3,3,30)
# y=x**2
# plot(x,y)
# show()

# pylab module
# from numpy import *
# from pylab import *
# x = linspace(-3, 3, 30)
# y = x**2
# plot(x, y)
# show()

# subplots function
# import matplotlib.pyplot as plt
# x=[12,23,34]
# y1=[23,33,45]
# y2=[12,26,67]
# y3=[1,2,3]
# y4=[6,7,8]
# fig,axes=plt.subplots(2,2,figsize=(10,8))
# axes[0,0].plot(x,y1)
# axes[0,0].set_title('first row first column ')
# axes[0,1].plot(x,y2)
# axes[0,1].set_title('first row sec col')
# axes[1,0].plot(x,y3)
# axes[1,0].set_title('sec row first col')
# axes[1,1].set_title('sec row sec col')
# plt.tight_layout()
# plt.show()


# BAR plot
# import matplotlib.pyplot as plt
# x=['wheat','gram','rice','pulse']
# y=[2000,3000,1500,5000]
# plt.xlabel("food items")
# plt.ylabel('production')
# plt.title("food production in india")
# plt.barh(x,y)
# plt.show()


# barchat without legend
# import matplotlib.pyplot as plt
# year=['2020','2021','2022','2023','2024']
# percentages=[80,85,88,92,95]
# colors=['royalblue','black','green','yellow','red']
# plt.bar(year,percentages,color=colors)
# plt.xlabel('year')
# plt.ylabel('percentage of students')
# plt.title('percentage of students  last five years')
# plt.show()

# histogram 

# import matplotlib.pyplot as plt
# exam_scores = [68, 74, 82, 79, 92, 85, 66, 77, 44, 22]
# plt.hist(exam_scores, bins=4, edgecolor='k', alpha=0.7)
# plt.title('Exam Scores Histogram')
# plt.xlabel('Score Range')
# plt.ylabel('Frequency')
# plt.grid(True)
# # plt.grid(False) #no grid
# plt.show()


# line plot

# Line Plot एक प्रकार का graph होता है, जिसमें अलग-अलग data points को lines के द्वारा जोड़ा जाता है। इसका उपयोग data में होने वाले changes और trends को समझने के लिए किया जाता है।
# Line Plot का उपयोग क्यों करते हैं?
# 1. समय के अनुसार बदलाव देखने के लिए।
# 2. Sales में वृद्धि या कमी देखने के लिए।
# 3. Temperature में बदलाव देखने के लिए।
# 4. किसी data के trend को समझने के लिए।
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
plt.plot(x, y, marker='o', color='blue', label='Sales')
plt.title('Line Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.grid(True)
plt.show()
