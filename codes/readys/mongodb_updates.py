from pymongo import MongoClient

# MongoDB에 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # 데이터베이스 선택
collection = db['mycollection']  # 컬렉션 선택

# 여러 문서 삽입
documents = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 35, "city": "Incheon"}
]

result = collection.insert_many(documents)
print(f"삽입된 문서 ID들: {result.inserted_ids}")

# 문서 업데이트
filter_query = {"name": "Alice"}
update_query = {"$set": {"age": 26}}
result = collection.update_one(filter_query, update_query)

print(f"업데이트된 문서 수: {result.modified_count}")

# 모든 문서 출력
for document in collection.find():
    print(document)

# 날짜 컬럼 추가
from datetime import datetime
current_date = datetime.now()
filter_query = {}  # 모든 문서에 대해 업데이트
update_query = {"$set": {"date": current_date}}
result = collection.update_many(filter_query, update_query)

print(f"업데이트된 문서 수: {result.modified_count}")

# 모든 문서 출력 (날짜 확인)
for document in collection.find():
    print(document)
