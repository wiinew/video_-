import re
import requests
#import json
import pprint
from tqdm import tqdm
import itertools
import  selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import tkinter as tl

useragents={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
useragent={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'}
io=[["name", "纯净/B站", "category",1, "url", "https://z1.m1907.cn/?jx=", "showType", 3],["name", "高速接口", "category", 1, "url","https://jsap.attakids.com/?url=", "showType",3],["name", "综合/B站", "category", 1, "url", "https://vip.parwix.com:4433/player/?url=", "showType", 3],
    ["name", "OK解析", "category",1, "url", "https://okjx.cc/?url=", "showType",3],["name","夜幕", "category", 1, "url","https://www.yemu.xyz/?url=", "showType", 3],["name","playerjy/B站", "category", 1, "url","https://jx.playerjy.com/?url=", "showType",3],["name", "乐多资源", "category", 1, "url","https://api.leduotv.com/wp-api/ifr.php?isDp=1&vid=", "showType", 3],
    ["name","虾米", "category",1, "url","https://jx.xmflv.com/?url=", "showType", 3],["name","M3U8.TV", "category",1, "url","https://jx.m3u8.tv/jiexi/?url=", "showType", 3],["name","人人迷", "category",1, "url", "https://jx.blbo.cc:4433/?url=", "showType", 3],["name", "全民", "category", 1, "url", "https://jx.blbo.cc:4433/?url=", "showType", 3],["name","七哥", "category",1, "url","https://jx.mmkv.cn/tv.php?url=", "showType", 3],["name", "冰豆", "category", 1, "url","https://api.qianqi.net/vip/?url=", "showType", 3],["迪奥", "category", 1, "url", "https://123.1dior.cn/?url=", "showType", 3],["name","CK", "category",1, "url", "https://www.ckplayer.vip/jiexi/?url=", "showType",3],["name","游艺", "category",1, "url", "https://api.u1o.net/?url=", "showType",3],["name", "游艺", "category",1, "url","https://api.u1o.net/?url=", "showType", 3],["name", "ckmov", "category", 1, "url", "https://www.ckmov.vip/api.php?url=", "showType",3],["name", "ccyjjd", "category", 1, "url","https://ckmov.ccyjjd.com/ckmov/?url=", "showType", 3],["name", "诺诺", "category", 1, "url", "https://www.ckmov.com/?url=", "showType", 3],["name", "爱豆", "category", 1, "url", "https://jx.aidouer.net/?url=", "showType",3],["name", "H8", "category", 1, "url","https://www.h8jx.com/jiexi.php?url=", "showType", 3],["name", "BL", "category",1, "url", "https://vip.bljiex.com/?v=", "showType", 3],["name","解析la", "category",1, "url", "https://api.jiexi.la/?url=", "showType", 3],["name","黑米", "category",1, "url", "https://www.myxin.top/jx/api/?url=", "showType",1],["name","综合线路解析", "category",2, "url", "https://www.xixicai.top/mov/s/?sv=3&url=", "showType", 1]]
originalInterfaceList = [
        {"name": "纯净/B站", "category": 1, "url": "https://z1.m1907.cn/?jx=", "showType": 3},
        {"name": "高速接口", "category": 1, "url": "https://jsap.attakids.com/?url=", "showType": 3},
        {"name": "综合/B站", "category": 1, "url": "https://vip.parwix.com:4433/player/?url=", "showType": 3},
        {"name": "OK解析", "category": 1, "url": "https://okjx.cc/?url=", "showType": 3},
        {"name": "夜幕", "category": 1, "url": "https://www.yemu.xyz/?url=", "showType": 3},
        {"name": "playerjy/B站", "category": 1, "url": "https://jx.playerjy.com/?url=", "showType": 3},
        {"name": "乐多资源", "category": 1, "url": "https://api.leduotv.com/wp-api/ifr.php?isDp=1&vid=", "showType": 3},
        {"name": "虾米", "category": 1, "url": "https://jx.xmflv.com/?url=", "showType": 3},
        {"name": "M3U8.TV", "category": 1, "url": "https://jx.m3u8.tv/jiexi/?url=", "showType": 3},
        {"name": "人人迷", "category": 1, "url": "https://jx.blbo.cc:4433/?url=", "showType": 3},
        {"name": "全民", "category": 1, "url": "https://jx.blbo.cc:4433/?url=", "showType": 3},
        {"name": "七哥", "category": 1, "url": "https://jx.mmkv.cn/tv.php?url=", "showType": 3},
        {"name": "冰豆", "category": 1, "url": "https://api.qianqi.net/vip/?url=", "showType": 3},
        {"name": "迪奥", "category": 1, "url": "https://123.1dior.cn/?url=", "showType": 3},
        {"name": "CK", "category": 1, "url": "https://www.ckplayer.vip/jiexi/?url=", "showType": 3},
        {"name": "游艺", "category": 1, "url": "https://api.u1o.net/?url=", "showType": 3},
        {"name": "LE", "category": 1, "url": "https://lecurl.cn/?url=", "showType": 3},
        {"name": "ckmov", "category": 1, "url": "https://www.ckmov.vip/api.php?url=", "showType": 3},
        {"name": "ccyjjd", "category": 1, "url": "https://ckmov.ccyjjd.com/ckmov/?url=", "showType": 3},
        {"name": "爱豆", "category": 1, "url": "https://jx.aidouer.net/?url=", "showType": 3},
        {"name": "诺诺", "category": 1, "url": "https://www.ckmov.com/?url=", "showType": 3},
        {"name": "H8", "category": 1, "url": "https://www.h8jx.com/jiexi.php?url=", "showType": 3},
        {"name": "BL", "category": 1, "url": "https://vip.bljiex.com/?v=", "showType": 3},
        {"name": "解析la", "category": 1, "url": "https://api.jiexi.la/?url=", "showType": 3},
        {"name": "MUTV", "category": 1, "url": "https://jiexi.janan.net/jiexi/?url=", "showType": 3},
        {"name": "MAO", "category": 1, "url": "https://www.mtosz.com/m3u8.php?url=", "showType": 3},
        {"name": "老板", "category": 1, "url": "https://vip.laobandq.com/jiexi.php?url=", "showType": 3},
        {"name": "盘古", "category": 1, "url": "https://www.pangujiexi.cc/jiexi.php?url=", "showType": 3},
        {"name": "盖世", "category": 1, "url": "https://www.gai4.com/?url=", "showType": 3},
        {"name": "小蒋", "category": 1, "url": "https://www.kpezp.cn/jlexi.php?url=", "showType": 3},
        {"name": "YiTV", "category": 1, "url": "https://jiexi.us/?url=", "showType": 3},
        {"name": "星空", "category": 1, "url": "http://60jx.com/?url=", "showType": 1},
        {"name": "0523", "category": 1, "url": "https://go.yh0523.cn/y.cy?url=", "showType": 1},
        {"name": "17云", "category": 1, "url": "https://www.1717yun.com/jx/ty.php?url=", "showType": 1},
        {"name": "4K", "category": 1, "url": "https://jx.4kdv.com/?url=", "showType": 1},
        {"name": "云析", "category": 1, "url": "https://jx.yparse.com/index.php?url=", "showType": 1},
        {"name": "8090", "category": 1, "url": "https://www.8090g.cn/?url=", "showType": 1},
        {"name": "江湖", "category": 1, "url": "https://api.jhdyw.vip/?url=", "showType": 1},
        {"name": "诺讯", "category": 1, "url": "https://www.nxflv.com/?url=", "showType": 1},
        {"name": "PM", "category": 1, "url": "https://www.playm3u8.cn/jiexi.php?url=", "showType": 1},
        {"name": "奇米", "category": 1, "url": "https://qimihe.com/?url=", "showType": 1},
        {"name": "思云", "category": 1, "url": "https://jx.ap2p.cn/?url=", "showType": 1},
        {"name": "听乐", "category": 1, "url": "https://jx.dj6u.com/?url=", "showType": 1},
        {"name": "aijx", "category": 1, "url": "https://jiexi.t7g.cn/?url=", "showType": 1},
        {"name": "52", "category": 1, "url": "https://vip.52jiexi.top/?url=", "showType": 1},
        {"name": "黑米", "category": 1, "url": "https://www.myxin.top/jx/api/?url=", "showType": 1},
        {"name": "豪华啦", "category": 1, "url": "https://api.lhh.la/vip/?url=", "showType": 1},
        {"name": "凉城", "category": 1, "url": "https://jx.mw0.cc/?url=", "showType": 1},
        {"name": "33t", "category": 1, "url": "https://www.33tn.cn/?url=", "showType": 1},
        {"name": "180", "category": 1, "url": "https://jx.000180.top/jx/?url=", "showType": 1},
        {"name": "无名", "category": 1, "url": "https://www.administratorw.com/video.php?url=", "showType": 1},
        {"name": "黑云", "category": 1, "url": "https://jiexi.380k.com/?url=", "showType": 1},
        {"name": "九八", "category": 1, "url": "https://jx.youyitv.com/?url=", "showType": 1},

        {"name": "综合线路解析", "category": 2, "url": "https://www.xixicai.top/mov/s/?sv=3&url=", "showType": 1},
        {"name": "纯净/B站", "category": 2, "url": "https://z1.m1907.cn/?jx=", "showType": 1},
        {"name": "高速接口", "category": 2, "url": "https://jsap.attakids.com/?url=", "showType": 1},
        {"name": "综合/B站1", "category": 2, "url": "https://vip.parwix.com:4433/player/?url=", "showType": 1},
        {"name": "OK解析", "category": 2, "url": "https://okjx.cc/?url=", "showType": 1},
        {"name": "夜幕", "category": 2, "url": "https://www.yemu.xyz/?url=", "showType": 1},
        {"name": "虾米", "category": 2, "url": "https://jx.xmflv.com/?url=", "showType": 1},
        {"name": "全民", "category": 2, "url": "https://jx.quanmingjiexi.com/?url=", "showType": 1},
    ]
def M3U8_qq():
    global url, name, data
    url = 'https://vd.l.qq.com/proxyhttp'
    # yus=input()
    # datas=yus
    # print(datas)
    name = input('请输入文件name')
    data = {"buid": "vinfoad",
            "adparam": "pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fm441e3rjq9kwpsc.html&refer=https%3A%2F%2Fv.qq.com%2Fchannel%2Fcartoon&ty=web&plugin=1.0.0&v=3.5.57&coverid=m441e3rjq9kwpsc&vid=m00253deqqo&pt=&flowid=951905524fa089c2b2873c11c7c44a43_10201&vptag=www_baidu_com%7Cchannel&pu=-1&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=367321efb865a817b4fce835298c6426&req_type=1&from=0&appversion=1.0.174&lt=qq&platform=10201&tpid=3",
            "vinfoparam": "spsrt=1&charge=0&defaultfmt=auto&otype=ojson&guid=367321efb865a817b4fce835298c6426&flowid=951905524fa089c2b2873c11c7c44a43_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fm441e3rjq9kwpsc.html&refer=v.qq.com&sphttps=1&tm=1655126589&spwm=4&logintoken=&vid=m00253deqqo&defn=&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&drm=32&hdcp=1&spau=1&spaudio=15&defsrc=1&encryptVer=9.1&cKey=E-E5SuGudVB6KJEItZs_lpJX5WB4a2CdS8kH5OVmVaqtHEZQ1c_W6myJ8hQAnmDDGMN6HtSKNTvm2vPBr-xE-uhvZyEMY131vUh1H4pgCXe2Op9Lrzb_fbB32kFt6bl1q30sVBkIXYfWkOdABnbLUo4RgzSXkBHF3N3K7dNKPg_56X9JO3gwBMyBeAex05x8SbbQKY5AXaDVSM7hsBQ8XEeHzIEGJzlCt8VJJAjXQisjKvQ6nZ9BrwFprdnifPDW3nfhDvrdkCkJhrZ4JUBeuGEk8zAOhE9HTZPNDViLRIyt2mNDud09qSLLKl4XAj3FR6vg6-bWRHo5h_ua7HiGyDkZjRppZdC9KQsnUpP_C6F30g1dTsIgANVL7n2uPnMBWUtpFA&fp2p=1&spadseg=3"}
    userage = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'}
    request = requests.post(url=url, json=data, headers=userage)
    pprint.pprint(request.json())
    M3U8 = request.json()['vinfo']
    pprint.pprint(M3U8)
    HTML = re.compile('https://.*?"')
    urls = re.findall(HTML, M3U8)[5]
    pprint.pprint(urls)
    m3u8_data = requests.get(url=urls).text
    # print(m3u8_data)
    m3u8_data = re.sub('#EXTM3U', '', m3u8_data)
    m3u8_data = re.sub('EXT-X-VERSION:\d', '', m3u8_data)
    m3u8_data = re.sub('#EXT-X-MEDIA-SEQUENCE:\d', '', m3u8_data)
    m3u8_data = re.sub('#EXT-X-TARGETDURATION:\d+', '', m3u8_data)
    m3u8_data = re.sub('#EXT-X-PLAYLIST-TYPE:VOD', '', m3u8_data)
    m3u8_data = re.sub('#EXTINF:\d+\.\d+,', '', m3u8_data)
    print(m3u8_data)
    for ts in tqdm(m3u8_data):
        ts_url = 'https://ltsjdy.qq.com/sII_w29-yzp2C_-l_zBaZ0lrGGGnEI14jI9n3CiaXfgfIdT2KGnCUyPX1BN2SGkz-AkQQMh7v9FGeEJEX65G3uZYyqeZ6jWJDxe7CKQXnGi9IeyB-iINn2rA5-Pih_MblT_0-9K8xTbNctx7eIDoB4ro2VMMU5SmMv9uWw6hfAohY8R0wiXdXQ/' + ts
        print(ts_url)
        ts_contect = requests.get(url=ts_url).content
        with open(name + 'mp4', mode='ab') as fp:
            fp.write(ts_contect)
    print('下载OK')
def xml():
    for i in range(len(io)):
        print(i,io[i][1])
    url = input('请输入你想要的解析器')
    print(io[int(url)][1],io[int(url)][5])
    pol=io[int(url)][5]
    key=input('请输入您要解析的网站')
    urls=pol+key
    print('您解析的网址',urls)
def  JeXi():
    #documents = set()
  """print(originalInterfaceList)
    url_text=list(itertools.chain.from_iterable(originalInterfaceList))"""
  print('请选择 1 xml 2 web ')
  opo=input()
  if opo=='1':
     xml()
  elif opo=='2':
    for i in range(len(io)):
        print(i,io[i][1])
    root = tl.Tk()
    root.geometry('300x180')
    root.title('解析器')
    username = tl.StringVar()
    password = tl.StringVar()
    page = tl.Frame(root)
    page.pack()
    tl.Label(page).grid(row=0, column=0)
    tl.Label(page, text='选择的解析器:').grid(row=1, column=1, pady=10)
    tl.Entry(page, textvariable=username).grid(row=1, column=2)
    tl.Label(page, text='网址:').grid(row=2, column=1, pady=10)
    tl.Entry(page, textvariable=password).grid(row=2, column=2)


    def login():
        name = username.get()
        pwd = password.get()
        ol = io[int(name)][1], io[int(name)][5]
        ols = io[int(name)][5] + str(pwd)
        print(str(ols))

    tl.Button(page, text='解析', command=login).grid(row=3, column=2, pady=10)
    root.mainloop()
    """requy=requests.get(urls,headers=useragent).text
    print(requy)"""

    """ io=io.extend(documents.intersection(url_text))
    pprint.pprint(io)"""

if __name__=='__main__':
 while True:
   JeXi()
   """root=tl.Tk()
   root.geometry('300x180')
   root.title('解析器')
   username = tl.StringVar()
   password = tl.StringVar()
   page=tl.Frame(root)
   page.pack()
   tl.Label(page).grid(row=0,column=0)
   tl.Label(page,text='选择的解析器:').grid(row=1,column=1,pady=10)
   tl.Entry(page,textvariable=username).grid(row=1,column=2)
   tl.Label(page, text='网址:').grid(row=2, column=1,pady=10)
   tl.Entry(page,textvariable=password).grid(row=2, column=2)
   def login():
       name = username.get()
       pwd = password.get()
       ol=io[int(name)][1],io[int(name)][5]
       ols=io[int(name)][5]+str(pwd)
       print(ols)
   tl.Button(page,text='解析',command=login).grid(row=3,column=2,pady=10)
   root.mainloop()"""
   """ wd=webdriver.Chrome(service=Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'))
    #wd.get('https://www.ckmov.com/?url=https://v.qq.com/x/cover/sifd2an7kx2h9h8.html')
    wd.get('https://www.baidu.com')
"""

#M3U8_qq()