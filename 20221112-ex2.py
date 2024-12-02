import zipfile
import re
from concurrent.futures import as_completed,ProcessPoolExecutor
import multiprocessing
import winprocess

def read_data(filename):
    total = 0
    with zipfile.ZipFile(filename) as zipfp:
        with zipfp.open(zipfp.namelist()[0],'r') as fp:
            for a_line in fp.readlines():
                a_line = a_line.decode('utf-8')
                for number in re.finditer(r'(\d+(\.?\d*)|\.\d+)',a_line):
                    total += float(number.group())
    return total
                    
print(read_data('ex2_1.zip'))

if __name__ == '__main__':
    total = 0
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures= [winprocess.submit(executor, read_data, f)  for f in ['ex2_1.zip','ex2_2.zip','ex2_3.zip','ex2_4.zip','ex2_5.zip']]
    for future in as_completed(futures):
        total += future.result()
    print(total)