import matplotlib.pyplot as plot
import math

m = 0.995
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
fig, axs = plot.subplots(2)
axs[0].set_title("Синий - численный, ораньжевый - аналитич")
axs[1].set_title("Ошибка, y - метры, x - секунды")
plot.subplots_adjust(left= None, bottom= None,right= None, top= None, wspace= None, hspace= 0.367)
odd = 0
xSecondExsponent = [0,0]
tSecondExsponent = [0,0]

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


    print("g = " + str(1 + ((p * u0 * S * C) / m) * tDelta))
    if math.fabs(round(u0, -1)) == math.fabs(round(uArr[-2], -1)):
        print("x = ", xSecondExsponent[-1], "u = ", u0)

    xTrue = -(-330 - 68 * tNow + 476 * math.log(1 + math.e ** (0.287 * tNow)))
    xTrueArr.append(xTrue)
    errors.append(xSecondExsponent[-1] - xTrue)

axs[0].plot(tSecondExsponent, xSecondExsponent)
axs[0].plot(timeArr, xTrueArr)

axs[1].plot(timeArr, errors)
plot.show()
