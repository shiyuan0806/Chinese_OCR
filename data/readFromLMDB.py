#-*-encoding=utf-8-*-
import lmdb  # install lmdb by "pip install lmdb"
from setting.dataSetting import cfg

outputPath = cfg.LMDB_CFG.TRAIN_PATH
env = lmdb.open(outputPath)
txn = env.begin(write=True)
for key, value in txn.cursor():
    print(key,value)
env.close()