### Python Libraries
- [Mito & Aibro: The Two Best Python Libraries for Data Analysis and Model Training](https://medium.com/geekculture/mito-aibro-the-two-best-python-libraries-for-data-analysis-and-model-training-43dc432b176c)
- [Top 5+ Data Visualization Dashboard Templates to Use For Free](https://medium.com/@marinatetzlaff/top-5-data-visualization-dashboard-templates-to-use-for-free-58902b8bf74b)

### 공개 데이터셋 목록 
  - https://kbig.kr/portal/kbig/datacube.page
  - https://zdataset.com/
  - https://bdp.kt.co.kr/ : KT통신 빅데이터 플랫폼(유,무료)

### 주요 내부 코드 링크
- [./codes/cases](./codes/cases/)
- [./codes/pandas](./codes/pandas/)
- [./codes/numpys](./codes/numpys/)
- [./codes/preprocess](./codes/preprocess/)
- [./codes/dealingwithsound/](./codes/dealingwithsound/)

### link
#### 확률 통계
[[지오지브라 따라하며 배우기] 스프레드시트 / 히스토그램 / 도수분포다각형](https://youtu.be/XG4Ps13I6ds)
#### 이해 위한 필요 설명
Series = list
DataFrame = dict
dataframe.describe() :  각 항목 그래프로 표현, 설명
#### package
numpy
[pandas.DataFrame.replace](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html)  
to_save(.., encoding='utf-8-sig')
dataframe.dropna(.., subset=?, thresh=?)
dataframe.fillna(value=alt)   # alt='age':0,'gender':'U'
dataframe.get_dummies()
dataframe.to_datetime()
dataframe.query()
dataframe.merge(), concate()
dataframe.group()
dataframe.pivot_table()
