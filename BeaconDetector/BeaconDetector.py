import re

def man_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

file = open('input.txt')

sensors = dict()
maxY = 4_000_000
for line in file:
    sensor_x, sensor_y, beacon_x, beacon_y = re.match("^Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)", line.strip()).groups()
    sensors[(int(sensor_x), int(sensor_y))] = (int(beacon_x), int(beacon_y))

for y in range(0, maxY):
    if y % 10_000 == 0:
        print(y)
    ranges = []
    for sensor in sensors.keys():
        dist = man_dist(sensor, sensors[sensor])
        ycomp = abs(sensor[1] - y)
        if ycomp > dist:
            continue
        ranges.append((max(0, sensor[0] - (dist - ycomp)), min(sensor[0] + (dist - ycomp), maxY)))
    ranges.sort()
    compressed = []
    buildOn = ranges[0]
    for range in ranges[1:]:
        if buildOn[1] + 1 < range[0]:
            compressed.append(buildOn)
            buildOn = range
        elif buildOn[1] + 1 >= range[0] and buildOn[1] <= range[1]:
            buildOn = (buildOn[0], range[1])
    if len(compressed) == 2:
        x = compressed[1][0] - 1
        print(4_000_000 * x + y)
        break