import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plotlines(vertices):
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]
    for edge in edges:
        plt.plot(vertices[0, edge], vertices[1, edge], vertices[2, edge], 'k')

def main():
    x = np.array(list(map(float, input("Please input the center of the cube(e.g. 1,1,1): ").split(','))))
    d = float(input("Please input the half length of the edge of the cube: "))

    projection = np.eye(4)
    projection[3, 3] = 0
    projection[3, 2] = 1

    x = np.append(x, 1)

    vertices = x[:3].reshape(3, 1) + d * np.array([
        [-1, -1, -1, -1, 1, 1, 1, 1],
        [-1, -1, 1, 1, -1, -1, 1, 1],
        [-1, 1, 1, -1, -1, 1, 1, -1]
    ])
    vertices = np.vstack((vertices, np.ones((1, 8))))
    proj = np.dot(projection, vertices)
    proj = proj[:3, :] / proj[3, :]

    p = max(abs(x[0] + d), abs(x[1] + d))
    p1 = np.arange(-p, p + 1)
    X, Y = np.meshgrid(p1, p1)
    Z = np.ones_like(X)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.5)

    ax.plot([0], [0], [0], 'r*', linewidth=4)
    plotlines(vertices)

    plotlines(proj)

    for i in range(8):
        ax.plot([vertices[0, i], proj[0, i]],  # x 坐标从顶点到投影点
                [vertices[1, i], proj[1, i]],  # y 坐标从顶点到投影点
                [vertices[2, i], proj[2, i]],  # z 坐标从顶点到投影点
                'b--', linewidth=1)           # 蓝色虚线，线宽为 1


    ax.set_xticks(np.arange(-p, p + 1, 1))  # 设置 x 轴刻度，每隔 1
    ax.set_yticks(np.arange(-p, p + 1, 1))  # 设置 y 轴刻度，每隔 1
    ax.set_zticks(np.arange(-p, p + 1, 1))   # 设置 z 轴刻度，每隔 1

    ax.set_box_aspect([1, 1, 1])  # x, y, z 的物理比例一致


    plt.show()

main()