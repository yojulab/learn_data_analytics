#### with_data_analyst
- 공개 데이터셋 목록 
  - https://kbig.kr/portal/kbig/datacube.page
  - https://zdataset.com/
  - https://bdp.kt.co.kr/ : KT통신 빅데이터 플랫폼(유,무료)

|종류| 주제 | 주요 항목 |데이터| 작성 | 출처 | 참조 |
| :---: | --- | :---: | :---: | :---: | :---: | :---: |
|분포| 범죄율 | 미국 강력 |USA arrests| 지도, 인구 분포 따른 변화 | - | - |
|CloundForm| 리뷰 | 네이버 리뷰 영화평 |주요 명사|  | - | - |
|CloundForm| 댓글 개입 | 국정원 |국정원(뉴스타파 공개)|  | - | - |
|시계열| 종가 예측 | 삼성전자 |API| - | - | - |
|시계열| 이용객 수 예측 | 항공기 이용객 |?| - | - | - |
| file| 주민등록인구통계| [cvs](https://jumin.mois.go.kr/index.jsp) | 주민등록인구통계,연령별 인구현황,주민등록 인구 기타현황 | encoding='cp949' | [행정안전부](https://mois.go.kr/) |  |
|file | 기상관측 | 지상,해양,고층,항공,세계기상전문 |[cvs](https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36)| [서울 연간](codes/연별_서울_기온변화.ipynb), [전국 월별](./codes/지점별_연_기온변화.ipynb), [열대야](./codes/서울_열대야_시각화.ipynb) | [기상자료개발포털](https://data.kma.go.kr) |  |
|file| 주택 실거래가 | 아파트 매매가 |[cvs](http://rtdown.molit.go.kr/)|[전국](codes/주택실거래가_전국.ipynb),[특정지역](./codes/주택실거래가_특정지역.ipynb),[부천](./codes/주택실거래가_부천.ipynb)| [국토교통부](http://rt.molit.go.kr/) | - |
|api | COVID19 | summary, By Country Live |[APIs](https://documenter.getpostman.com/view/10808728/SzS8rjbc)| web postman | [sourced from Johns Hopkins](https://covid19api.com/) | - |
|file| 상권 정보 | 소상공인시장진흥공단_상가(상권)정보 |[cvs](https://www.data.go.kr/data/15083033/fileData.do)| [전국상가](./codes/전국상가분석.ipynb), [경기상가](./codes/경기상가분석.ipynb), [경기시군구상가](./codes/경기시군구상가분석_지도.ipynb) | [공공데이터포털](https://www.data.go.kr/) | - |
|file| 행동예측 | Breathing In-Depth, Wearables in the Wetlab |[uri](https://ubicomp.eti.uni-siegen.de/home/datasets/index.html.en?lang=en)| - | - | - |
|API| 부동산 실거래가 | 단독/다가구 매매 실거래 자료, 연립다세대 매매 실거래자료, 아파트매매 실거래 자료, 아파트 분양권전매 신고 자료, 오피스텔 매매 신고 조회 서비스, 토지 매매 신고 조회 서비스, 아파트매매 실거래 상세 자료, 상업업무용 부동산 매매 신고 자료 |[api](https://www.data.go.kr/)| - | [공공데이터포털](https://www.data.go.kr/) | 국토교통부 |
|file?| 말뭉치 | - |-| - | [국립어학원](https://corpus.korean.go.kr/) | 국립어학원 |

