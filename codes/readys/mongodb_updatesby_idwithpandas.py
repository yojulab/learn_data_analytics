import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# MongoDB에 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # 데이터베이스 선택
collection = db['mycollection']  # 컬렉션 선택

# 기존 데이터 가져오기 (예시로는 _id와 name 필드만 가져옴)
existing_data = collection.find({}, {"_id": 1, "name": 1})

# 가져온 데이터를 Pandas DataFrame으로 변환
data = pd.DataFrame(list(existing_data))

# 날짜 컬럼 추가 및 문자열로 변환
data['date'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# 각 문서별로 업데이트 수행
for _, row in data.iterrows():
    filter_query = {"_id": row['_id']}  # 일치하는 문서 찾기 위한 필터 조건 설정
    
    update_query = {"$set": {
        "date": row['date'],   # 업데이트할 날짜 컬럼 및 값을 지정합니다.
    }}
    
    result = collection.update_one(filter_query, update_query)
    print(f"업데이트된 문서 수: {result.modified_count}")
