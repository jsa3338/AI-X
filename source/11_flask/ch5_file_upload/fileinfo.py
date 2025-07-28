import os
import datetime

UPLOAD_FOLDER = './uploads/'
filelist= os.listdir(UPLOAD_FOLDER) # 해당 폴더의 파일 이름 목록
# print(filelist)

def stamp2datetime(stamp):
    return datetime.datetime.fromtimestamp(stamp)

def info(file):
    ctime = os.path.getctime(UPLOAD_FOLDER + file) # 파일의 생성시간
    mtime = os.path.getmtime(UPLOAD_FOLDER + file) # 파일의 최종 수정시간
    atime = os.path.getatime(UPLOAD_FOLDER + file) # 파일의 최종 접근시간
    size = os.path.getsize(UPLOAD_FOLDER + file)   # 파일의 크기(byte)
    if size >= 1024 * 1024: # 1024 byte = 1 MB
        size = size / (1024 * 1024)
        size = '%.2f MB' % size
    elif size >= 1024:
        size = size / 1024
        size = "{:.2f} KB".format(size)
    else:
        size = "{} bytes".format(size)
    return stamp2datetime(ctime), stamp2datetime(mtime), stamp2datetime(atime), size

if __name__ == '__main__':
    filelist= os.listdir(UPLOAD_FOLDER) # 해당 폴더의 파일 이름 목록
    for file in filelist:
        ctime, mtime, atime, size = info(file)
        print(file, ctime, mtime, atime, size)