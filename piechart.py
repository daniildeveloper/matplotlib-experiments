import matplotlib.pyplot as plt

pieces = [5, 15, 7, 2]
colors = ['b', 'r', 'c', 'm']
owners = ["Dima", "Misha", "Vasya", "Irina"]

plt.pie(pieces,
    labels=owners,
    colors=colors,
    autopct="%1.1f%%",
    shadow=1,
    startangle=90,
    explode=(0, 0.1, 0, 0))
plt.title("Billing cake")

plt.show()
