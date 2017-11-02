import os
import shutil

#搜索apk文件并复制到目标目录
def checkApkFile (srcPath,destPath):
    files = os.listdir(srcPath)
    for file in files:
        if file.lower().endswith(".apk"):
            oldFile=srcPath+"\\"+file
            newFile=destPath+"\\"+file
            if os.path.exists(newFile):
                os.remove(newFile)
            print("copy " + file,end=" ")
            shutil.copyfile(oldFile,newFile)
            print("success")

#搜索release目录并在其目录下检测apk文件
def checkReleaseDir (srcPath,destPath):
    files = os.listdir(srcPath)
    isTragetDir=False
    for file in files:
        if "release" == file.lower():
            releaseDir=srcPath+"\\"+file
            checkApkFile(releaseDir,destPath)
            isTragetDir=True
    if isTragetDir:#删除目录
        shutil.rmtree(srcPath,True)

#返回当前工作目录
curPath=os.getcwd()

#打印当前工作目录
print(curPath)

#创建目录
releasePath=curPath+"\\Release"
if not os.path.exists(releasePath):
    os.mkdir(releasePath)

#收集当前目录所有的文件及目录
files=os.listdir(curPath)

#遍历
for f1 in files:
    filePath = curPath + "\\" + f1
    if os.path.isdir(filePath):#如果是目录，则进一步检测目录下是否有Release目录
        checkReleaseDir(filePath,releasePath)

print("end")