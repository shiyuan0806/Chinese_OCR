from easydict import EasyDict as edict

_D = edict()
#you can get config by from dataSetting import cfg
cfg = _D

#output path of images
_D.OUTPUT_PATH = "images/"
#font type of text in generating images
_D.FONTTYPE = "font_type/black/huaWenXiHei.ttf"
#path of sample.txt
_D.SAMPLE_FILE = "images/sample.txt"

#black white background
_D.BW_CFG = edict()
_D.BW_CFG.FONTSIZE = 15

#idcard BackGround
_D.IDCARD_CFG = edict()
_D.IDCARD_CFG.BG_BASE_PATH = "id_background/"

#setting of lmdb
_D.LMDB_CFG = edict()
_D.LMDB_CFG.TRAIN_PATH = "lmdb_data/train/"
_D.LMDB_CFG.TEST_PATH = "lmdb_data/test/"






