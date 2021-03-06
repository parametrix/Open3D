# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

import numpy as np
from py3d import *

if __name__ == "__main__":

    print("Load two aligned point clouds.")
    pcd0 = read_point_cloud("../../TestData/Feature/cloud_bin_0.pcd")
    pcd1 = read_point_cloud("../../TestData/Feature/cloud_bin_1.pcd")
    pcd0.paint_uniform_color([1, 0.706, 0])
    pcd1.paint_uniform_color([0, 0.651, 0.929])
    draw_geometries([pcd0, pcd1])
    print("Load their FPFH feature and evaluate.")
    print("Black : matching distance > 0.2")
    print("White : matching distance = 0")
    feature0 = read_feature("../../TestData/Feature/cloud_bin_0.fpfh.bin")
    feature1 = read_feature("../../TestData/Feature/cloud_bin_1.fpfh.bin")
    fpfh_tree = KDTreeFlann(feature1)
    for i in range(len(pcd0.points)):
        [_, idx, _] = fpfh_tree.search_knn_vector_xd(feature0.data[:, i], 1)
        dis = np.linalg.norm(pcd0.points[i] - pcd1.points[idx[0]])
        c = (0.2 - np.fmin(dis, 0.2)) / 0.2
        pcd0.colors[i] = [c, c, c]
    draw_geometries([pcd0])
    print("")

    print("Load their L32D feature and evaluate.")
    print("Black : matching distance > 0.2")
    print("White : matching distance = 0")
    feature0 = read_feature("../../TestData/Feature/cloud_bin_0.d32.bin")
    feature1 = read_feature("../../TestData/Feature/cloud_bin_1.d32.bin")
    fpfh_tree = KDTreeFlann(feature1)
    for i in range(len(pcd0.points)):
        [_, idx, _] = fpfh_tree.search_knn_vector_xd(feature0.data[:, i], 1)
        dis = np.linalg.norm(pcd0.points[i] - pcd1.points[idx[0]])
        c = (0.2 - np.fmin(dis, 0.2)) / 0.2
        pcd0.colors[i] = [c, c, c]
    draw_geometries([pcd0])
    print("")
