import matplotlib.pyplot as plot
import math

m = 0.01 * 12 ** 1/3 #Возведение в степь 1/3 номера 12
p = 1.2
g = 9.81
C = 0.5
S = 0.0070
u0 = 0.5
tNow = 0.0
x = 0
alpha = 0
flaw = 0.0

print("Введите максимальное время:")
tMax = float(input())
tDelta = 0.1
timeArr = []
xArr = [0,0]
xTrueArr = []
uArr = [0,0]

errors = []
odd = 0
xSecondExsponent = [0,0]
tSecondExsponent = [0,0]
derivativeFuncWithUArr = [0,0]

while tNow < tMax:
    a = -g + p * u0 * u0 * S * C / (2 * m)
    u0 += a * tDelta
    x = u0 * tDelta + a * tDelta * tDelta / 2
    tNow += tDelta
    uArr.append(u0)

    xArr.append(x)
    timeArr.append(tNow)

    xSecondExsponent.append(xSecondExsponent[-1] + (xArr[-1] + xArr[-2]) / 2)
    tSecondExsponent.append(tNow)

    derivativeFuncWithUArr.append((p * u0 * S * C) / m)

    print("g = " + str((1 + (derivativeFuncWithUArr[-2]) * tDelta / 2) /
                       (1 - (derivativeFuncWithUArr[-1]) * tDelta / 2)))
    if math.fabs(round(u0, -3)) == math.fabs(round(uArr[-2], -3)):
        print("x = ", xSecondExsponent[-1], "u = ", u0)

plot.xlabel("Время, с")
plot.ylabel("Расстояние, м")
plot.plot(tSecondExsponent, xSecondExsponent)

plot.show()
