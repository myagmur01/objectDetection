 
#### Object Detection by Tensorflow Object Detection API 
 - Workshop Tutorial
 - August 2, 2018
 
![alt text](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/img/kites_detections_output.jpg "kites")

---

- About the Repo
   * API     : Tensorflow's Object Detection API
   * ckpt    : trained model parameters saved
   * config  : Configuration settings
   * eval    : Evaluation result folder
   * figures : helper figures for understanding Faster-RCNN
   * frozen_model : Inference graph of trained model
   * images : 
      * train/val/test data
      * converted csv files
      * converted tfrecord files
      * labelmap.pbtxt : defines labels
   * pretrained   : Pretrained model parameters 

---
 
## 1. Introduction

### 1.1. Datasets
--> [Datasets](https://www.analyticsvidhya.com/blog/2018/03/comprehensive-collection-deep-learning-datasets/)
- COCO
- KITTI
- Pascal
- Oid
- AVA v2.1 trained models
- Open Images-trained models

### 1.2. Landmark Papers

>> 2-Stage Detectors
 - [Mask-RCNN](Link here)
 - [Faster-RCNN](Link here)
 - [Fast-RCNN](Link here)
 - [RCNN](Link here)
 - [Selective Search](Link here)
 
>> 1-Stage Detectors
 - [YOLO](Link here)
 - [SSD](Link here)
 - [OverFeat](Link here)

>> Review
 - [Trade-off](Link here)


### 1.3. Architectures

- VGG
- ZFNet
- MobileNet
- Inception
- ResNet
- DenseNet



## 2. Prepare Input Pipeline

### 2.1.Download Images

>> Google Advanced Image Search
 - birds , tigers , rabbits etc..
 
>> Downloader Tools (Chrome Extensions):
 - Download All Images 2.0.4
 - Fatkun Batch Download Image 2.23


### 2.2. Annotate Objects

- Bounding Box
--> [LabelImg](https://github.com/tzutalin/labelImg)
- Polygon
- Semantic Segmentation
- Bounding Box
- Line

### 2.3. Data Format Conversion

- xml_to_csv
- csv_to_tfrecord
- resizer
- extension check
- size check

### 2.4. API Introduction

 - [Download API](Link here)
 - [configuration files](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs)
 - [configuration settings](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/configuring_jobs.md)
 - [models/research/object_detection/g3doc/detection_model_zoo.md](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)

## 3. Set Colab Environment

 - Install Requirements
 - Connect Drive
 - Clone Repository
 - Set python environment
 - train
 - ..


## 4. Useful Links (References)
- [Protobuf](https://towardsdatascience.com/3-steps-to-update-parameters-of-faster-r-cnn-ssd-models-in-tensorflow-object-detection-api-7eddb11273ed)
- [BlogPost](https://blog.playment.io/comparing-image-annotation-types/)

