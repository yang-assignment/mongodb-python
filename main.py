from pymongo import MongoClient

class Test:
    # 创建类的狗仔函数或初始化方法，其中包含一个参数self，表示类的示例，self在定义类的方法时是必须要有的，在带哦用时可以不传入相应参数
    def __init__(self):
        # 获取数据库的连接
        self.client = MongoClient('127.0.0.1', 27017)
        print(self.client)

    def getDBs(self):
        dbs = self.client.list_database_names()
        for db in dbs:
            print(db)

    def getColl(self):
        articledb = self.client["articledb"]
        collections = articledb.list_collection_names()
        for collection in collections:
            print(collection)

    def createColl(self):
        articledb = self.client["articledb"]
        articledb.create_collection("itcast")

    def dropColl(self):
        articledb = self.client["articledb"]
        articledb.drop_collection("itcast")

    def findDoc(self):
        self.articledb = self.client["articledb"]
        comment = self.articledb["comment"]
        documents = comment.find()
        for document in documents:
            print(document)

    def insertOneDoc(self):
        self.articledb = self.client["articledb"]
        comment = self.articledb["comment"]
        newDoc = {
            "_id": "7",
            "articleid": "100001",
            "content": "脱水会使人精疲力竭，而喝水可以使人精神饱满",
            "userid": "1007",
            "nickname": "咫尺天涯间",
            "age": "25",
            "phone": "13937165554",
            "createdatetime": "new Date()",
            "likenum": "999",
            "state": "1",
        }
        comment.insert_one(newDoc)

    def insertManyDoc(self):
        self.articledb = self.client["articledb"]
        comment = self.articledb["comment"]
        newDocs =[
            {
                "_id": "8",
                "articleid": "100001",
                "content": "吃饭千万不能吃多了，因为会饱",
                "userid": "1008",
                "nickname": "天涯若比邻",
                "age": "21",
                "phone": "135846240285",
                "createdatetime": "new Date()",
                "likenum": "666",
                "state": "1",
            },
            {
                "_id": "9",
                "articleid": "100001",
                "content": "吃饭前，先喝杯水或一碗汤，可减少饭量，对控制体重有帮助",
                "userid": "1008",
                "nickname": "玛丽莲·梦露",
                "age": "18",
                "phone": "13937165554",
                "createdatetime": "new Date()",
                "likenum": "8888",
                "state": "null",
            }
        ]
        comment.insert_many(newDocs)

    def updateDoc(self):
        self.articledb = self.client["articledb"]
        comment = self.articledb["comment"]
        comment.update_one({"content": "脱水会使人精疲力竭，而喝水可以使人精神饱满"},
                           {"$set": {"content": "吃饭前，先喝杯水或一碗汤，可减少饭量，对控制体重有明显的帮助"}})

    def deleteDoc(self):
        self.articledb = self.articledb = self.client["articledb"]
        comment = self.articledb["comment"]
        comment.delete_one({"nickname": "咫尺天涯间"})


# 主程序入口
if __name__ == '__main__':
    test = Test()
    # test.getDBs()
    # test.createColl()
    # test.dropColl()
    # test.getColl()
    # test.insertOneDoc()
    # test.insertManyDoc()
    test.updateDoc()
    # test.deleteDoc()
    test.findDoc()
