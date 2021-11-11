import matplotlib.pyplot as plt
import numpy as np


def U_I():
    I = [12.55, 10.8, 9.15, 8.18, 7.52, 6.75, 6.23, 5.82, 5.38, 5.09, 4.78, 4.54, 4.2, 4.04, 3.88]
    U = [0.001, 1.47, 2.77, 3, 3.58, 3.96, 4.28, 4.57, 4.86, 5.16, 5.33, 5.5, 5.64, 5.78, 5.88]

    # Построение графика
    plt.title("График зависимости U(I)")  # заголовок
    plt.xlabel("I, мА")  # ось абсцисс
    plt.ylabel("U, В")  # ось ординат
    plt.grid()  # включение отображения сетки
    plt.scatter(I, U)
    plt.text(2, 4, 'U=-0,655I + 8.44', style='italic', fontsize=10,
             bbox={'facecolor': 'grey', 'alpha': 0.5, 'pad': 10})
    plt.xlim(xmin=0)

    theta = np.polyfit(I, U, deg=1)
    model = np.poly1d(theta)

    # plt.plot(x, y, 'ro')
    plt.plot(I, model(I), color='orange')

    plt.show()  # построение графика
    coefs, res, _, _, _ = a = np.polyfit(I, U, 1, full=True)
    print(coefs, res)


def P_I():
    I = [12.55, 10.8, 9.15, 8.18, 7.52, 6.75, 6.23, 5.82, 5.38, 5.09, 4.78, 4.54, 4.2, 4.04, 3.88]
    PR = [0.01, 15.88, 25.35, 24.54, 26.92, 26.73, 26.66, 26.60, 26.15, 26.26, 25.48, 24.97, 23.69, 23.35, 22.81]
    PS = [110.25, 81.65, 58.61, 46.84, 39.59, 31.89, 27.17, 23.71, 20.26, 18.14, 15.99, 14.43, 12.35, 11.43, 10.54]
    P = [110.31, 94.93, 80.43, 71.9, 66.1, 59.33, 54.76, 51.16, 47.29, 44.74, 42.02, 39.91, 36.92, 35.51, 34.11]

    coefs, res, _, _, _ = np.polyfit(I, PR, 2, full=True)
    print(coefs, res)
    coefs, res, _, _, _ = np.polyfit(I, PS, 2, full=True)
    print(coefs, res)
    coefs, res, _, _, _ = np.polyfit(I, P, 2, full=True)
    print(coefs, res)
    # Построение графика
    plt.title("График зависимости P(I)")  # заголовок
    plt.xlabel("I, мА")  # ось абсцисс
    plt.ylabel("P, мВт")  # ось ординат
    plt.grid()  # включение отображения сетки
    plt.scatter(I, PR)
    plt.scatter(I, PS)
    plt.scatter(I, P)
    plt.xlim(xmin=0)

    beginning = np.array([3, 2.5, 2, 1.56, 0.73, 0])
    beginningPR = np.array([22.74, 22.46, 16.13, 11.59, 1.1, 0])
    beginningPS = np.array([11.74, 3.01, 3.56, 0.57, 0.01, 0])
    beginningP = np.array([32.99, 31.91, 20.8, 9, 0.1, 0])

    I = np.hstack((I,beginning))
    PR=np.hstack((PR,beginningPR))
    PS = np.hstack((PS, beginningPS))
    P = np.hstack((P, beginningP))

    theta = np.polyfit(I, PR, deg=2)
    model = np.poly1d(theta)

    # plt.plot(x, y, 'ro')
    plt.plot(I, model(I), color='orange')

    theta = np.polyfit(I, PS, deg=2)
    model = np.poly1d(theta)

    # plt.plot(x, y, 'ro')
    plt.plot(I, model(I), color='orange')

    theta = np.polyfit(I, P, deg=2)
    model = np.poly1d(theta)

    # plt.plot(x, y, 'ro')
    plt.plot(I, model(I), color='orange')

    plt.show()  # построение графика



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    P_I()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
