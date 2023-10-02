import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string

fig = plt.figure(figsize=(16,9))
#ex1
# ax1 = fig.add_subplot(111)
#
# x_measured = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y_measured = [0, 2, 5, 16, 18, 22, 35, 47, 110, 220]
#
# ax1.scatter(x_measured, y_measured, marker='x')
#
# ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')
#
# x = np.linspace(0, 10)
# ax1.plot(x, np.exp(x)/40)
#
# ax1.grid()
# plt.show()

#ex 2
#
# ax1 = fig.add_subplot(311)
# ax2 = fig.add_subplot(312)
# ax3 = fig.add_subplot(313)
# pos = 0
#
# scale = 10
#
# size1 = 1000
# size2 = 100000
# size3 = 10000000
#
# values1 = np.random.normal(pos, scale, size1)
# values2 = np.random.normal(pos, scale, size2)
# values3 = np.random.normal(pos, scale, size3)
#
# ax1.hist(values1, 1000)
# ax2.hist(values2, 1000)
# ax3.hist(values3, 1000)
#
# plt.show()
#ex 3
# ax1 = fig.add_subplot(211)
# ax2 = fig.add_subplot(212)
#
#
# article_read = pd.read_csv('iris_data.csv', delimiter=',')
# species_list = article_read['Species'].to_list()
# setosa = 0
# virginica = 0
# versicolor = 0
#
# for i in species_list:
#     if i == 'Iris-setosa':
#         setosa += 1
#     elif i == 'Iris-virginica':
#         virginica += 1
#     elif i == 'Iris-versicolor':
#         versicolor += 1
#
# setosa = setosa/len(species_list)
# virginica = virginica/len(species_list)
# versicolor = versicolor/len(species_list)
# ax1.pie([setosa, virginica, versicolor], labels = ['Setosa', 'Virginica', 'Versicolor'])
#
# more_15 = 0
# litl_12 = 0
# more_12_litl_15 = 0
# length_petal_list = article_read['PetalLengthCm'].to_list()
# for i in length_petal_list:
#     if i <= 1.2:
#         litl_12 += 1
#     elif 1.2 < i <= 1.5:
#         more_12_litl_15 += 1
#     else:
#         more_15 += 1
# more_15 = more_15/len(length_petal_list)
# litl_12 = litl_12/len(length_petal_list)
# more_12_litl_15 = more_12_litl_15/len(length_petal_list)
# ax2.pie([litl_12, more_12_litl_15, more_15], labels = ['<1.2','>1.2 and <1.5', '>1.5'])
#
#
# plt.show()

#ex 4

# article_read = pd.read_csv('iris_data.csv', delimiter=',')
# length_sepal_list = article_read['SepalLengthCm'].to_list()
# width_sepal_list = article_read['SepalWidthCm'].to_list()
# length_petal_list = article_read['PetalLengthCm'].to_list()
# width_petal_list = article_read['PetalWidthCm'].to_list()
# SIZE = len(length_petal_list)
#
# ax1 = fig.add_subplot(211)
# ax2 = fig.add_subplot(212)
#
# ax1.scatter(length_sepal_list, width_sepal_list)
# ax2.scatter(length_petal_list, width_petal_list)
#
# x1 = [4, 8]
# y1 = np.interp(x1, length_sepal_list, width_sepal_list)
# x2 = [1, 7]
# y2 = np.interp(x2, length_petal_list, width_petal_list)
#
# ax1.plot(x1, y1)
# ax2.plot(x2, y2)
#
# plt.show()

#ex 5

# article_read = pd.read_csv('BTC_data.csv', delimiter=',')
# time_list = article_read['time'].to_list()
# close_list = article_read['close'].to_list()
# for i in range(len(time_list)):
#     time_list[i] = str(time_list[i])[:10]
# time_list_int = [0] * len(time_list)
# ax = fig.add_subplot(111)
# plt.plot(time_list, close_list)
# locator = matplotlib.ticker.MaxNLocator()
# ax.xaxis.set_major_locator(locator)
# ax.grid()
# plt.show()


#ex 6
# article_read = pd.read_csv('BTC_data.csv', delimiter=',')
# ax = fig.add_subplot(111)
# time_list = article_read['time'].to_list()
# close_list = article_read['close'].to_list()
# x = [i for i in range(len(time_list))]
# n = 1
# coeff = np.polyfit(x, close_list, deg=n)
# y = [0] * len(x)
# for i in range(len(x)):
#     for j in range(n+1):
#         y[i] += coeff[len(coeff)-1 - j] * x[i] ** j
# ax.plot(time_list, close_list)
# ax.plot(x, y)
#
#
# plt.show()

#ex 7
# d = {}
# with open('text.txt') as f:
#     text = f.readlines()
# " ".join(text)
# text_string = str(text)
# for i in string.punctuation:
#     text_string = text_string.replace(i, ' ')
# text_string = text_string.replace("\\n", ' ')
# text_string = text_string.replace(" n ", ' ')
# text_string = text_string.lower()
# text_list = text_string.split(' ')
# text_list = list(filter(None, text_list))
#
# for i in text_list:
#     if i not in d:
#         d[i] = 0
#     else:
#         d[i] +=1
# sorted_d = sorted(d.items(), key=lambda x:x[1])
# for i in range(10):
#     print(sorted_d[len(sorted_d) - i - 1])

#ex 8
# A = {1, 4, 5, 7, 8, 9, 11, 16, 17, 22, 105, 1516}
# B = {5, 234, 35, 234, 4, 17, 1415, 105}
# print(A-B | B-A)
# print(A | B)
# print(A & B)
