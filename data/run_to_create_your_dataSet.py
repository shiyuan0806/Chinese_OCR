#-*-encoding=utf-8-*-

import writeToLMDB
import genData
import xlrd
from setting.dataSetting import cfg

def genYourData(dataType,dataNum):
    workbook = xlrd.open_workbook(r'national.xls')
    fontName = cfg.FONTTYPE
    if dataType=='Adress':
        genData.genImageFromAddress(workbook,fontName,dataNum)
    else:
        genData.genImageFromAlphabet(fontName,dataNum)

def wirteLmdb():
    outputPath = cfg.LMDB_CFG.TRAIN_PATH
    path = cfg.SAMPLE_FILE
    imgPaths = []
    txtLists = []
    with open(path,'r',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            imgPaths.append(line.split('\t')[0])
            txtLists.append(line.split('\t')[1])
    writeToLMDB.createDataset(outputPath, imgPaths, txtLists, checkValid=True)

if __name__=="__main__":
    dataType = "wb"
    dataNum = 10
    genYourData(dataType,dataNum)
    wirteLmdb
