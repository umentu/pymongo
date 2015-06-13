# -*- coding: utf-8 -*-

from pymongo import MongoClient

if __name__ == "__main__":

    mongo_client = MongoClient('localhost:27017')
    db_connect = mongo_client["db_name"]

    # データを挿入する
    # db_connect["collection_name"].insert_one({'x':1})

    # データをたくさん挿入する
    # db_connect["collection_name"].insert_many([{'x':i} for i in range(2,10)])

    # データを取得する
    # collection_list = db_connect["collection_name"].find()

    # 条件検索
    # collection_list = db_connect["collection_name"].find({'x':3})

    # OR検索
    # collection_list = db_connect["collection_name"].find({"$or":[ {"x":1}, {"x":5}]})

    # AND検索
    # collection_list = db_connect["collection_name"].find({"$and":[ {"x":1}, {"x":5}]})

    # データを変更する
    # db_connect["collection_name"].replace_one({'x': 1}, {'x': 4})   

    # x==2に該当するデータのxに10加算する
    # db_connect["collection_name"].update_one({'x': 9}, {'$set': {'x': 999}})

    # x==2に該当するデータのxに10加算する
    # db_connect["collection_name"].update_one({'x': 2}, {'$inc': {'x': 10}})

    # x==2に該当するすべてのデータのxに100加算する
    # db_connect["collection_name"].update_many({'x': 4}, {'$inc': {'x': 100}})

    # データを消去する
    # db_connect["collection_name"].delete_one({'x': 3})

    # データを複数消去する
    # db_connect["collection_name"].delete_many({'x': 104})

    collection_list = db_connect["collection_name"].find()

    for x in collection_list:
        print(x)
