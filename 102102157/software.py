from collections import Counter

import requests
import json

from danmu import get_barrage
#创建一个新列表，用来存放爬取的弹幕
barrage_list = []

url = "https://api.bilibili.com/x/web-interface/wbi/search/type?page_size=50&keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%9F%93%E6%B0%B4%E6%8E%92%E6%B5%B7&search_type=video"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
}
cookies = {
    "LIVE_BUVID": "AUTO4016261546844610",
    "dy_spec_agreed": "1",
    "i-wanna-go-back": "-1",
    "buvid_fp_plain": "undefined",
    "CURRENT_BLACKGAP": "0",
    "buvid3": "DB924180-3BD8-42B5-8BA2-4C8E6CD0802A148811infoc",
    "blackside_state": "0",
    "is-2022-channel": "1",
    "buvid4": "7FDFFDBD-4A05-CE5B-36F8-65644EF23BAA01057-022012119-AriTOoXUlusyf%2FPJFVaFQQ%3D%3D",
    "fingerprint3": "a5079b7c6bbff612db4a71d0b5309f09",
    "_uuid": "1895FF54-38108-F76E-425C-67F7D2649F2D79892infoc",
    "b_nut": "100",
    "rpdid": "|(k|ul)))|)J0J'uYY)l~~uku",
    "b_ut": "5",
    "CURRENT_PID": "6064c9b0-cd27-11ed-9166-4964fac53142",
    "nostalgia_conf": "-1",
    "hit-new-style-dyn": "1",
    "hit-dyn-v2": "1",
    "CURRENT_FNVAL": "4048",
    "FEED_LIVE_VERSION": "V8",
    "buvid_fp": "fa328c199106d855c503e19e77cfd2e5",
    "PVID": "5",
    "header_theme_version": "CLOSE",
    "CURRENT_QUALITY": "120",
    "fingerprint": "df225497cabdc8de8b5d4ffa4c5f3b07",
    "home_feed_column": "5",
    "b_lsid": "12946BB1_18A6F60043F",
    "browser_resolution": "1456-797",
    "sid": "4x0efj2f",
    "bp_video_offset_457472714": "838573964930318341"
}

for i in range(6):
    sess = requests.session()
    req = sess.get(url + "&page=" + str(i+1), headers=headers, cookies=cookies)
    res = json.loads(req.text)
    for video in res['data']['result']:
        barrage_list = barrage_list + get_barrage(video['bvid'],headers)


a = open("barrage.txt","r",encoding="utf-8")
for line in a.readlines():
    line = line.strip("\n")
    barrage_list.append(line)

barrage_counter = Counter(barrage_list) #：这是Python内置的计数器（counter）类，它用于对可迭代对象中的元素进行计数。在这段代码中，barrage_counter = Counter(barrage_list)将弹幕列表中的每个元素进行计数，返回一个包含元素及其对应计数的字典。
sorted_danmu = sorted(barrage_counter.items(), key=lambda x: x[1], reverse=True)
for i in range(20):
    print(sorted_danmu[i]) #这是Python内置的排序函数，用于对可迭代对象进行排序。在这段代码中，sorted_danmu = sorted(barrage_counter.items(), key=lambda x: x[1], reverse=True)对计数器对象中的元素进行排序，按照计数值从大到小排列，并将结果存储在列表sorted_danmu中。
    print(sorted_danmu[i][0])
