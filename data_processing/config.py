import crawler.config


NUM = crawler.config.NUM

# The path of files
RAW_DATA_FOLDER = '../raw_data/'
PROCESSED_DATA_FOLDER = '../processed_data/'
PROCESSED_DATA_FILE = 'bilibili_popular_data.csv'

# About csv
COLUMNS = (
    '更新时间', '期数', '本周热词', '本期标题', '本期副标题',
    '视频标题', '视频分区', '视频简介',
    'UP主',
    '视频观看次数', '弹幕数', '评论数', '点赞数', '收藏数', '投币数', '转发数', '历史排名',
    '视频分辨率', 'IP属地', 'BV号', '推荐理由'
)
