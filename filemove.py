import os
import shutil
import sys
import time

def renameimg(dirname,target_raw):
    if not os.path.isdir(dirname):
        input(f"文件夹不存在:{dirname}，按回车键关闭")
        return
    target=os.path.join(dirname,target_raw)
    if not os.path.exists(target):
        os.mkdir(target)
        #print(f"目标文件夹 {target} 不存在")
        #sys.exit()
    n=0
    for foldername, subfolders, filenames in os.walk(dirname):
        if foldername == target_raw:
            continue
        wen1 = os.path.basename(foldername)
        for filename in filenames:
            if filename.endswith((".jpg", ".png", ".webp", ".gif")):
                n += 1
                b, extension = os.path.splitext(filename)
                print(f'{b=},{wen1=},{subfolders=},{foldername=}')
                newname = str(int(wen1) * 100 + int(b)) + extension
                src = os.path.join(foldername, filename)
                dst = os.path.join(dirname, "1", newname)
                if os.path.exists(dst):
                    newname = str(int(wen1) * 100 + int(b)) + '-' + str(time.time()) + extension
                    dst = os.path.join(dirname, "1", newname)
                shutil.copyfile(src, dst)
                print(f"文件 {foldername}/{filename} 重命名为 {newname}，并复制到文件夹 {target} 下")
    if n ==0:
        input("\n将该程序放在要处理的文件夹下，双击开始执行\n其他文件夹下的图片，将被重命名为 所在文件夹名*100+图片名，然后复制到 1 文件夹下")
        return
    input(f"按回车键关闭窗口...，共处理图片 {n} 张")



# 调用示例

dirname=os.getcwd()
target="1"
if len(sys.argv)==2:
    dirname=sys.argv[1]
if len(sys.argv)==3:
    target=sys.argv[2]

renameimg(dirname,target)
