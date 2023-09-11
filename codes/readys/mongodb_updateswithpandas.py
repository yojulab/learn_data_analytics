import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# MongoDB에 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # 데이터베이스 선택
mycollection = db['mycollection']  # 기존 컬렉션 선택
updatecollection = db['updatecollection']  # 업데이트할 컬렉션 선택

# mycollection에서 데이터 가져오기 (모든 필드)
data_cursor = mycollection.find()
data_list = list(data_cursor)

# 가져온 데이터를 Pandas DataFrame으로 변환
data_df = pd.DataFrame(data_list)

# 날짜 컬럼 추가 및 값 할당
data_df['date'] = datetime.utcnow()

# DataFrame을 updatecollection에 저장하기 위해 딕셔너리로 변환하여 저장
documents_to_insert = data_df.to_dict(orient='records')
result = updatecollection.insert_many(documents_to_insert)
print(f"저장된 문서 수: {len(result.inserted_ids)}")
