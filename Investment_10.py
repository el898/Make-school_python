investment= input("Input your investment amount :")
intrest = input("Your expected intrest :")
investment = float(investment)
intrest = float(intrest)* .01
for i in range(10):
  investment += (investment * intrest)
print("year {} the returns are {:.2f}".format(i, investment))