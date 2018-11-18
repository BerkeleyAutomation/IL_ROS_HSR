# Tentative Results

On commit 10f24d8034379d4c0a977ab881db5f53baceb913 with ssldata2, here is a
sample output, from running:

```
(py2-torch) seita@hermes1:~/IL_ROS_HSR/src/il_ros_hsr/nets$ python train_action_predictor.py  --holdout
```

I get:

```
Saving in: /nfs/diskstation/seita/bedmake_ssl/resnet18_2018-11-17-12-22_000

Now training!! On device: cuda:0
data_sizes: {'train': 159.0, 'valid': 40.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5441
loss_pos:    0.1752
loss_ang:    1.3689
correct_ang: 0.3145
  (valid)
loss total:  1.4220
loss_pos:    0.0586
loss_ang:    1.3633
correct_ang: 0.2750
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3369
loss_pos:    0.0506
loss_ang:    1.2864
correct_ang: 0.4088
  (valid)
loss total:  1.4075
loss_pos:    0.1182
loss_ang:    1.2893
correct_ang: 0.4000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.2157
loss_pos:    0.0284
loss_ang:    1.1873
correct_ang: 0.4969
  (valid)
loss total:  1.2505
loss_pos:    0.0381
loss_ang:    1.2124
correct_ang: 0.4250
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0968
loss_pos:    0.0244
loss_ang:    1.0723
correct_ang: 0.5597
  (valid)
loss total:  1.1498
loss_pos:    0.0285
loss_ang:    1.1212
correct_ang: 0.5250
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.9324
loss_pos:    0.0190
loss_ang:    0.9134
correct_ang: 0.7296
  (valid)
loss total:  0.9952
loss_pos:    0.0251
loss_ang:    0.9701
correct_ang: 0.7250
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.7830
loss_pos:    0.0157
loss_ang:    0.7673
correct_ang: 0.8050
  (valid)
loss total:  0.8489
loss_pos:    0.0287
loss_ang:    0.8203
correct_ang: 0.7750
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.6389
loss_pos:    0.0140
loss_ang:    0.6249
correct_ang: 0.8868
  (valid)
loss total:  0.6947
loss_pos:    0.0223
loss_ang:    0.6724
correct_ang: 0.8750
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.5090
loss_pos:    0.0124
loss_ang:    0.4966
correct_ang: 0.9245
  (valid)
loss total:  0.5268
loss_pos:    0.0109
loss_ang:    0.5159
correct_ang: 0.9250
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.3432
loss_pos:    0.0117
loss_ang:    0.3315
correct_ang: 0.9748
  (valid)
loss total:  0.4535
loss_pos:    0.0094
loss_ang:    0.4440
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.2738
loss_pos:    0.0092
loss_ang:    0.2646
correct_ang: 0.9623
  (valid)
loss total:  0.3735
loss_pos:    0.0120
loss_ang:    0.3615
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.1793
loss_pos:    0.0084
loss_ang:    0.1709
correct_ang: 0.9874
  (valid)
loss total:  0.2826
loss_pos:    0.0137
loss_ang:    0.2688
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.1667
loss_pos:    0.0089
loss_ang:    0.1578
correct_ang: 0.9811
  (valid)
loss total:  0.2030
loss_pos:    0.0082
loss_ang:    0.1947
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0944
loss_pos:    0.0066
loss_ang:    0.0878
correct_ang: 1.0000
  (valid)
loss total:  0.2039
loss_pos:    0.0067
loss_ang:    0.1972
correct_ang: 0.9250
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0744
loss_pos:    0.0083
loss_ang:    0.0661
correct_ang: 0.9874
  (valid)
loss total:  0.1911
loss_pos:    0.0095
loss_ang:    0.1817
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0570
loss_pos:    0.0052
loss_ang:    0.0518
correct_ang: 0.9937
  (valid)
loss total:  0.1989
loss_pos:    0.0131
loss_ang:    0.1858
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0366
loss_pos:    0.0052
loss_ang:    0.0314
correct_ang: 0.9937
  (valid)
loss total:  0.1871
loss_pos:    0.0104
loss_ang:    0.1768
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0337
loss_pos:    0.0067
loss_ang:    0.0270
correct_ang: 1.0000
  (valid)
loss total:  0.1728
loss_pos:    0.0073
loss_ang:    0.1655
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0416
loss_pos:    0.0050
loss_ang:    0.0366
correct_ang: 1.0000
  (valid)
loss total:  0.1430
loss_pos:    0.0082
loss_ang:    0.1349
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0233
loss_pos:    0.0062
loss_ang:    0.0171
correct_ang: 1.0000
  (valid)
loss total:  0.1141
loss_pos:    0.0052
loss_ang:    0.1089
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0146
loss_pos:    0.0046
loss_ang:    0.0100
correct_ang: 1.0000
  (valid)
loss total:  0.1043
loss_pos:    0.0064
loss_ang:    0.0980
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0182
loss_pos:    0.0051
loss_ang:    0.0131
correct_ang: 1.0000
  (valid)
loss total:  0.0963
loss_pos:    0.0079
loss_ang:    0.0884
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0143
loss_pos:    0.0047
loss_ang:    0.0096
correct_ang: 1.0000
  (valid)
loss total:  0.0941
loss_pos:    0.0047
loss_ang:    0.0894
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0110
loss_pos:    0.0035
loss_ang:    0.0075
correct_ang: 1.0000
  (valid)
loss total:  0.0938
loss_pos:    0.0058
loss_ang:    0.0880
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0093
loss_pos:    0.0030
loss_ang:    0.0063
correct_ang: 1.0000
  (valid)
loss total:  0.0925
loss_pos:    0.0052
loss_ang:    0.0873
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0095
loss_pos:    0.0033
loss_ang:    0.0061
correct_ang: 1.0000
  (valid)
loss total:  0.0967
loss_pos:    0.0054
loss_ang:    0.0913
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0110
loss_pos:    0.0032
loss_ang:    0.0079
correct_ang: 1.0000
  (valid)
loss total:  0.0937
loss_pos:    0.0047
loss_ang:    0.0889
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0157
loss_pos:    0.0041
loss_ang:    0.0117
correct_ang: 0.9937
  (valid)
loss total:  0.1220
loss_pos:    0.0050
loss_ang:    0.1170
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0100
loss_pos:    0.0032
loss_ang:    0.0068
correct_ang: 1.0000
  (valid)
loss total:  0.1449
loss_pos:    0.0062
loss_ang:    0.1387
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0090
loss_pos:    0.0035
loss_ang:    0.0055
correct_ang: 1.0000
  (valid)
loss total:  0.1595
loss_pos:    0.0055
loss_ang:    0.1540
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0097
loss_pos:    0.0038
loss_ang:    0.0059
correct_ang: 1.0000
  (valid)
loss total:  0.1486
loss_pos:    0.0054
loss_ang:    0.1433
correct_ang: 0.9500
------------------------------

Trained in 0m 48s
Best validation epoch total loss:  0.092516
  train:
[1.54411, 1.33691, 1.21575, 1.09675, 0.93239, 0.78298, 0.63891, 0.50903, 0.34322, 0.27378, 0.17928, 0.1667, 0.09438, 0.07436, 0.05695, 0.03664, 0.03372, 0.0416, 0.02333, 0.0146, 0.01824, 0.01431, 0.01104, 0.00927, 0.00946, 0.01103, 0.01572, 0.00997, 0.00896, 0.00973]
  valid:
[1.42195, 1.40751, 1.2505, 1.14976, 0.99522, 0.84893, 0.69469, 0.52685, 0.45346, 0.37351, 0.28256, 0.20299, 0.2039, 0.19115, 0.19886, 0.18712, 0.17282, 0.14304, 0.11411, 0.10434, 0.0963, 0.09405, 0.09381, 0.09252, 0.09673, 0.09367, 0.12197, 0.14487, 0.15948, 0.14864]

Visualizing performance of best model on validation set:
  31 / 32 angle accuracy for this mb
  8 / 8 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/

Done! Look at this directory for results:
/nfs/diskstation/seita/bedmake_ssl/resnet18_2018-11-17-12-22_000
```

With cross validation (the default option), we get significantly more verbose output:
```
(py27) ryanhoque@triton3:~/IL_ROS_HSR/src/il_ros_hsr/nets$ python train_action_predictor.py
```

```
Saving in: /nfs/diskstation/seita/bedmake_ssl/resnet18_2018-11-18-13-43_000
Fold #0

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.4897
loss_pos:    0.1223
loss_ang:    1.3674
correct_ang: 0.3017
  (valid)
loss total:  1.3546
loss_pos:    0.0376
loss_ang:    1.3170
correct_ang: 0.4000
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3503
loss_pos:    0.0583
loss_ang:    1.2921
correct_ang: 0.3408
  (valid)
loss total:  1.2996
loss_pos:    0.0367
loss_ang:    1.2629
correct_ang: 0.4000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.2037
loss_pos:    0.0257
loss_ang:    1.1780
correct_ang: 0.5642
  (valid)
loss total:  1.2124
loss_pos:    0.0288
loss_ang:    1.1835
correct_ang: 0.5500
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0524
loss_pos:    0.0235
loss_ang:    1.0289
correct_ang: 0.7207
  (valid)
loss total:  1.0672
loss_pos:    0.0090
loss_ang:    1.0583
correct_ang: 0.6000
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8416
loss_pos:    0.0166
loss_ang:    0.8250
correct_ang: 0.8492
  (valid)
loss total:  0.9152
loss_pos:    0.0143
loss_ang:    0.9009
correct_ang: 0.7000
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6814
loss_pos:    0.0127
loss_ang:    0.6686
correct_ang: 0.8883
  (valid)
loss total:  0.7645
loss_pos:    0.0140
loss_ang:    0.7505
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.5055
loss_pos:    0.0124
loss_ang:    0.4932
correct_ang: 0.9441
  (valid)
loss total:  0.6112
loss_pos:    0.0148
loss_ang:    0.5964
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3563
loss_pos:    0.0112
loss_ang:    0.3451
correct_ang: 0.9721
  (valid)
loss total:  0.4831
loss_pos:    0.0077
loss_ang:    0.4753
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2624
loss_pos:    0.0106
loss_ang:    0.2518
correct_ang: 0.9609
  (valid)
loss total:  0.3875
loss_pos:    0.0129
loss_ang:    0.3746
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1616
loss_pos:    0.0112
loss_ang:    0.1503
correct_ang: 0.9777
  (valid)
loss total:  0.2852
loss_pos:    0.0070
loss_ang:    0.2783
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.1161
loss_pos:    0.0085
loss_ang:    0.1076
correct_ang: 0.9888
  (valid)
loss total:  0.2271
loss_pos:    0.0089
loss_ang:    0.2182
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0875
loss_pos:    0.0078
loss_ang:    0.0797
correct_ang: 0.9888
  (valid)
loss total:  0.2143
loss_pos:    0.0160
loss_ang:    0.1983
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0615
loss_pos:    0.0061
loss_ang:    0.0554
correct_ang: 0.9888
  (valid)
loss total:  0.1916
loss_pos:    0.0085
loss_ang:    0.1831
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0450
loss_pos:    0.0074
loss_ang:    0.0376
correct_ang: 0.9944
  (valid)
loss total:  0.2057
loss_pos:    0.0094
loss_ang:    0.1963
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0337
loss_pos:    0.0077
loss_ang:    0.0260
correct_ang: 1.0000
  (valid)
loss total:  0.1553
loss_pos:    0.0066
loss_ang:    0.1487
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0275
loss_pos:    0.0042
loss_ang:    0.0233
correct_ang: 1.0000
  (valid)
loss total:  0.1201
loss_pos:    0.0085
loss_ang:    0.1116
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0245
loss_pos:    0.0045
loss_ang:    0.0201
correct_ang: 1.0000
  (valid)
loss total:  0.1210
loss_pos:    0.0062
loss_ang:    0.1149
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0253
loss_pos:    0.0051
loss_ang:    0.0203
correct_ang: 1.0000
  (valid)
loss total:  0.1103
loss_pos:    0.0058
loss_ang:    0.1044
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0159
loss_pos:    0.0060
loss_ang:    0.0099
correct_ang: 1.0000
  (valid)
loss total:  0.1019
loss_pos:    0.0051
loss_ang:    0.0968
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0234
loss_pos:    0.0051
loss_ang:    0.0183
correct_ang: 0.9944
  (valid)
loss total:  0.1223
loss_pos:    0.0050
loss_ang:    0.1173
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0194
loss_pos:    0.0064
loss_ang:    0.0130
correct_ang: 1.0000
  (valid)
loss total:  0.1095
loss_pos:    0.0079
loss_ang:    0.1016
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0150
loss_pos:    0.0046
loss_ang:    0.0104
correct_ang: 1.0000
  (valid)
loss total:  0.1065
loss_pos:    0.0053
loss_ang:    0.1012
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0233
loss_pos:    0.0051
loss_ang:    0.0182
correct_ang: 1.0000
  (valid)
loss total:  0.0909
loss_pos:    0.0053
loss_ang:    0.0855
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0121
loss_pos:    0.0046
loss_ang:    0.0075
correct_ang: 1.0000
  (valid)
loss total:  0.1017
loss_pos:    0.0055
loss_ang:    0.0962
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0115
loss_pos:    0.0047
loss_ang:    0.0068
correct_ang: 1.0000
  (valid)
loss total:  0.1195
loss_pos:    0.0080
loss_ang:    0.1115
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0107
loss_pos:    0.0053
loss_ang:    0.0054
correct_ang: 1.0000
  (valid)
loss total:  0.1173
loss_pos:    0.0067
loss_ang:    0.1107
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0107
loss_pos:    0.0070
loss_ang:    0.0038
correct_ang: 1.0000
  (valid)
loss total:  0.0898
loss_pos:    0.0077
loss_ang:    0.0821
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0097
loss_pos:    0.0047
loss_ang:    0.0050
correct_ang: 1.0000
  (valid)
loss total:  0.0696
loss_pos:    0.0065
loss_ang:    0.0631
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0082
loss_pos:    0.0043
loss_ang:    0.0039
correct_ang: 1.0000
  (valid)
loss total:  0.0581
loss_pos:    0.0054
loss_ang:    0.0527
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0082
loss_pos:    0.0054
loss_ang:    0.0029
correct_ang: 1.0000
  (valid)
loss total:  0.0579
loss_pos:    0.0041
loss_ang:    0.0539
correct_ang: 1.0000
------------------------------

Trained in 0m 51s
Best validation epoch total loss:  0.057932
  train:
[1.48973, 1.35034, 1.2037, 1.05238, 0.84164, 0.68135, 0.50552, 0.35631, 0.26239, 0.16155, 0.11608, 0.08746, 0.06155, 0.04499, 0.03371, 0.02748, 0.02454, 0.02534, 0.01586, 0.02337, 0.01944, 0.01504, 0.0233, 0.01205, 0.01155, 0.01068, 0.01074, 0.00973, 0.00822, 0.00823]
  valid:
[1.35463, 1.29961, 1.21237, 1.06725, 0.91518, 0.76454, 0.61116, 0.48307, 0.3875, 0.28524, 0.22705, 0.21431, 0.19159, 0.2057, 0.15532, 0.12011, 0.12104, 0.11026, 0.1019, 0.12231, 0.10946, 0.10651, 0.09086, 0.10169, 0.11947, 0.11735, 0.0898, 0.06962, 0.05808, 0.05793]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #1

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5021
loss_pos:    0.1378
loss_ang:    1.3643
correct_ang: 0.3408
  (valid)
loss total:  1.3960
loss_pos:    0.1075
loss_ang:    1.2885
correct_ang: 0.5000
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3028
loss_pos:    0.0480
loss_ang:    1.2548
correct_ang: 0.5419
  (valid)
loss total:  1.2240
loss_pos:    0.0707
loss_ang:    1.1533
correct_ang: 0.6000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.1451
loss_pos:    0.0202
loss_ang:    1.1248
correct_ang: 0.5642
  (valid)
loss total:  1.0246
loss_pos:    0.0377
loss_ang:    0.9869
correct_ang: 0.6500
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  0.9629
loss_pos:    0.0221
loss_ang:    0.9408
correct_ang: 0.7709
  (valid)
loss total:  0.8493
loss_pos:    0.0302
loss_ang:    0.8191
correct_ang: 0.7500
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.7809
loss_pos:    0.0128
loss_ang:    0.7681
correct_ang: 0.8156
  (valid)
loss total:  0.6711
loss_pos:    0.0331
loss_ang:    0.6381
correct_ang: 0.8000
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6200
loss_pos:    0.0132
loss_ang:    0.6068
correct_ang: 0.8939
  (valid)
loss total:  0.5162
loss_pos:    0.0176
loss_ang:    0.4986
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.4521
loss_pos:    0.0130
loss_ang:    0.4391
correct_ang: 0.9441
  (valid)
loss total:  0.4120
loss_pos:    0.0109
loss_ang:    0.4011
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.2937
loss_pos:    0.0126
loss_ang:    0.2811
correct_ang: 0.9721
  (valid)
loss total:  0.3231
loss_pos:    0.0088
loss_ang:    0.3143
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2154
loss_pos:    0.0096
loss_ang:    0.2057
correct_ang: 0.9665
  (valid)
loss total:  0.2347
loss_pos:    0.0079
loss_ang:    0.2268
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1324
loss_pos:    0.0095
loss_ang:    0.1229
correct_ang: 0.9888
  (valid)
loss total:  0.2475
loss_pos:    0.0058
loss_ang:    0.2416
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.1119
loss_pos:    0.0074
loss_ang:    0.1046
correct_ang: 0.9888
  (valid)
loss total:  0.2214
loss_pos:    0.0086
loss_ang:    0.2128
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0626
loss_pos:    0.0069
loss_ang:    0.0558
correct_ang: 1.0000
  (valid)
loss total:  0.1733
loss_pos:    0.0045
loss_ang:    0.1688
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0521
loss_pos:    0.0085
loss_ang:    0.0436
correct_ang: 0.9944
  (valid)
loss total:  0.1632
loss_pos:    0.0072
loss_ang:    0.1560
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0455
loss_pos:    0.0065
loss_ang:    0.0390
correct_ang: 1.0000
  (valid)
loss total:  0.1618
loss_pos:    0.0051
loss_ang:    0.1566
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0468
loss_pos:    0.0071
loss_ang:    0.0396
correct_ang: 1.0000
  (valid)
loss total:  0.1349
loss_pos:    0.0041
loss_ang:    0.1309
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0504
loss_pos:    0.0061
loss_ang:    0.0443
correct_ang: 0.9944
  (valid)
loss total:  0.0990
loss_pos:    0.0038
loss_ang:    0.0952
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0636
loss_pos:    0.0081
loss_ang:    0.0555
correct_ang: 0.9888
  (valid)
loss total:  0.1006
loss_pos:    0.0032
loss_ang:    0.0974
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0252
loss_pos:    0.0058
loss_ang:    0.0194
correct_ang: 1.0000
  (valid)
loss total:  0.1426
loss_pos:    0.0073
loss_ang:    0.1354
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0375
loss_pos:    0.0068
loss_ang:    0.0308
correct_ang: 0.9944
  (valid)
loss total:  0.1339
loss_pos:    0.0042
loss_ang:    0.1298
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0255
loss_pos:    0.0071
loss_ang:    0.0184
correct_ang: 0.9944
  (valid)
loss total:  0.1343
loss_pos:    0.0046
loss_ang:    0.1297
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0224
loss_pos:    0.0060
loss_ang:    0.0165
correct_ang: 1.0000
  (valid)
loss total:  0.1162
loss_pos:    0.0042
loss_ang:    0.1120
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0214
loss_pos:    0.0053
loss_ang:    0.0161
correct_ang: 1.0000
  (valid)
loss total:  0.1126
loss_pos:    0.0055
loss_ang:    0.1071
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0196
loss_pos:    0.0068
loss_ang:    0.0128
correct_ang: 1.0000
  (valid)
loss total:  0.1131
loss_pos:    0.0035
loss_ang:    0.1096
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0137
loss_pos:    0.0049
loss_ang:    0.0088
correct_ang: 1.0000
  (valid)
loss total:  0.1367
loss_pos:    0.0051
loss_ang:    0.1317
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0180
loss_pos:    0.0052
loss_ang:    0.0127
correct_ang: 1.0000
  (valid)
loss total:  0.1342
loss_pos:    0.0041
loss_ang:    0.1301
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0123
loss_pos:    0.0053
loss_ang:    0.0070
correct_ang: 1.0000
  (valid)
loss total:  0.1489
loss_pos:    0.0036
loss_ang:    0.1453
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0099
loss_pos:    0.0040
loss_ang:    0.0058
correct_ang: 1.0000
  (valid)
loss total:  0.1715
loss_pos:    0.0059
loss_ang:    0.1656
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0102
loss_pos:    0.0059
loss_ang:    0.0043
correct_ang: 1.0000
  (valid)
loss total:  0.1610
loss_pos:    0.0041
loss_ang:    0.1569
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0091
loss_pos:    0.0033
loss_ang:    0.0058
correct_ang: 1.0000
  (valid)
loss total:  0.1475
loss_pos:    0.0045
loss_ang:    0.1430
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0127
loss_pos:    0.0042
loss_ang:    0.0085
correct_ang: 1.0000
  (valid)
loss total:  0.1182
loss_pos:    0.0040
loss_ang:    0.1142
correct_ang: 0.9500
------------------------------

Trained in 0m 51s
Best validation epoch total loss:  0.099027
  train:
[1.50206, 1.30278, 1.14506, 0.96291, 0.78085, 0.62, 0.45213, 0.29368, 0.21537, 0.13238, 0.11194, 0.06262, 0.05209, 0.04551, 0.04675, 0.05043, 0.06361, 0.02521, 0.03752, 0.02548, 0.02241, 0.02137, 0.01959, 0.01375, 0.01796, 0.01231, 0.00986, 0.01019, 0.00909, 0.01272]
  valid:
[1.39595, 1.22395, 1.02459, 0.84928, 0.67115, 0.5162, 0.41199, 0.32309, 0.23468, 0.24745, 0.22136, 0.17331, 0.16316, 0.16177, 0.13493, 0.09903, 0.1006, 0.14262, 0.13391, 0.13431, 0.11615, 0.11263, 0.1131, 0.13674, 0.13425, 0.1489, 0.17147, 0.161, 0.1475, 0.11816]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #2

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5335
loss_pos:    0.1619
loss_ang:    1.3716
correct_ang: 0.2402
  (valid)
loss total:  1.4073
loss_pos:    0.0564
loss_ang:    1.3509
correct_ang: 0.2500
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3438
loss_pos:    0.0622
loss_ang:    1.2817
correct_ang: 0.4302
  (valid)
loss total:  1.3526
loss_pos:    0.0362
loss_ang:    1.3164
correct_ang: 0.3500
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.1858
loss_pos:    0.0269
loss_ang:    1.1590
correct_ang: 0.6592
  (valid)
loss total:  1.2772
loss_pos:    0.0516
loss_ang:    1.2256
correct_ang: 0.4500
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0606
loss_pos:    0.0279
loss_ang:    1.0327
correct_ang: 0.7095
  (valid)
loss total:  1.1147
loss_pos:    0.0311
loss_ang:    1.0836
correct_ang: 0.5500
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8751
loss_pos:    0.0178
loss_ang:    0.8573
correct_ang: 0.8045
  (valid)
loss total:  0.9270
loss_pos:    0.0210
loss_ang:    0.9060
correct_ang: 0.7500
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.7082
loss_pos:    0.0173
loss_ang:    0.6909
correct_ang: 0.8324
  (valid)
loss total:  0.7775
loss_pos:    0.0208
loss_ang:    0.7566
correct_ang: 0.7500
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.5008
loss_pos:    0.0134
loss_ang:    0.4874
correct_ang: 0.9330
  (valid)
loss total:  0.6186
loss_pos:    0.0108
loss_ang:    0.6078
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3628
loss_pos:    0.0104
loss_ang:    0.3523
correct_ang: 0.9665
  (valid)
loss total:  0.5001
loss_pos:    0.0113
loss_ang:    0.4888
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2825
loss_pos:    0.0110
loss_ang:    0.2716
correct_ang: 0.9609
  (valid)
loss total:  0.4756
loss_pos:    0.0124
loss_ang:    0.4632
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1314
loss_pos:    0.0094
loss_ang:    0.1221
correct_ang: 0.9944
  (valid)
loss total:  0.4192
loss_pos:    0.0113
loss_ang:    0.4079
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.1183
loss_pos:    0.0097
loss_ang:    0.1085
correct_ang: 0.9832
  (valid)
loss total:  0.2983
loss_pos:    0.0087
loss_ang:    0.2896
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0889
loss_pos:    0.0088
loss_ang:    0.0800
correct_ang: 0.9944
  (valid)
loss total:  0.2187
loss_pos:    0.0095
loss_ang:    0.2092
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0810
loss_pos:    0.0067
loss_ang:    0.0743
correct_ang: 0.9777
  (valid)
loss total:  0.1849
loss_pos:    0.0085
loss_ang:    0.1764
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0546
loss_pos:    0.0092
loss_ang:    0.0455
correct_ang: 0.9944
  (valid)
loss total:  0.1743
loss_pos:    0.0092
loss_ang:    0.1651
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0453
loss_pos:    0.0077
loss_ang:    0.0376
correct_ang: 1.0000
  (valid)
loss total:  0.1646
loss_pos:    0.0109
loss_ang:    0.1537
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0272
loss_pos:    0.0065
loss_ang:    0.0208
correct_ang: 1.0000
  (valid)
loss total:  0.1389
loss_pos:    0.0073
loss_ang:    0.1316
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0334
loss_pos:    0.0056
loss_ang:    0.0278
correct_ang: 1.0000
  (valid)
loss total:  0.1268
loss_pos:    0.0073
loss_ang:    0.1195
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0186
loss_pos:    0.0057
loss_ang:    0.0129
correct_ang: 1.0000
  (valid)
loss total:  0.1502
loss_pos:    0.0065
loss_ang:    0.1437
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0241
loss_pos:    0.0058
loss_ang:    0.0183
correct_ang: 1.0000
  (valid)
loss total:  0.1580
loss_pos:    0.0062
loss_ang:    0.1517
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0270
loss_pos:    0.0046
loss_ang:    0.0223
correct_ang: 0.9944
  (valid)
loss total:  0.1318
loss_pos:    0.0066
loss_ang:    0.1252
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0152
loss_pos:    0.0048
loss_ang:    0.0104
correct_ang: 1.0000
  (valid)
loss total:  0.0881
loss_pos:    0.0058
loss_ang:    0.0823
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0367
loss_pos:    0.0053
loss_ang:    0.0313
correct_ang: 0.9944
  (valid)
loss total:  0.1237
loss_pos:    0.0059
loss_ang:    0.1179
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0127
loss_pos:    0.0049
loss_ang:    0.0078
correct_ang: 1.0000
  (valid)
loss total:  0.1470
loss_pos:    0.0061
loss_ang:    0.1409
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0142
loss_pos:    0.0044
loss_ang:    0.0098
correct_ang: 1.0000
  (valid)
loss total:  0.1247
loss_pos:    0.0060
loss_ang:    0.1186
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0158
loss_pos:    0.0043
loss_ang:    0.0115
correct_ang: 1.0000
  (valid)
loss total:  0.0678
loss_pos:    0.0041
loss_ang:    0.0637
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0156
loss_pos:    0.0071
loss_ang:    0.0085
correct_ang: 1.0000
  (valid)
loss total:  0.0558
loss_pos:    0.0051
loss_ang:    0.0506
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0077
loss_pos:    0.0034
loss_ang:    0.0044
correct_ang: 1.0000
  (valid)
loss total:  0.0647
loss_pos:    0.0044
loss_ang:    0.0602
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0115
loss_pos:    0.0064
loss_ang:    0.0051
correct_ang: 1.0000
  (valid)
loss total:  0.0592
loss_pos:    0.0057
loss_ang:    0.0535
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0172
loss_pos:    0.0074
loss_ang:    0.0098
correct_ang: 1.0000
  (valid)
loss total:  0.0699
loss_pos:    0.0061
loss_ang:    0.0638
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0111
loss_pos:    0.0056
loss_ang:    0.0055
correct_ang: 1.0000
  (valid)
loss total:  0.0834
loss_pos:    0.0061
loss_ang:    0.0773
correct_ang: 1.0000
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.055759
  train:
[1.53346, 1.34383, 1.18582, 1.06059, 0.87506, 0.70824, 0.50077, 0.36276, 0.28254, 0.13143, 0.11827, 0.08886, 0.081, 0.05464, 0.0453, 0.02725, 0.03339, 0.0186, 0.02409, 0.02698, 0.01517, 0.03666, 0.01269, 0.0142, 0.01583, 0.0156, 0.00773, 0.01154, 0.01718, 0.01111]
  valid:
[1.40729, 1.3526, 1.27719, 1.1147, 0.92699, 0.77746, 0.61863, 0.50009, 0.47558, 0.41922, 0.29831, 0.21871, 0.18488, 0.17432, 0.16465, 0.13891, 0.1268, 0.1502, 0.15799, 0.13177, 0.08805, 0.12375, 0.14697, 0.12467, 0.06776, 0.05576, 0.06466, 0.05923, 0.06988, 0.08335]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #3

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5201
loss_pos:    0.1311
loss_ang:    1.3891
correct_ang: 0.2793
  (valid)
loss total:  1.4011
loss_pos:    0.0389
loss_ang:    1.3622
correct_ang: 0.2000
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3362
loss_pos:    0.0538
loss_ang:    1.2824
correct_ang: 0.5084
  (valid)
loss total:  1.3178
loss_pos:    0.0364
loss_ang:    1.2813
correct_ang: 0.5000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.1916
loss_pos:    0.0194
loss_ang:    1.1722
correct_ang: 0.5922
  (valid)
loss total:  1.1858
loss_pos:    0.0323
loss_ang:    1.1535
correct_ang: 0.6500
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0637
loss_pos:    0.0245
loss_ang:    1.0392
correct_ang: 0.6648
  (valid)
loss total:  1.0256
loss_pos:    0.0188
loss_ang:    1.0068
correct_ang: 0.7000
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8721
loss_pos:    0.0145
loss_ang:    0.8576
correct_ang: 0.7933
  (valid)
loss total:  0.8481
loss_pos:    0.0159
loss_ang:    0.8321
correct_ang: 0.7500
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6457
loss_pos:    0.0162
loss_ang:    0.6295
correct_ang: 0.8659
  (valid)
loss total:  0.6740
loss_pos:    0.0169
loss_ang:    0.6571
correct_ang: 0.7500
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.4768
loss_pos:    0.0134
loss_ang:    0.4633
correct_ang: 0.9106
  (valid)
loss total:  0.5150
loss_pos:    0.0143
loss_ang:    0.5006
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3291
loss_pos:    0.0120
loss_ang:    0.3171
correct_ang: 0.9609
  (valid)
loss total:  0.4383
loss_pos:    0.0187
loss_ang:    0.4196
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2181
loss_pos:    0.0100
loss_ang:    0.2081
correct_ang: 0.9832
  (valid)
loss total:  0.3828
loss_pos:    0.0132
loss_ang:    0.3697
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1470
loss_pos:    0.0086
loss_ang:    0.1384
correct_ang: 0.9832
  (valid)
loss total:  0.2656
loss_pos:    0.0110
loss_ang:    0.2546
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.1026
loss_pos:    0.0083
loss_ang:    0.0943
correct_ang: 0.9944
  (valid)
loss total:  0.2287
loss_pos:    0.0097
loss_ang:    0.2190
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0541
loss_pos:    0.0076
loss_ang:    0.0465
correct_ang: 0.9944
  (valid)
loss total:  0.3220
loss_pos:    0.0123
loss_ang:    0.3097
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0472
loss_pos:    0.0059
loss_ang:    0.0413
correct_ang: 1.0000
  (valid)
loss total:  0.3386
loss_pos:    0.0123
loss_ang:    0.3263
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0366
loss_pos:    0.0052
loss_ang:    0.0315
correct_ang: 1.0000
  (valid)
loss total:  0.3527
loss_pos:    0.0092
loss_ang:    0.3435
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0253
loss_pos:    0.0053
loss_ang:    0.0200
correct_ang: 1.0000
  (valid)
loss total:  0.3557
loss_pos:    0.0097
loss_ang:    0.3461
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0321
loss_pos:    0.0065
loss_ang:    0.0256
correct_ang: 1.0000
  (valid)
loss total:  0.3409
loss_pos:    0.0072
loss_ang:    0.3337
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0201
loss_pos:    0.0042
loss_ang:    0.0158
correct_ang: 1.0000
  (valid)
loss total:  0.2848
loss_pos:    0.0073
loss_ang:    0.2774
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0214
loss_pos:    0.0058
loss_ang:    0.0156
correct_ang: 1.0000
  (valid)
loss total:  0.2239
loss_pos:    0.0073
loss_ang:    0.2166
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0167
loss_pos:    0.0040
loss_ang:    0.0127
correct_ang: 1.0000
  (valid)
loss total:  0.1958
loss_pos:    0.0075
loss_ang:    0.1884
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0148
loss_pos:    0.0042
loss_ang:    0.0106
correct_ang: 1.0000
  (valid)
loss total:  0.1717
loss_pos:    0.0064
loss_ang:    0.1653
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0110
loss_pos:    0.0037
loss_ang:    0.0072
correct_ang: 1.0000
  (valid)
loss total:  0.1913
loss_pos:    0.0061
loss_ang:    0.1852
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0149
loss_pos:    0.0045
loss_ang:    0.0103
correct_ang: 1.0000
  (valid)
loss total:  0.2449
loss_pos:    0.0091
loss_ang:    0.2358
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0113
loss_pos:    0.0051
loss_ang:    0.0062
correct_ang: 1.0000
  (valid)
loss total:  0.2831
loss_pos:    0.0061
loss_ang:    0.2770
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0129
loss_pos:    0.0061
loss_ang:    0.0068
correct_ang: 1.0000
  (valid)
loss total:  0.3530
loss_pos:    0.0094
loss_ang:    0.3437
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0123
loss_pos:    0.0059
loss_ang:    0.0064
correct_ang: 1.0000
  (valid)
loss total:  0.3078
loss_pos:    0.0063
loss_ang:    0.3015
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0106
loss_pos:    0.0036
loss_ang:    0.0070
correct_ang: 1.0000
  (valid)
loss total:  0.2854
loss_pos:    0.0058
loss_ang:    0.2796
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0106
loss_pos:    0.0043
loss_ang:    0.0063
correct_ang: 1.0000
  (valid)
loss total:  0.3083
loss_pos:    0.0090
loss_ang:    0.2993
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0106
loss_pos:    0.0055
loss_ang:    0.0051
correct_ang: 1.0000
  (valid)
loss total:  0.2156
loss_pos:    0.0058
loss_ang:    0.2097
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0096
loss_pos:    0.0050
loss_ang:    0.0047
correct_ang: 1.0000
  (valid)
loss total:  0.1975
loss_pos:    0.0057
loss_ang:    0.1918
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0096
loss_pos:    0.0038
loss_ang:    0.0058
correct_ang: 1.0000
  (valid)
loss total:  0.2061
loss_pos:    0.0065
loss_ang:    0.1995
correct_ang: 0.9000
------------------------------

Trained in 0m 51s
Best validation epoch total loss:  0.171701
  train:
[1.52013, 1.33617, 1.19161, 1.06369, 0.87212, 0.64566, 0.47676, 0.32913, 0.21812, 0.147, 0.10259, 0.05414, 0.0472, 0.03663, 0.02532, 0.03211, 0.02006, 0.02145, 0.01674, 0.01478, 0.01098, 0.01486, 0.01126, 0.01288, 0.01232, 0.01059, 0.01056, 0.01061, 0.00963, 0.00964]
  valid:
[1.40108, 1.31777, 1.18585, 1.02558, 0.84807, 0.67398, 0.51499, 0.43834, 0.38285, 0.26556, 0.2287, 0.32199, 0.3386, 0.3527, 0.35573, 0.34086, 0.28479, 0.22385, 0.19582, 0.1717, 0.19127, 0.24488, 0.2831, 0.35303, 0.30776, 0.28539, 0.30826, 0.21557, 0.19748, 0.20607]

Visualizing performance of best model on validation set:
  18 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #4

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.4803
loss_pos:    0.1164
loss_ang:    1.3639
correct_ang: 0.3073
  (valid)
loss total:  1.3503
loss_pos:    0.0458
loss_ang:    1.3045
correct_ang: 0.3500
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3275
loss_pos:    0.0531
loss_ang:    1.2744
correct_ang: 0.4804
  (valid)
loss total:  1.2417
loss_pos:    0.0173
loss_ang:    1.2243
correct_ang: 0.3500
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.1672
loss_pos:    0.0245
loss_ang:    1.1427
correct_ang: 0.6034
  (valid)
loss total:  1.1251
loss_pos:    0.0274
loss_ang:    1.0977
correct_ang: 0.6000
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0351
loss_pos:    0.0186
loss_ang:    1.0165
correct_ang: 0.6704
  (valid)
loss total:  0.9905
loss_pos:    0.0171
loss_ang:    0.9733
correct_ang: 0.7000
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8385
loss_pos:    0.0164
loss_ang:    0.8221
correct_ang: 0.8212
  (valid)
loss total:  0.7764
loss_pos:    0.0150
loss_ang:    0.7615
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6386
loss_pos:    0.0143
loss_ang:    0.6244
correct_ang: 0.9441
  (valid)
loss total:  0.5798
loss_pos:    0.0077
loss_ang:    0.5721
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.4773
loss_pos:    0.0114
loss_ang:    0.4659
correct_ang: 0.9050
  (valid)
loss total:  0.4436
loss_pos:    0.0083
loss_ang:    0.4353
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3302
loss_pos:    0.0121
loss_ang:    0.3181
correct_ang: 0.9553
  (valid)
loss total:  0.3243
loss_pos:    0.0119
loss_ang:    0.3124
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2193
loss_pos:    0.0097
loss_ang:    0.2096
correct_ang: 0.9944
  (valid)
loss total:  0.2667
loss_pos:    0.0065
loss_ang:    0.2603
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1414
loss_pos:    0.0087
loss_ang:    0.1327
correct_ang: 0.9944
  (valid)
loss total:  0.1984
loss_pos:    0.0085
loss_ang:    0.1899
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.0921
loss_pos:    0.0074
loss_ang:    0.0847
correct_ang: 0.9944
  (valid)
loss total:  0.1959
loss_pos:    0.0077
loss_ang:    0.1883
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0613
loss_pos:    0.0067
loss_ang:    0.0547
correct_ang: 1.0000
  (valid)
loss total:  0.1774
loss_pos:    0.0061
loss_ang:    0.1713
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0531
loss_pos:    0.0071
loss_ang:    0.0460
correct_ang: 1.0000
  (valid)
loss total:  0.1577
loss_pos:    0.0051
loss_ang:    0.1526
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0502
loss_pos:    0.0075
loss_ang:    0.0426
correct_ang: 0.9888
  (valid)
loss total:  0.1874
loss_pos:    0.0040
loss_ang:    0.1834
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0339
loss_pos:    0.0059
loss_ang:    0.0280
correct_ang: 1.0000
  (valid)
loss total:  0.1724
loss_pos:    0.0094
loss_ang:    0.1630
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0188
loss_pos:    0.0049
loss_ang:    0.0139
correct_ang: 1.0000
  (valid)
loss total:  0.1373
loss_pos:    0.0054
loss_ang:    0.1319
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0205
loss_pos:    0.0052
loss_ang:    0.0152
correct_ang: 1.0000
  (valid)
loss total:  0.1198
loss_pos:    0.0062
loss_ang:    0.1136
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0171
loss_pos:    0.0061
loss_ang:    0.0110
correct_ang: 1.0000
  (valid)
loss total:  0.1465
loss_pos:    0.0057
loss_ang:    0.1407
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0186
loss_pos:    0.0045
loss_ang:    0.0141
correct_ang: 1.0000
  (valid)
loss total:  0.1889
loss_pos:    0.0044
loss_ang:    0.1845
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0324
loss_pos:    0.0052
loss_ang:    0.0272
correct_ang: 1.0000
  (valid)
loss total:  0.2153
loss_pos:    0.0048
loss_ang:    0.2104
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0130
loss_pos:    0.0048
loss_ang:    0.0081
correct_ang: 1.0000
  (valid)
loss total:  0.1980
loss_pos:    0.0054
loss_ang:    0.1926
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0142
loss_pos:    0.0044
loss_ang:    0.0098
correct_ang: 1.0000
  (valid)
loss total:  0.2026
loss_pos:    0.0084
loss_ang:    0.1942
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0102
loss_pos:    0.0052
loss_ang:    0.0050
correct_ang: 1.0000
  (valid)
loss total:  0.1541
loss_pos:    0.0046
loss_ang:    0.1495
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0136
loss_pos:    0.0049
loss_ang:    0.0087
correct_ang: 1.0000
  (valid)
loss total:  0.1564
loss_pos:    0.0037
loss_ang:    0.1526
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0084
loss_pos:    0.0041
loss_ang:    0.0043
correct_ang: 1.0000
  (valid)
loss total:  0.1890
loss_pos:    0.0058
loss_ang:    0.1832
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0120
loss_pos:    0.0059
loss_ang:    0.0060
correct_ang: 1.0000
  (valid)
loss total:  0.1847
loss_pos:    0.0043
loss_ang:    0.1804
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0074
loss_pos:    0.0038
loss_ang:    0.0036
correct_ang: 1.0000
  (valid)
loss total:  0.1925
loss_pos:    0.0044
loss_ang:    0.1881
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0081
loss_pos:    0.0039
loss_ang:    0.0043
correct_ang: 1.0000
  (valid)
loss total:  0.1689
loss_pos:    0.0037
loss_ang:    0.1652
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0117
loss_pos:    0.0056
loss_ang:    0.0061
correct_ang: 1.0000
  (valid)
loss total:  0.1481
loss_pos:    0.0047
loss_ang:    0.1435
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0099
loss_pos:    0.0076
loss_ang:    0.0023
correct_ang: 1.0000
  (valid)
loss total:  0.1473
loss_pos:    0.0038
loss_ang:    0.1435
correct_ang: 0.9500
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.119822
  train:
[1.48034, 1.32753, 1.16719, 1.0351, 0.83846, 0.63863, 0.47729, 0.33018, 0.21931, 0.14144, 0.09209, 0.06135, 0.0531, 0.05015, 0.03389, 0.01875, 0.02048, 0.01711, 0.01861, 0.03245, 0.01297, 0.01424, 0.01021, 0.0136, 0.00843, 0.01196, 0.00738, 0.00813, 0.0117, 0.0099]
  valid:
[1.35026, 1.24165, 1.12507, 0.99047, 0.77645, 0.57983, 0.44365, 0.32432, 0.26673, 0.19841, 0.19591, 0.17741, 0.15765, 0.1874, 0.17237, 0.13726, 0.11982, 0.14646, 0.1889, 0.21525, 0.19801, 0.20265, 0.1541, 0.15637, 0.18899, 0.18466, 0.19252, 0.16885, 0.14813, 0.14731]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #5

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5117
loss_pos:    0.1621
loss_ang:    1.3496
correct_ang: 0.3743
  (valid)
loss total:  1.3955
loss_pos:    0.0612
loss_ang:    1.3344
correct_ang: 0.4500
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3488
loss_pos:    0.0548
loss_ang:    1.2940
correct_ang: 0.3855
  (valid)
loss total:  1.3623
loss_pos:    0.0540
loss_ang:    1.3083
correct_ang: 0.4500
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.2049
loss_pos:    0.0257
loss_ang:    1.1791
correct_ang: 0.5307
  (valid)
loss total:  1.2167
loss_pos:    0.0193
loss_ang:    1.1974
correct_ang: 0.5500
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0639
loss_pos:    0.0227
loss_ang:    1.0412
correct_ang: 0.6927
  (valid)
loss total:  1.0566
loss_pos:    0.0124
loss_ang:    1.0442
correct_ang: 0.6000
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8523
loss_pos:    0.0176
loss_ang:    0.8347
correct_ang: 0.7933
  (valid)
loss total:  0.8883
loss_pos:    0.0377
loss_ang:    0.8507
correct_ang: 0.7000
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.7114
loss_pos:    0.0148
loss_ang:    0.6966
correct_ang: 0.8380
  (valid)
loss total:  0.7061
loss_pos:    0.0405
loss_ang:    0.6655
correct_ang: 0.8000
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.5080
loss_pos:    0.0129
loss_ang:    0.4951
correct_ang: 0.9330
  (valid)
loss total:  0.5252
loss_pos:    0.0272
loss_ang:    0.4980
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3379
loss_pos:    0.0120
loss_ang:    0.3259
correct_ang: 0.9721
  (valid)
loss total:  0.4074
loss_pos:    0.0145
loss_ang:    0.3930
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2318
loss_pos:    0.0094
loss_ang:    0.2224
correct_ang: 0.9777
  (valid)
loss total:  0.3446
loss_pos:    0.0159
loss_ang:    0.3287
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1659
loss_pos:    0.0102
loss_ang:    0.1557
correct_ang: 0.9832
  (valid)
loss total:  0.2892
loss_pos:    0.0130
loss_ang:    0.2762
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.0890
loss_pos:    0.0090
loss_ang:    0.0800
correct_ang: 0.9888
  (valid)
loss total:  0.2460
loss_pos:    0.0144
loss_ang:    0.2316
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0622
loss_pos:    0.0081
loss_ang:    0.0542
correct_ang: 1.0000
  (valid)
loss total:  0.1800
loss_pos:    0.0159
loss_ang:    0.1641
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0485
loss_pos:    0.0070
loss_ang:    0.0415
correct_ang: 0.9944
  (valid)
loss total:  0.1381
loss_pos:    0.0138
loss_ang:    0.1243
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0448
loss_pos:    0.0084
loss_ang:    0.0364
correct_ang: 0.9944
  (valid)
loss total:  0.1124
loss_pos:    0.0139
loss_ang:    0.0985
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0326
loss_pos:    0.0076
loss_ang:    0.0250
correct_ang: 1.0000
  (valid)
loss total:  0.1274
loss_pos:    0.0125
loss_ang:    0.1149
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0350
loss_pos:    0.0096
loss_ang:    0.0254
correct_ang: 0.9944
  (valid)
loss total:  0.1170
loss_pos:    0.0098
loss_ang:    0.1072
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0204
loss_pos:    0.0070
loss_ang:    0.0134
correct_ang: 1.0000
  (valid)
loss total:  0.1150
loss_pos:    0.0120
loss_ang:    0.1030
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0231
loss_pos:    0.0055
loss_ang:    0.0176
correct_ang: 1.0000
  (valid)
loss total:  0.0927
loss_pos:    0.0089
loss_ang:    0.0838
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0247
loss_pos:    0.0075
loss_ang:    0.0171
correct_ang: 1.0000
  (valid)
loss total:  0.1192
loss_pos:    0.0108
loss_ang:    0.1084
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0311
loss_pos:    0.0053
loss_ang:    0.0258
correct_ang: 0.9944
  (valid)
loss total:  0.1293
loss_pos:    0.0095
loss_ang:    0.1197
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0237
loss_pos:    0.0070
loss_ang:    0.0167
correct_ang: 1.0000
  (valid)
loss total:  0.1426
loss_pos:    0.0103
loss_ang:    0.1323
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0220
loss_pos:    0.0065
loss_ang:    0.0154
correct_ang: 0.9944
  (valid)
loss total:  0.1120
loss_pos:    0.0102
loss_ang:    0.1019
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0142
loss_pos:    0.0050
loss_ang:    0.0092
correct_ang: 1.0000
  (valid)
loss total:  0.1155
loss_pos:    0.0111
loss_ang:    0.1045
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0341
loss_pos:    0.0070
loss_ang:    0.0271
correct_ang: 0.9944
  (valid)
loss total:  0.0964
loss_pos:    0.0082
loss_ang:    0.0881
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0147
loss_pos:    0.0054
loss_ang:    0.0093
correct_ang: 1.0000
  (valid)
loss total:  0.0936
loss_pos:    0.0131
loss_ang:    0.0804
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0135
loss_pos:    0.0049
loss_ang:    0.0086
correct_ang: 1.0000
  (valid)
loss total:  0.0801
loss_pos:    0.0135
loss_ang:    0.0666
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0158
loss_pos:    0.0055
loss_ang:    0.0104
correct_ang: 1.0000
  (valid)
loss total:  0.0689
loss_pos:    0.0077
loss_ang:    0.0612
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0133
loss_pos:    0.0046
loss_ang:    0.0087
correct_ang: 1.0000
  (valid)
loss total:  0.0718
loss_pos:    0.0070
loss_ang:    0.0648
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0084
loss_pos:    0.0046
loss_ang:    0.0038
correct_ang: 1.0000
  (valid)
loss total:  0.0827
loss_pos:    0.0065
loss_ang:    0.0762
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0088
loss_pos:    0.0042
loss_ang:    0.0045
correct_ang: 1.0000
  (valid)
loss total:  0.0951
loss_pos:    0.0088
loss_ang:    0.0863
correct_ang: 1.0000
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.068914
  train:
[1.51168, 1.34882, 1.20485, 1.06393, 0.85232, 0.71137, 0.50804, 0.33789, 0.23177, 0.16591, 0.08897, 0.06222, 0.04854, 0.04478, 0.0326, 0.035, 0.02045, 0.02313, 0.02466, 0.03114, 0.02374, 0.02195, 0.01417, 0.03414, 0.01465, 0.01348, 0.01585, 0.01329, 0.00837, 0.00877]
  valid:
[1.39554, 1.3623, 1.21667, 1.05657, 0.88833, 0.70607, 0.52523, 0.40742, 0.34461, 0.28917, 0.24604, 0.18004, 0.13812, 0.11239, 0.12745, 0.11698, 0.11499, 0.0927, 0.11923, 0.12927, 0.1426, 0.11205, 0.11555, 0.09635, 0.09357, 0.08006, 0.06891, 0.07183, 0.08268, 0.09511]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #6

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5284
loss_pos:    0.1514
loss_ang:    1.3770
correct_ang: 0.3240
  (valid)
loss total:  1.3838
loss_pos:    0.0428
loss_ang:    1.3411
correct_ang: 0.3500
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3257
loss_pos:    0.0578
loss_ang:    1.2679
correct_ang: 0.4302
  (valid)
loss total:  1.3375
loss_pos:    0.0483
loss_ang:    1.2891
correct_ang: 0.3000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.1890
loss_pos:    0.0254
loss_ang:    1.1636
correct_ang: 0.4916
  (valid)
loss total:  1.2299
loss_pos:    0.0360
loss_ang:    1.1939
correct_ang: 0.3500
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0592
loss_pos:    0.0242
loss_ang:    1.0350
correct_ang: 0.6816
  (valid)
loss total:  1.0645
loss_pos:    0.0197
loss_ang:    1.0449
correct_ang: 0.6500
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8371
loss_pos:    0.0182
loss_ang:    0.8189
correct_ang: 0.8659
  (valid)
loss total:  0.8611
loss_pos:    0.0182
loss_ang:    0.8429
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6350
loss_pos:    0.0202
loss_ang:    0.6147
correct_ang: 0.9330
  (valid)
loss total:  0.7340
loss_pos:    0.0265
loss_ang:    0.7074
correct_ang: 0.7500
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.4674
loss_pos:    0.0162
loss_ang:    0.4512
correct_ang: 0.9497
  (valid)
loss total:  0.6386
loss_pos:    0.0131
loss_ang:    0.6255
correct_ang: 0.7500
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3079
loss_pos:    0.0122
loss_ang:    0.2957
correct_ang: 0.9832
  (valid)
loss total:  0.5046
loss_pos:    0.0107
loss_ang:    0.4939
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2339
loss_pos:    0.0121
loss_ang:    0.2217
correct_ang: 0.9609
  (valid)
loss total:  0.4029
loss_pos:    0.0083
loss_ang:    0.3945
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1486
loss_pos:    0.0093
loss_ang:    0.1393
correct_ang: 0.9832
  (valid)
loss total:  0.3775
loss_pos:    0.0138
loss_ang:    0.3638
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.1055
loss_pos:    0.0091
loss_ang:    0.0964
correct_ang: 0.9944
  (valid)
loss total:  0.3942
loss_pos:    0.0078
loss_ang:    0.3864
correct_ang: 0.8000
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0862
loss_pos:    0.0078
loss_ang:    0.0784
correct_ang: 1.0000
  (valid)
loss total:  0.4211
loss_pos:    0.0095
loss_ang:    0.4117
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0520
loss_pos:    0.0071
loss_ang:    0.0449
correct_ang: 1.0000
  (valid)
loss total:  0.2994
loss_pos:    0.0069
loss_ang:    0.2925
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0508
loss_pos:    0.0068
loss_ang:    0.0441
correct_ang: 0.9944
  (valid)
loss total:  0.2319
loss_pos:    0.0062
loss_ang:    0.2257
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0271
loss_pos:    0.0053
loss_ang:    0.0218
correct_ang: 1.0000
  (valid)
loss total:  0.2264
loss_pos:    0.0071
loss_ang:    0.2192
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0336
loss_pos:    0.0056
loss_ang:    0.0280
correct_ang: 1.0000
  (valid)
loss total:  0.2701
loss_pos:    0.0080
loss_ang:    0.2621
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0199
loss_pos:    0.0064
loss_ang:    0.0136
correct_ang: 1.0000
  (valid)
loss total:  0.2931
loss_pos:    0.0061
loss_ang:    0.2870
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0243
loss_pos:    0.0065
loss_ang:    0.0178
correct_ang: 1.0000
  (valid)
loss total:  0.2782
loss_pos:    0.0069
loss_ang:    0.2713
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0162
loss_pos:    0.0053
loss_ang:    0.0108
correct_ang: 1.0000
  (valid)
loss total:  0.2696
loss_pos:    0.0056
loss_ang:    0.2640
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0142
loss_pos:    0.0035
loss_ang:    0.0107
correct_ang: 1.0000
  (valid)
loss total:  0.2488
loss_pos:    0.0055
loss_ang:    0.2433
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0096
loss_pos:    0.0033
loss_ang:    0.0063
correct_ang: 1.0000
  (valid)
loss total:  0.2592
loss_pos:    0.0052
loss_ang:    0.2540
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0094
loss_pos:    0.0038
loss_ang:    0.0056
correct_ang: 1.0000
  (valid)
loss total:  0.2662
loss_pos:    0.0054
loss_ang:    0.2608
correct_ang: 0.8500
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0146
loss_pos:    0.0046
loss_ang:    0.0101
correct_ang: 1.0000
  (valid)
loss total:  0.2564
loss_pos:    0.0057
loss_ang:    0.2507
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0111
loss_pos:    0.0039
loss_ang:    0.0073
correct_ang: 1.0000
  (valid)
loss total:  0.2250
loss_pos:    0.0054
loss_ang:    0.2196
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0111
loss_pos:    0.0044
loss_ang:    0.0067
correct_ang: 1.0000
  (valid)
loss total:  0.2152
loss_pos:    0.0053
loss_ang:    0.2099
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0136
loss_pos:    0.0085
loss_ang:    0.0051
correct_ang: 1.0000
  (valid)
loss total:  0.2082
loss_pos:    0.0051
loss_ang:    0.2031
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0127
loss_pos:    0.0079
loss_ang:    0.0047
correct_ang: 1.0000
  (valid)
loss total:  0.2110
loss_pos:    0.0075
loss_ang:    0.2035
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0154
loss_pos:    0.0041
loss_ang:    0.0113
correct_ang: 1.0000
  (valid)
loss total:  0.1826
loss_pos:    0.0047
loss_ang:    0.1780
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0075
loss_pos:    0.0042
loss_ang:    0.0033
correct_ang: 1.0000
  (valid)
loss total:  0.2085
loss_pos:    0.0075
loss_ang:    0.2010
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0089
loss_pos:    0.0036
loss_ang:    0.0052
correct_ang: 1.0000
  (valid)
loss total:  0.2277
loss_pos:    0.0048
loss_ang:    0.2229
correct_ang: 0.9000
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.182634
  train:
[1.52839, 1.32568, 1.18896, 1.05916, 0.83714, 0.63496, 0.46745, 0.30792, 0.23385, 0.14858, 0.10554, 0.08621, 0.05197, 0.05085, 0.02714, 0.03365, 0.01991, 0.02432, 0.01618, 0.0142, 0.00959, 0.00938, 0.01464, 0.01114, 0.01112, 0.01362, 0.01266, 0.01543, 0.00754, 0.00887]
  valid:
[1.38385, 1.33749, 1.22994, 1.06455, 0.86109, 0.73396, 0.63861, 0.50459, 0.40287, 0.37751, 0.39419, 0.42115, 0.29941, 0.23189, 0.22636, 0.27009, 0.29312, 0.27823, 0.26963, 0.24885, 0.25919, 0.26625, 0.25642, 0.22498, 0.2152, 0.20816, 0.21101, 0.18263, 0.20853, 0.22771]

Visualizing performance of best model on validation set:
  18 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #7

Now training!! On device: cuda:0
data_sizes: {'train': 180.0, 'valid': 19.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5570
loss_pos:    0.1877
loss_ang:    1.3693
correct_ang: 0.3833
  (valid)
loss total:  1.3586
loss_pos:    0.0403
loss_ang:    1.3183
correct_ang: 0.4211
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3627
loss_pos:    0.0566
loss_ang:    1.3061
correct_ang: 0.3667
  (valid)
loss total:  1.2420
loss_pos:    0.0593
loss_ang:    1.1827
correct_ang: 0.4737
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.2053
loss_pos:    0.0262
loss_ang:    1.1791
correct_ang: 0.5167
  (valid)
loss total:  1.1360
loss_pos:    0.0332
loss_ang:    1.1029
correct_ang: 0.5789
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0677
loss_pos:    0.0227
loss_ang:    1.0450
correct_ang: 0.7222
  (valid)
loss total:  1.0162
loss_pos:    0.0384
loss_ang:    0.9777
correct_ang: 0.7895
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8877
loss_pos:    0.0201
loss_ang:    0.8677
correct_ang: 0.8444
  (valid)
loss total:  0.8559
loss_pos:    0.0229
loss_ang:    0.8329
correct_ang: 0.8947
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6875
loss_pos:    0.0139
loss_ang:    0.6735
correct_ang: 0.9222
  (valid)
loss total:  0.6491
loss_pos:    0.0217
loss_ang:    0.6274
correct_ang: 0.8947
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.5140
loss_pos:    0.0139
loss_ang:    0.5001
correct_ang: 0.9389
  (valid)
loss total:  0.4704
loss_pos:    0.0133
loss_ang:    0.4571
correct_ang: 0.8947
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3347
loss_pos:    0.0101
loss_ang:    0.3246
correct_ang: 0.9889
  (valid)
loss total:  0.3525
loss_pos:    0.0084
loss_ang:    0.3440
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2399
loss_pos:    0.0097
loss_ang:    0.2302
correct_ang: 0.9833
  (valid)
loss total:  0.2561
loss_pos:    0.0051
loss_ang:    0.2510
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1373
loss_pos:    0.0077
loss_ang:    0.1296
correct_ang: 0.9944
  (valid)
loss total:  0.2211
loss_pos:    0.0051
loss_ang:    0.2160
correct_ang: 0.8947
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.1085
loss_pos:    0.0058
loss_ang:    0.1027
correct_ang: 1.0000
  (valid)
loss total:  0.2205
loss_pos:    0.0072
loss_ang:    0.2132
correct_ang: 0.8947
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0545
loss_pos:    0.0066
loss_ang:    0.0479
correct_ang: 1.0000
  (valid)
loss total:  0.1703
loss_pos:    0.0100
loss_ang:    0.1604
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0416
loss_pos:    0.0059
loss_ang:    0.0356
correct_ang: 1.0000
  (valid)
loss total:  0.1407
loss_pos:    0.0087
loss_ang:    0.1319
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0386
loss_pos:    0.0080
loss_ang:    0.0306
correct_ang: 1.0000
  (valid)
loss total:  0.1429
loss_pos:    0.0078
loss_ang:    0.1351
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0223
loss_pos:    0.0053
loss_ang:    0.0170
correct_ang: 1.0000
  (valid)
loss total:  0.1642
loss_pos:    0.0098
loss_ang:    0.1544
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0222
loss_pos:    0.0059
loss_ang:    0.0163
correct_ang: 1.0000
  (valid)
loss total:  0.1493
loss_pos:    0.0059
loss_ang:    0.1434
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0208
loss_pos:    0.0056
loss_ang:    0.0153
correct_ang: 1.0000
  (valid)
loss total:  0.1638
loss_pos:    0.0049
loss_ang:    0.1589
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0123
loss_pos:    0.0038
loss_ang:    0.0085
correct_ang: 1.0000
  (valid)
loss total:  0.1567
loss_pos:    0.0059
loss_ang:    0.1509
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0164
loss_pos:    0.0054
loss_ang:    0.0110
correct_ang: 1.0000
  (valid)
loss total:  0.1590
loss_pos:    0.0055
loss_ang:    0.1535
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0172
loss_pos:    0.0043
loss_ang:    0.0129
correct_ang: 1.0000
  (valid)
loss total:  0.1198
loss_pos:    0.0047
loss_ang:    0.1151
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0126
loss_pos:    0.0039
loss_ang:    0.0087
correct_ang: 1.0000
  (valid)
loss total:  0.1143
loss_pos:    0.0050
loss_ang:    0.1093
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0090
loss_pos:    0.0036
loss_ang:    0.0054
correct_ang: 1.0000
  (valid)
loss total:  0.1279
loss_pos:    0.0049
loss_ang:    0.1230
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0120
loss_pos:    0.0043
loss_ang:    0.0077
correct_ang: 1.0000
  (valid)
loss total:  0.1558
loss_pos:    0.0066
loss_ang:    0.1492
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0088
loss_pos:    0.0034
loss_ang:    0.0054
correct_ang: 1.0000
  (valid)
loss total:  0.1578
loss_pos:    0.0044
loss_ang:    0.1534
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0100
loss_pos:    0.0050
loss_ang:    0.0050
correct_ang: 1.0000
  (valid)
loss total:  0.1414
loss_pos:    0.0044
loss_ang:    0.1370
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0069
loss_pos:    0.0027
loss_ang:    0.0042
correct_ang: 1.0000
  (valid)
loss total:  0.1296
loss_pos:    0.0047
loss_ang:    0.1249
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0098
loss_pos:    0.0052
loss_ang:    0.0046
correct_ang: 1.0000
  (valid)
loss total:  0.1253
loss_pos:    0.0030
loss_ang:    0.1223
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0073
loss_pos:    0.0035
loss_ang:    0.0037
correct_ang: 1.0000
  (valid)
loss total:  0.1152
loss_pos:    0.0041
loss_ang:    0.1111
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0069
loss_pos:    0.0036
loss_ang:    0.0033
correct_ang: 1.0000
  (valid)
loss total:  0.1137
loss_pos:    0.0034
loss_ang:    0.1103
correct_ang: 0.9474
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0063
loss_pos:    0.0031
loss_ang:    0.0032
correct_ang: 1.0000
  (valid)
loss total:  0.1278
loss_pos:    0.0043
loss_ang:    0.1235
correct_ang: 0.9474
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.113667
  train:
[1.55703, 1.36269, 1.20526, 1.06771, 0.88775, 0.68746, 0.514, 0.3347, 0.23987, 0.13729, 0.10852, 0.05448, 0.04156, 0.0386, 0.02234, 0.02219, 0.02083, 0.01231, 0.01644, 0.01716, 0.01261, 0.00905, 0.01201, 0.0088, 0.00997, 0.00689, 0.00976, 0.00726, 0.00687, 0.00629]
  valid:
[1.35861, 1.24198, 1.13604, 1.01619, 0.85585, 0.64908, 0.4704, 0.35246, 0.25611, 0.22112, 0.22048, 0.17035, 0.1407, 0.14287, 0.16417, 0.14935, 0.16379, 0.15675, 0.15899, 0.11984, 0.11433, 0.12791, 0.15578, 0.15781, 0.14141, 0.12961, 0.12531, 0.11523, 0.11367, 0.12776]

Visualizing performance of best model on validation set:
  18 / 19 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #8

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5262
loss_pos:    0.1597
loss_ang:    1.3664
correct_ang: 0.3352
  (valid)
loss total:  1.4383
loss_pos:    0.0882
loss_ang:    1.3501
correct_ang: 0.3000
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3399
loss_pos:    0.0561
loss_ang:    1.2838
correct_ang: 0.3743
  (valid)
loss total:  1.3884
loss_pos:    0.0914
loss_ang:    1.2970
correct_ang: 0.4000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.2077
loss_pos:    0.0185
loss_ang:    1.1892
correct_ang: 0.4972
  (valid)
loss total:  1.2060
loss_pos:    0.0191
loss_ang:    1.1869
correct_ang: 0.6000
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0620
loss_pos:    0.0244
loss_ang:    1.0376
correct_ang: 0.6704
  (valid)
loss total:  0.9990
loss_pos:    0.0184
loss_ang:    0.9806
correct_ang: 0.7500
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8704
loss_pos:    0.0170
loss_ang:    0.8534
correct_ang: 0.8156
  (valid)
loss total:  0.7793
loss_pos:    0.0335
loss_ang:    0.7457
correct_ang: 0.7000
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6661
loss_pos:    0.0158
loss_ang:    0.6504
correct_ang: 0.8715
  (valid)
loss total:  0.5737
loss_pos:    0.0152
loss_ang:    0.5585
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.5151
loss_pos:    0.0119
loss_ang:    0.5032
correct_ang: 0.9106
  (valid)
loss total:  0.4268
loss_pos:    0.0154
loss_ang:    0.4114
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3310
loss_pos:    0.0121
loss_ang:    0.3190
correct_ang: 0.9497
  (valid)
loss total:  0.2649
loss_pos:    0.0057
loss_ang:    0.2593
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.2305
loss_pos:    0.0079
loss_ang:    0.2226
correct_ang: 0.9609
  (valid)
loss total:  0.2391
loss_pos:    0.0080
loss_ang:    0.2312
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1647
loss_pos:    0.0104
loss_ang:    0.1542
correct_ang: 0.9721
  (valid)
loss total:  0.1686
loss_pos:    0.0076
loss_ang:    0.1610
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.0844
loss_pos:    0.0079
loss_ang:    0.0765
correct_ang: 0.9944
  (valid)
loss total:  0.0999
loss_pos:    0.0080
loss_ang:    0.0919
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0804
loss_pos:    0.0074
loss_ang:    0.0730
correct_ang: 0.9944
  (valid)
loss total:  0.0913
loss_pos:    0.0086
loss_ang:    0.0827
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0452
loss_pos:    0.0063
loss_ang:    0.0390
correct_ang: 1.0000
  (valid)
loss total:  0.0995
loss_pos:    0.0051
loss_ang:    0.0943
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0453
loss_pos:    0.0059
loss_ang:    0.0394
correct_ang: 1.0000
  (valid)
loss total:  0.1010
loss_pos:    0.0059
loss_ang:    0.0951
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0360
loss_pos:    0.0076
loss_ang:    0.0284
correct_ang: 1.0000
  (valid)
loss total:  0.1365
loss_pos:    0.0081
loss_ang:    0.1283
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0241
loss_pos:    0.0058
loss_ang:    0.0183
correct_ang: 1.0000
  (valid)
loss total:  0.1183
loss_pos:    0.0080
loss_ang:    0.1103
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0259
loss_pos:    0.0062
loss_ang:    0.0198
correct_ang: 1.0000
  (valid)
loss total:  0.0895
loss_pos:    0.0060
loss_ang:    0.0835
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0173
loss_pos:    0.0054
loss_ang:    0.0119
correct_ang: 1.0000
  (valid)
loss total:  0.0910
loss_pos:    0.0047
loss_ang:    0.0863
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0135
loss_pos:    0.0069
loss_ang:    0.0066
correct_ang: 1.0000
  (valid)
loss total:  0.0862
loss_pos:    0.0056
loss_ang:    0.0805
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0150
loss_pos:    0.0073
loss_ang:    0.0077
correct_ang: 1.0000
  (valid)
loss total:  0.0945
loss_pos:    0.0058
loss_ang:    0.0887
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0133
loss_pos:    0.0054
loss_ang:    0.0078
correct_ang: 1.0000
  (valid)
loss total:  0.0728
loss_pos:    0.0053
loss_ang:    0.0675
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0110
loss_pos:    0.0038
loss_ang:    0.0072
correct_ang: 1.0000
  (valid)
loss total:  0.0519
loss_pos:    0.0053
loss_ang:    0.0467
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0202
loss_pos:    0.0043
loss_ang:    0.0159
correct_ang: 0.9944
  (valid)
loss total:  0.0537
loss_pos:    0.0059
loss_ang:    0.0478
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0112
loss_pos:    0.0039
loss_ang:    0.0073
correct_ang: 1.0000
  (valid)
loss total:  0.0515
loss_pos:    0.0052
loss_ang:    0.0463
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0185
loss_pos:    0.0045
loss_ang:    0.0140
correct_ang: 1.0000
  (valid)
loss total:  0.0927
loss_pos:    0.0058
loss_ang:    0.0869
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0084
loss_pos:    0.0039
loss_ang:    0.0045
correct_ang: 1.0000
  (valid)
loss total:  0.0960
loss_pos:    0.0062
loss_ang:    0.0898
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0121
loss_pos:    0.0042
loss_ang:    0.0079
correct_ang: 1.0000
  (valid)
loss total:  0.0721
loss_pos:    0.0033
loss_ang:    0.0687
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0110
loss_pos:    0.0051
loss_ang:    0.0058
correct_ang: 1.0000
  (valid)
loss total:  0.0420
loss_pos:    0.0053
loss_ang:    0.0366
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0156
loss_pos:    0.0040
loss_ang:    0.0116
correct_ang: 0.9944
  (valid)
loss total:  0.0345
loss_pos:    0.0051
loss_ang:    0.0294
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0124
loss_pos:    0.0047
loss_ang:    0.0077
correct_ang: 1.0000
  (valid)
loss total:  0.1155
loss_pos:    0.0076
loss_ang:    0.1080
correct_ang: 0.9500
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.034470
  train:
[1.52618, 1.33986, 1.20765, 1.06196, 0.87042, 0.66612, 0.51505, 0.33101, 0.2305, 0.16465, 0.08443, 0.08042, 0.04524, 0.04535, 0.03601, 0.02412, 0.02593, 0.01734, 0.01348, 0.01499, 0.01326, 0.01103, 0.02018, 0.01117, 0.01847, 0.00843, 0.01211, 0.01096, 0.01556, 0.0124]
  valid:
[1.43835, 1.38838, 1.20601, 0.99898, 0.77925, 0.57373, 0.42683, 0.26493, 0.23915, 0.16862, 0.09989, 0.0913, 0.09947, 0.10095, 0.13648, 0.11828, 0.08951, 0.091, 0.08615, 0.09446, 0.07276, 0.05194, 0.0537, 0.05154, 0.09271, 0.096, 0.07207, 0.04197, 0.03447, 0.11554]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #9

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.4996
loss_pos:    0.1533
loss_ang:    1.3462
correct_ang: 0.3464
  (valid)
loss total:  1.4317
loss_pos:    0.0805
loss_ang:    1.3511
correct_ang: 0.3000
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3402
loss_pos:    0.0623
loss_ang:    1.2779
correct_ang: 0.3799
  (valid)
loss total:  1.3678
loss_pos:    0.0807
loss_ang:    1.2872
correct_ang: 0.3000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.2146
loss_pos:    0.0248
loss_ang:    1.1897
correct_ang: 0.4469
  (valid)
loss total:  1.1122
loss_pos:    0.0286
loss_ang:    1.0835
correct_ang: 0.5500
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0826
loss_pos:    0.0215
loss_ang:    1.0612
correct_ang: 0.6592
  (valid)
loss total:  0.8826
loss_pos:    0.0373
loss_ang:    0.8453
correct_ang: 0.8000
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8951
loss_pos:    0.0170
loss_ang:    0.8781
correct_ang: 0.8380
  (valid)
loss total:  0.6904
loss_pos:    0.0433
loss_ang:    0.6471
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6936
loss_pos:    0.0145
loss_ang:    0.6791
correct_ang: 0.9385
  (valid)
loss total:  0.5065
loss_pos:    0.0241
loss_ang:    0.4824
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.5027
loss_pos:    0.0123
loss_ang:    0.4903
correct_ang: 0.9441
  (valid)
loss total:  0.3491
loss_pos:    0.0123
loss_ang:    0.3367
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.3201
loss_pos:    0.0132
loss_ang:    0.3069
correct_ang: 0.9721
  (valid)
loss total:  0.2544
loss_pos:    0.0088
loss_ang:    0.2456
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.1887
loss_pos:    0.0084
loss_ang:    0.1803
correct_ang: 0.9888
  (valid)
loss total:  0.2166
loss_pos:    0.0067
loss_ang:    0.2100
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.1439
loss_pos:    0.0091
loss_ang:    0.1349
correct_ang: 0.9721
  (valid)
loss total:  0.1768
loss_pos:    0.0081
loss_ang:    0.1687
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.0965
loss_pos:    0.0133
loss_ang:    0.0831
correct_ang: 0.9944
  (valid)
loss total:  0.2087
loss_pos:    0.0123
loss_ang:    0.1964
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.0573
loss_pos:    0.0081
loss_ang:    0.0492
correct_ang: 1.0000
  (valid)
loss total:  0.2435
loss_pos:    0.0105
loss_ang:    0.2330
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0509
loss_pos:    0.0065
loss_ang:    0.0444
correct_ang: 0.9944
  (valid)
loss total:  0.2196
loss_pos:    0.0075
loss_ang:    0.2121
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0444
loss_pos:    0.0086
loss_ang:    0.0359
correct_ang: 1.0000
  (valid)
loss total:  0.1980
loss_pos:    0.0062
loss_ang:    0.1918
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0360
loss_pos:    0.0067
loss_ang:    0.0292
correct_ang: 1.0000
  (valid)
loss total:  0.1839
loss_pos:    0.0044
loss_ang:    0.1795
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0249
loss_pos:    0.0051
loss_ang:    0.0198
correct_ang: 1.0000
  (valid)
loss total:  0.1545
loss_pos:    0.0059
loss_ang:    0.1486
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0213
loss_pos:    0.0055
loss_ang:    0.0157
correct_ang: 1.0000
  (valid)
loss total:  0.1436
loss_pos:    0.0052
loss_ang:    0.1384
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0199
loss_pos:    0.0074
loss_ang:    0.0125
correct_ang: 1.0000
  (valid)
loss total:  0.1539
loss_pos:    0.0075
loss_ang:    0.1464
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0162
loss_pos:    0.0066
loss_ang:    0.0097
correct_ang: 1.0000
  (valid)
loss total:  0.2063
loss_pos:    0.0047
loss_ang:    0.2016
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0189
loss_pos:    0.0069
loss_ang:    0.0120
correct_ang: 1.0000
  (valid)
loss total:  0.2318
loss_pos:    0.0106
loss_ang:    0.2212
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0120
loss_pos:    0.0050
loss_ang:    0.0069
correct_ang: 1.0000
  (valid)
loss total:  0.2239
loss_pos:    0.0094
loss_ang:    0.2145
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0133
loss_pos:    0.0077
loss_ang:    0.0056
correct_ang: 1.0000
  (valid)
loss total:  0.1941
loss_pos:    0.0048
loss_ang:    0.1893
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0156
loss_pos:    0.0073
loss_ang:    0.0083
correct_ang: 1.0000
  (valid)
loss total:  0.1911
loss_pos:    0.0052
loss_ang:    0.1859
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0089
loss_pos:    0.0047
loss_ang:    0.0042
correct_ang: 1.0000
  (valid)
loss total:  0.2013
loss_pos:    0.0062
loss_ang:    0.1951
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0158
loss_pos:    0.0041
loss_ang:    0.0116
correct_ang: 1.0000
  (valid)
loss total:  0.2424
loss_pos:    0.0062
loss_ang:    0.2362
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0113
loss_pos:    0.0059
loss_ang:    0.0053
correct_ang: 1.0000
  (valid)
loss total:  0.2312
loss_pos:    0.0054
loss_ang:    0.2258
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0125
loss_pos:    0.0059
loss_ang:    0.0066
correct_ang: 1.0000
  (valid)
loss total:  0.1881
loss_pos:    0.0059
loss_ang:    0.1822
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0086
loss_pos:    0.0059
loss_ang:    0.0027
correct_ang: 1.0000
  (valid)
loss total:  0.1591
loss_pos:    0.0062
loss_ang:    0.1529
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0110
loss_pos:    0.0067
loss_ang:    0.0044
correct_ang: 1.0000
  (valid)
loss total:  0.1410
loss_pos:    0.0067
loss_ang:    0.1343
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0079
loss_pos:    0.0051
loss_ang:    0.0028
correct_ang: 1.0000
  (valid)
loss total:  0.1575
loss_pos:    0.0042
loss_ang:    0.1533
correct_ang: 0.9500
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.141036
  train:
[1.49956, 1.34023, 1.21457, 1.08262, 0.89511, 0.69362, 0.50266, 0.32012, 0.1887, 0.14394, 0.09646, 0.05732, 0.05085, 0.04445, 0.036, 0.02491, 0.02126, 0.01989, 0.01625, 0.0189, 0.01197, 0.0133, 0.01557, 0.00893, 0.01575, 0.01126, 0.0125, 0.00858, 0.01102, 0.00787]
  valid:
[1.43166, 1.36785, 1.11217, 0.8826, 0.69039, 0.50651, 0.34908, 0.25442, 0.21665, 0.1768, 0.20874, 0.24349, 0.21956, 0.19795, 0.18391, 0.15453, 0.14359, 0.15393, 0.20634, 0.23177, 0.22388, 0.19415, 0.19105, 0.20128, 0.24235, 0.23122, 0.18808, 0.15911, 0.14104, 0.15751]

Visualizing performance of best model on validation set:
  19 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
AVERAGE VALIDATION LOSS: 0.104496

Done! Look at this directory for results:
/nfs/diskstation/seita/bedmake_ssl/resnet18_2018-11-18-13-43_000
```
