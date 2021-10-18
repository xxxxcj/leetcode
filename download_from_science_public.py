# coding: utf8

import urllib.request
import os
import time
import random

def download_img(img_url, api_token, page, bookname):
    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        img_name = "%s.png"%page
        filename = "D:\\book\\%s\\"%bookname+ img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed"

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    path=path.rstrip("\\")

    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False

def get_FileSize(filePath):

    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024)

    return round(fsize, 2)

if __name__ == '__main__':
    # 下载要的图片
    api_token = ""  # "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
    bookname = input("请输入书名：")
    if not mkdir("D:\\book\\%s\\"%bookname):
        exit(0)
    asserts = input("请输入asserts,如果不知道,通过book.sciencereading.cn中的对应图书F12,网络,然后打印某个页面,查看请求网址获得：\n")
    totalpage = int(input("请输入总页数:"))
    page = 0
    while page < totalpage:
        img_url = "http://159.226.241.32:8093/asserts/%s/image/%s/100?accessToken=accessToken&formMode=true"%(asserts,page)
        status = download_img(img_url, api_token, page, bookname)
        if status[0] != 'f':
            if get_FileSize(status) <= 10:
                print("error")
                page -= 1
            else:
                print("download ", status, " success!")
        else:
            print("failed")
        time.sleep(1+random.random())
        page += 1
