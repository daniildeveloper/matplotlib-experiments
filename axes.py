import matplotlib.pyplot as plt

x = [12, 4, 5]
y = [8, 11, 9]

y2 = [12, 4, 5]
x2 = [8, 11, 9]

plt.plot(x, y, label="first")
plt.plot(x2, y2, label="second")

plt.xlabel("Burgers")
plt.ylabel("Dogs")

plt.title("Check it")

plt.legend()

plt.show()
