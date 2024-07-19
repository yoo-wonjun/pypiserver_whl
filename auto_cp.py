import os
from time import sleep, time

def auto_copy():
    try:
        base_dir = 'dist'
        base_file_list = os.listdir(base_dir)
        while True:
            sleep(5)
            after_base_file_list = os.listdir(base_dir)
            a = [i for i in after_base_file_list if i not in base_file_list]
            if len(a) != 0:
                for i in a:
                    os.system(f"cp {os.path.join(base_dir, i)} packages")
            base_file_list = after_base_file_list
            
if __name__=='__main__':
    auto_copy()