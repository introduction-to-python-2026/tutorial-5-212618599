# Q: Write an import statement that imports the function pyplot from the module matplotlib and renames it to plt.

def build_histogram(data):
    my_dic ={}
    for i in data:
        if i in my_dic :
            my_dic[i]+=1
        else:
            my_dic[i]=1
    return my_dic

def plot_histogram(histogram):
    import matplotlib.pyplot as plt
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


