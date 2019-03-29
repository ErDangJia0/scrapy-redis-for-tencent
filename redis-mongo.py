import json, redis, pymongo


def main():
    # 指定Redis数据库信息
    rediscli = redis.Redis(host='localhost', port=6379, db=0)
    # 指定MongoDB数据库信息
    mongocli = pymongo.MongoClient(host='localhost', port=27017)
    # 创建数据库名
    db = mongocli['sina']
    # 创建表名
    sheet = db['sina_items']
    offset = 0
    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["tencent:item"])
        item = json.loads(data.decode("utf-8"))
        sheet.insert(item)
        offset += 1
        print(offset)


if __name__ == '__main__':
    main()
