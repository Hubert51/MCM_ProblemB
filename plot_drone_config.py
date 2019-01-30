import matplotlib.pyplot as plt
import numpy as np

VOLUMN_B = 19800
VOLUMN_C = 90000
VOLUMN_F = 40000


def plot_hist(data, tick_label, label, color, x_label, y_label, title):
    x = list(range(len(data[0])))

    total_width, n = 0.8, len(data)
    width = total_width / n
    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(3) * 4)

    plt.bar(x, data[0], width=width, label=label[0],tick_label=tick_label, fc=color[0])
    for i in range(len(x)):
        x[i] = x[i] + width

    for index in range(1,len(data)):

        plt.bar(x, data[index], width=width, label=label[index],  fc=color[index])
        for i in range(len(x)):
            x[i] = x[i] + width


    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def plot_hist_old(file_name, ratio, title):
    f = open(file_name, "r")
    lines = f.read().strip().split("\n")
    print(len(lines))
    outer_list = []
    for line in lines:
        middle_list = [0,0,0,0]
        containers = line.split('\t')
        for container in containers:
            # inner_list = [0,0,0,0]
            drones = list(container)
            for drone in drones:
                if drone == "B":
                    middle_list[0] += 1
                if drone == "C":
                    middle_list[1] += 1
                if drone == "F":
                    middle_list[2] += 1
                if drone == "A":
                    middle_list[3] += 1
            # middle_list.append(inner_list)
        outer_list.append(middle_list)

    print(outer_list)
    data_list = [ [], [], [], [] ]
    for list1 in outer_list:
        data_list[0].append(list1[0])
        data_list[1].append(list1[1])
        data_list[2].append(list1[2])
        data_list[3].append(list1[3])
    print(data_list)


    x = list(range(len(data_list[0])))
    print( x )


    name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
    num_list = data_list[0]
    num_list1 = data_list[1]
    num_list2 = data_list[2]
    num_list3 = data_list[3]

    x = list(range(len(num_list)))
    x_label = list(range(len(num_list)+1))
    for i in range(len(x_label)):
        x_label[i] = x_label[i] * ratio;
    x_label.remove(0)
    total_width, n = 1, 4
    width = total_width / n
    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(3) * 4)

    plt.bar(x, num_list, width=width, label='Drone B', fc="c")
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, num_list1, width=width, label='Drone C',tick_label=x_label, fc="orange")
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, num_list2, width=width, label='Drone F', fc="m")

    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, num_list3, width=width, label='Drone A', fc="chartreuse")
    plt.legend()
    plt.xlabel("Maintenance day")
    plt.ylabel("Number of Drones")
    plt.title(title)
    plt.show()


def plot_one_day_hist(file_name, title):
    f = open( file_name, "r")
    line = f.read().strip().split("\n")[-1]
    line = line.split("\t")
    for index in range(len(line)):
        line[index] = line[index].strip()

    number_c = [0,0,0]
    number_f = [0,0,0]
    number_b = [0,0,0]

    volumn = [0,0,0]
    for index in range(len(line)):
        number_c[index] += line[index].count("C")
        number_f[index] += line[index].count("F")
        number_b[index] += line[index].count("B")

    for index in range(len(line)):
        volumn[index] = (number_c[index] * VOLUMN_C + number_f[index] * VOLUMN_F + number_b[index] * VOLUMN_B) / 50000
    print(volumn)
    plot_hist( [number_c, number_b, number_f, volumn], ["container1", "container2", "container3"],
               label=[ "Drone C", "Drone B", "Drone F", 'Total Volumn' ], color=["c", "chartreuse", "m","orange" ],
               x_label="The number of different kind of drones in each containers", y_label="The number of drone",
               title=title)






if __name__ == '__main__':
    file_name = "k3_data_v3.txt"
    plot_hist_old(file_name, ratio=4, title="K3: V3 Distribution")
    plot_one_day_hist(file_name, "K3(V3): The number and volumn of drone in each container")