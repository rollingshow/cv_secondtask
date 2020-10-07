import matplotlib.pyplot as plt
import numpy as np


def recursion(B, i, j, l):

    B[i, j] = l
    if (B[i + 1, j] == 255):
        recursion(B, i + 1, j, l)
    if (B[i - 1, j] == 255):
        recursion(B, i - 1, j, l)
    if (B[i, j + 1] == 255):
        recursion(B, i, j + 1, l)
    if (B[i, j - 1] == 255):
        recursion(B, i, j - 1, l)

def recursion_labeling(B):
    labels = np.copy(B)  # Метки

    label = 1
    labels[labels != 0] = 255
    for row in range(B.shape[0]):
        for col in range(B.shape[1]):
            if labels[row, col] == 255:
                recursion(labels, row, col, label)
                label += 1

    return labels


if __name__ == "__main__":
    B = np.zeros((20, 20), dtype='int32')

    B[1:-1, -2] = 1

    B[1, 1:5] = 1
    B[1, 7:12] = 1
    B[2, 1:3] = 1
    B[2, 6:8] = 1
    B[3:4, 1:7] = 1

    B[7:11, 11] = 1
    B[7:11, 14] = 1
    B[10:15, 10:15] = 1

    B[5:10, 5] = 1
    B[5:10, 6] = 1

    LB = recursion_labeling(B)

    print("Labels - ", list(set(LB.ravel()))[1:])

    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.imshow(B)
    plt.colorbar(ticks=range(int(2)))
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(LB)
    plt.colorbar()
    plt.axis("off")
    plt.tight_layout()
    plt.show()