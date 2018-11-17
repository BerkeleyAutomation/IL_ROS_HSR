# Tentative Results


Here is a sample output, from running:

```
(py2-torch) seita@hermes1:~/IL_ROS_HSR/src/il_ros_hsr/nets$ python train_action_predictor.py  --num_epochs 30
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
