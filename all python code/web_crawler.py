import urllib.request as req

# fb台大百大正妹粉專網址
src = "https://www.facebook.com/NTU100Beauty/"

# 建立一個Request物件，附加Request headers的資訊
request = req.Request(src, headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 解析網站原始碼，取得篇文章的標題
from bs4 import BeautifulSoup
root = BeautifulSoup(data, "html.parser") # 使用 BeautifulSoup 協助解析 HTML 格式的文件
title = root.find("title") #, class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q")  # 尋找所有 class="title"的div標籤，匯集成一個 list

print(title)
'''
for title in titles: 
    if title.a != None:  # 如果標題包含 a 標籤(沒有被刪除)
        print(title.a.string)
'''