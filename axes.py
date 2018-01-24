import matplotlib.pyplot as plt

x = [12, 4, 5, 8, 5, 6]
y = [8, 11, 9, 7, 3, 4]


plt.bar(x, y, label="first")

plt.xlabel("Burgers")
plt.ylabel("Dogs")

plt.title("Check it")

plt.legend()

plt.show()
