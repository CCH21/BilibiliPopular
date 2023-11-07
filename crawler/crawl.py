import json
import os
import time

from fake_useragent import UserAgent
import requests
from retrying import retry

from config import *


@retry()
def get_data(url, save_path):
    headers = {
        'User-Agent': UserAgent().random,
        'Origin': ORIGIN,
        'Referer': REFERER
    }
    response = requests.get(url=url, headers=headers, timeout=10)
    json_data = response.json()
    with open(file=save_path, mode='w', encoding='utf-8') as output_file:
        json.dump(obj=json_data, fp=output_file, ensure_ascii=False)
    time.sleep(1)


def main():
    print('[INFO] 准备抓取Bilibili每周必看数据...')
    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)
        print('[INFO] 已建立存储数据目录，路径为{}'.format(DATA_FOLDER))
    else:
        print('[INFO] 存储数据目录路径为{}'.format(DATA_FOLDER))
    for i in range(1, NUM):
        start_time = time.time()
        url = URL + str(i)
        save_path = os.path.join(DATA_FOLDER, 'week_{}.json'.format(i))
        print('[INFO] 正在抓取第{}期Bilibili每周必看数据...'.format(i))
        get_data(url=url, save_path=save_path)
        end_time = time.time()
        print('[INFO] 第{}期Bilibili每周必看数据已抓取完成，用时{:.3f}s'.format(i, end_time - start_time))
    print('[INFO] 抓取Bilibili每周必看数据完成')


if __name__ == '__main__':
    main()
