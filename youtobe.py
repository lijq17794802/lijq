# coding-utf-8
# ------lijianquan-------
# Email:lijianquan0211@gmail.com
#  获取网站的图片示例

import requests
from lxml import etree # 数据预处理
# import lxml
from urllib import request  # xiazai tupian
import time # 延迟时间，模拟人的操作

def store_raw_images():

url = 'https://www.huya.com/g/4079'
# url = 'http://k6.csnmdcjnx.xyz/pw/html_data/14/2003/4650288.html'
# neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
# neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
response = requests.get(url,headers=headers)
print(response) # <Response [200]>
data_txt = response.text
# print (data_txt)
data = etree.HTML(data_txt)

    friends_list = data.xpath('//img[@class="pic"]')

    print (friends_list)

    for friend in friends_list:
        img = friend.xpath('./@data-original')[0]
        # print (img)

        img = img.split('?')[0]
        print (img)
        name = friend.xpath('./@alt')[0]
        request.urlretrieve(img,'C:/Users/PC/Desktop/ffff/'+name+'.jpg')
        print('<%s>下载完毕!!!!!!!'% name)

        # 为了防止被网站拉黑，模拟人的操作，延迟2秒
        time.sleep(2)


    # if not os.path.exists('nge'):
     #    os.makedirs('neg')



store_raw_images()