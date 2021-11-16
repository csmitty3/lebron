from matplotlib import pyplot as plt
points = [25, 21, 8, 7, 23, 17, 17, 18, 10, 22, 14, 28, 19, 15, 15, 6, 33, 19, 4, 8, 18, 23, 37, 27, 17, 36, 32, 22, 34, 18, 32, 22, 14, 14, 21, 19, 16, 27, 29, 29, 16, 27, 20, 38, 12, 32, 14, 14, 24, 9, 16, 32, 22, 21, 11, 30, 18, 24, 19, 24, 34, 14, 26, 17, 14, 15, 25, 16, 41, 18, 28, 20, 34, 21, 14, 24, 10, 27, 17]
results = ["L", "L", "L", "L", "L", "W", "W", "L", "L", "W", "W", "L", "L", "L", "L", "L", "L", "L", "L", "W", "L", "W", "L", "L", "L", "W", "W", "W", "L", "L", "W", "L", "L", "W", "L", "L", "L", "W", "L", "W", "W", "W", "L", "W", "W", "L", "L", "L", "W", "L", "L", "W", "W", "W", "L", "W", "L", "W", "W", "W", "W", "W", "W", "W", "L", "L", "L", "L", "W", "L", "L", "L", "L", "L", "L", "L", "W", "W", "W"]
gamenum = []
for i in range(79):
    gamenum.append(i + 1)
totalpoints = []
for i in range(len(points)):
    if i > 0:
        totalpoints.append(points[i] + totalpoints[i-1])
    else:
        totalpoints.append(points[i])
    i += 1
combined = zip(totalpoints, gamenum)
ppg = [x/y for (x, y) in combined]
wins = []
wincount = 0
losses = []
losscount = 0
for i in range(len(results)):
    if results[i] == "W":
        wincount += 1
    else:
        losscount += 1
    wins.append(wincount)
    losses.append(losscount)
    i += 1

plt.plot(gamenum, points, marker = "*")
plt.plot(gamenum, ppg, color = "black")
plt.plot(gamenum, wins)
plt.plot(gamenum, losses)
plt.show()