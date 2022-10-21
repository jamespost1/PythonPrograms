# CSCI 220/620
# Summer 2022
# Assignment 6 - Graphs and Graph Algorithms
# James Post
import math
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import texttable as tt


def read_graph(file_name):
    with open(file_name) as file:
        a = []
        for line in file.readlines():
            s = line.split(" ")
            row = []
            for num in s:
                row.append(int(num))
            a.append(row)
        return a


def print_adj_matrix(a):
    print("   ", end="")
    for j in range(len(a)):
        print(str(j) + " ", end="")
    print()
    for i in range(len(a)):
        row = a[i]
        print(str(i) + ": ", end="")
        for col in row:
            print(str(col) + " ", end="")
        print()
    print()


def convert_to_adj_table(a):
    t = []
    for row in a:
        l = []
        for j in range(len(row)):
            if row[j] == 1:
                l.append(j)
        t.append(l)
    return t


def print_adj_table(t):
    for i in range(len(t)):
        l = t[i]
        print(str(i) + ": ", end="")
        for v in l:
            print(str(v) + " ", end="")
        print()
    print()


def print_graph_info(a):
    is_symmetric = True
    is_complete = True
    is_connected = True
    vertices = len(a)
    edges = 0
    headers = ["Vertex", "In-degree", "Out-degree", "Neighbors"]
    data = []
    data.append(headers)
    for i in range(len(a)):
        data_row = []
        data_row.append(i) # vertex
        indegree = 0
        for k in range(len(a)):
            if a[k][i] == 1:
                indegree += 1
        data_row.append(indegree)
        row = a[i]
        outdegree = 0
        neighbours = ""
        for j in range(len(row)):
            if row[j] == 1:
                outdegree += 1
                edges += 1
                neighbours += str(j) + " "
        is_symmetric = is_symmetric and indegree == outdegree
        is_complete = is_complete and indegree == outdegree == (vertices - 1)
        is_connected = is_connected and outdegree > 0
        data_row.append(outdegree)
        data_row.append(neighbours)
        data.append(data_row)
    tbl = tt.Texttable(100)
    tbl.set_cols_align(["l", "r", "r", "l"])
    tbl.add_rows(data, header=True)
    print(tbl.draw())
    if is_symmetric:
        edges //= 2
    has_euler_circuit = is_symmetric
    for j in range(1, len(data)):
        has_euler_circuit = has_euler_circuit and data[j][2] % 2 == 0
    print("Vertices:", vertices, "Edges:", edges)
    print("Symmetric:", is_symmetric)
    print("Eulerian Circuit:", has_euler_circuit)
    print("Complete: ", is_complete)
    print("Connected: ", is_connected)


def plot_times(dict_sorts, sorts, trials, sizes):
    sort_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for sort_alg in sorts:
        sort_num += 1
        d = dict_sorts[sort_alg.__name__]
        x_axis = [j + .05 * sort_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]  # time
        plt.bar(x_axis, y_axis, width=.05, alpha=.75, label=sort_alg.__name__)
    plt.legend()
    plt.title("Runtime of Sorting Algorithms")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time for " + str(trials) + " trials (ms)")
    plt.savefig("Assignment5.png")
    plt.show()


def main():
    files = ["graph1.txt", "graph2.txt", "graph3.txt"]
    for file in files:
        a = read_graph(file)
        t = convert_to_adj_table(a)
        print(file)
        print_adj_matrix(a)
        print_adj_table(t)
        print_graph_info(a)
        print()


if __name__ == "__main__":
    main()
