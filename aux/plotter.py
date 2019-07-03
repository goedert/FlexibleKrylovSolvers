import matplotlib.pyplot as plt

def plotter(x,y,x_label,y_label,filename):

    plt.plot(y,x)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(filename)
