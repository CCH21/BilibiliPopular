import os

import pandas as pd

from config import *


def process(file_path):
    _week_data = pd.read_json(file_path)['data']

    update_date = _week_data['config']['name'][:4] + _week_data['config']['label'].split('(')[1][:4]
    update_date = update_date[:4] + '-' + update_date[4:6] + '-' + update_date[6:]
    period = _week_data['config']['label'].split('(')[0][1:-1]
    subject = _week_data['config']['subject']
    share_title = _week_data['config']['share_title']
    share_subtitle = _week_data['config']['share_subtitle']

    rows = []
    for video in _week_data['list']:
        video_info = [update_date, period, subject, share_title, share_subtitle]
        title = video['title']
        tname = video['tname']
        desc = video['desc']
        up = video['owner']['name']
        view = video['stat']['view']
        danmaku = video['stat']['danmaku']
        reply = video['stat']['reply']
        like = video['stat']['like']
        favorite = video['stat']['favorite']
        coin = video['stat']['coin']
        share = video['stat']['share']
        his_rank = video['stat']['his_rank']
        resolution = str(video['dimension']['width']) + '*' + str(video['dimension']['height'])
        try:
            ip = video['pub_location']
        except KeyError:
            ip = ''
        bvid = video['bvid']
        rcmd_reason = video['rcmd_reason']
        video_info.extend([title, tname, desc, up, view, danmaku, reply, like, favorite, coin, share, his_rank,
                           resolution, ip, bvid, rcmd_reason])
        rows.append(video_info)
    return rows


def merge_df():
    _df = pd.DataFrame(columns=COLUMNS)
    for i in range(1, NUM):
        file_path = RAW_DATA_FOLDER + 'week_{}.json'.format(i)
        rows = process(file_path=file_path)
        df_insert = pd.DataFrame(rows)
        df_insert.columns = COLUMNS
        _df = pd.concat([_df, df_insert], axis=0, ignore_index=True)
    return _df


def main():
    print('[INFO] 准备处理Bilibili每周必看数据...')
    if not os.path.exists(PROCESSED_DATA_FOLDER):
        os.mkdir(PROCESSED_DATA_FOLDER)
        print('[INFO] 已建立存储数据目录，路径为{}'.format(PROCESSED_DATA_FOLDER))
    else:
        print('[INFO] 存储数据目录路径为{}'.format(PROCESSED_DATA_FOLDER))
    output_file_path = PROCESSED_DATA_FOLDER + PROCESSED_DATA_FILE
    df = merge_df()
    print('[INFO] 处理后的DataFrame如下：')
    print(df)
    df.to_csv(output_file_path, index=False)
    print('[INFO] 数据处理完成')


if __name__ == '__main__':
    main()
