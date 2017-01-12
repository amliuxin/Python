from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# from sklearn.cluster import KMeans


def heat_visualization(data, ax, ay, resolution):
    minx, maxx, miny, maxy = get_range(data)
    lx = maxx - minx
    ly = maxy - miny
    img = []
    for i in np.linspace(minx - 0.1 * lx, maxx + 0.1 * lx,
                         lx * 1.2 / resolution + 1):
        r = []
        for j in np.linspace(maxy + 0.1 * ly, miny - 0.1 * ly,
                             ly * 1.2 / resolution + 1):
            r.append(get_heat(data, i, j, ax, ay))
        img.append(r)
    plt.imshow(np.array(img).T)
    plt.show()


def get_range(data):
    minx = data[0][0]
    maxx = data[0][0]
    miny = data[0][1]
    maxy = data[0][1]
    for dt in data:
        if dt[0] < minx:
            minx = dt[0]
        if dt[0] > maxx:
            maxx = dt[0]
        if dt[1] < miny:
            miny = dt[1]
        if dt[1] > maxy:
            maxy = dt[1]
    return [minx, maxx, miny, maxy]


def get_heat(data, x, y, ax, ay):
    heat = 0
    for dt in data:
        heat += np.exp(-((x - dt[0]) / ax)**2 / 2 - ((y - dt[1]) / ay)**2 / 2)
    return heat


def loadDataset(infile):
    df = pd.read_csv(infile, sep='\t', header=0, dtype=str, na_filter=False)
    return np.array(df).astype(np.float)

if __name__ == '__main__':
    d = [[0, 0], [1, 1], [0, 0.3], [0.1, 0], [1, 1.3], [1, 0.5], [0.5, 0.5]]
    data = loadDataset(r"testSet.txt")
    # y_pred = KMeans(n_clusters=4).fit_predict(data)
    # plt.scatter(data[:, 0], data[:, 1], c=y_pred)
    # plt.show()
    heat_visualization(data, 0.2, 0.2, 0.01)
