import requests
#import json
from bs4 import BeautifulSoup
from time import time
from time import sleep


tic = time()

#count_tir = 12818
#count_tir = 10
top_tir = 14194
bottom_tir = 14155
base_url = "https://www.stoloto.ru/7x49/archive/"
list_url = [ base_url + str(i) for i in range(top_tir, bottom_tir-1, -1) ]

def write_result(str):
    r = open("rez.txt", "a")
    r.write(str + '\n')
    r.close()

# def write_result(dd):
#     data_list = []
#     for name in dd:
#         data_list.append(
#             {
#                 "name": name,
#                 "numbers": dd[name]
#             }
#         )
#     with open("rez.json", "a") as file:
#         json.dump(data_list, file, indent=4, ensure_ascii=False)


def response(url):
    req = requests.get(url, allow_redirects=False, verify=True)
    if req.ok:
        return req

def response_code(url):
    try:
        return response(url).status_code
    except:
        return 'Error'

def find_num(url):
    list_num = []
    if response_code(url) == 302:
        url = url.replace('archive', 'archive_old')
    soup = BeautifulSoup(response(url).content, 'html.parser')
    items = soup.findAll('p', {"class": "number"})
    for item in items:
        num = str(item.get_text())
        list_num.append(num)

    return list_num

def iterating_url(list_url):
    dict_tirs = {}
    count = 1
    for url in list_url:
        name_tir = url.split('/')[-1]
        num = find_num(url)
        dict_tirs[name_tir] = num
        write_result(f"{name_tir} - {num}")
        if count == 1:
            write_result('/***********************************************/')
        if count == 5:
            count = 0
            write_result('')
        count += 1
        print(f"{name_tir} - Done!")
        sleep(1)
    #return str



iterating_url(list_url)


print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')