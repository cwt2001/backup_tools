import sys,os
import backup

# 假设第一个命令行参数是gametao指定的配置文件
if len(sys.argv) < 2:
    print("Error")

f = open(sys.argv[1],encoding="utf-8")
lines = f.readlines()
for line in lines:
    [source,dest] = line.split(" ")
    if (not os.path.exists(source)) or (not os.path.exists(dest)):
        print("Error on line : ",line)
        continue

    backup.backup_folder(source,dest)
    backup.backup_folder_update(source,dest)
    