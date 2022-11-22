"""object process"""
import glob
import shutil
import os
source_path = '../source/*'
postfix = [1, 6, 12, 5]
while True:
    source_object = glob.glob(source_path)

    if source_object:

        for single_path in source_object:

            shutil.copy(single_path, '.')
            fst, sec = single_path.split("\\")[-1].split(".")

            for preName in postfix:
                shutil.copy(single_path.split("\\")[-1], '../destination/'+f'{fst}_{preName}.{sec}')

            os.remove(single_path)
            os.remove(single_path.split("\\")[-1])
