#-*-encoding=utf-8-*-
import os
import cv2
import lmdb
import numpy as np
from setting.dataSetting import cfg

def checkImage(image):
    if image is None:
        return False
    imageBuf = np.fromstring(image, dtype=np.uint8)
    img = cv2.imdecode(imageBuf, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return False
    imgH, imgW = img.shape[0], img.shape[1]
    if imgH * imgW == 0:
        return False
    return True

def writeCache(env, cache):
    with env.begin(write=True) as txn:
        for k, v in cache.items():
            txn.put(k.encode(), v)


def createDataset(outputPath, imagePaths, labelList,checkValid=True):
    assert (len(imagePaths) == len(labelList))
    nSamples = len(imagePaths)
    if os.path.exists(outputPath):
        os.remove(outputPath)
    env = lmdb.open(outputPath)#, map_size=1099511627776
    cache = {}
    cnt = 1
    for i in range(nSamples):
        imagePath = imagePaths[i]
        label = labelList[i]
        if not os.path.exists(imagePath):
            print('%s does not exist' % imagePath)
            continue
        with open(imagePath, 'rb') as f:
            imageBin = f.read()
        if checkValid:
            if not checkImage(imageBin):
                print('%s is not a valid image' % imagePath)
                continue

        imageKey = 'image-%09d' % cnt
        labelKey = 'label-%09d' % cnt
        cache[imageKey] = imageBin
        cache[labelKey] = label.encode()
        if cnt % 1000 == 0:
            writeCache(env, cache)
            cache = {}
            print('Written %d / %d' % (cnt, nSamples))
        cnt += 1
    nSamples = cnt - 1
    cache['num-samples'] = str(nSamples).encode()
    writeCache(env, cache)
    print('Created dataset with %d samples' % nSamples)


def read_text(path):
    with open(path) as f:
        text = f.read()
    text = text.strip()
    return text

if __name__ == '__main__':
    outputPath = cfg.LMDB_CFG.TRAIN_PATH
    path = cfg.SAMPLE_FILE
    imgPaths = []
    labelList = []
    with open(path,'r',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            imgPaths.append(line.split('\t')[0])
            labelList.append(line.split('\t')[1])
    createDataset(outputPath, imgPaths, labelList, checkValid=True)
