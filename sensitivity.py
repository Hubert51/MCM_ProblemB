import matplotlib.pyplot as plt

if __name__ == '__main__':
    f = open("sensitivity.txt", "r")
    lines = f.read().strip().split("\n")
    x = [14]
    y = [1]
    for line in lines:
        x.append( int( line.split(" ")[-1].strip() ) )
        temp = line.strip().split()[-2]
        y.append( float (temp.strip() ) )

    initalize = 0.71
    for i in range(5):
        x.append(0)
        y.append(initalize)
        initalize -= 0.01
    for index in range(len(x)):
        x[index] = x[index] * 3
    plt.plot(y, x)
    plt.xlabel("$\gamma$")
    plt.ylabel("Maintenance day")
    plt.title("The relationship between $\gamma$ and maintenance day" )
    plt.show()


    print(y)