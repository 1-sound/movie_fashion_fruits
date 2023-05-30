# 데이터베이스 사용 방법

# 1.Connection 맺기 (Python ===== DB 프로그램)
# - IP      : 컴퓨터 주소
# - Port    : 27017
# - ID & PW : 계정정보
# 2.명령 보내기 (Python ----→ DB)
# 3.결과 받기 (Python ←---- DB)
# 4.Connection 끊기 (Python XXXXX DB)

from pymongo import MongoClient


# MongoDB Connection
def conn():
    client = MongoClient("mongodb+srv://cnu:cnu1234@moviefashionfruits.fm0ohii.mongodb.net/")  # IP, Port, ID&PW
    db = client["movie"]

    collection = db.get_collection("movie")
    return collection