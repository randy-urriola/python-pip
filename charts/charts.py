import matplotlib.pyplot as plt


def pie():
    labels = ['A', 'B', 'C']
    values = [100, 47, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
