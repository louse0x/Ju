import shutil,os

with os.scandir('log') as entries:
    for entry in entries:
        print(entry.name)
        os.remove(entry)