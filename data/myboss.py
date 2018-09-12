#-*-encoding=utf-8-*-
import os
from setting.dataSetting import cfg

outputPath = cfg.SAMPLE_FILE
print(os.path.exists(outputPath))
os.mknod(outputPath)
if os.path.exists(outputPath):
    os.remove(outputPath)
    os.mkdir(outputPath)
    print(os.path.exists(outputPath))