# 데이터 수집: yfinance 라이브러리를 이용하여 각 자산의 데이터를 수집합니다. ^KS11은 KOSPI 지수, KRW=X는 달러/원 환율, ^GSPC는 S&P 500, ^TNX는 미국 10년물 국채, JNK는 정크본드 ETF, VNQ는 미국 리츠 ETF
import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 수집
# Yahoo Finance에서 수집할 자산 코드 정의
assets = {
    "KOSPI": "^KS11",  # KOSPI 지수
    "USD/KRW": "KRW=X",  # 달러/원 환율
    "S&P 500": "^GSPC",  # S&P 500 지수
    "US Treasury 10Y": "^TNX",  # 미국 10년물 국채
    "US Junk Bond ETF": "JNK",  # 미국 정크본드 ETF
    "US REITs": "VNQ"  # 미국 리츠 ETF
}

# 각 자산에 대해 yfinance를 사용해 데이터 다운로드 (5년치)
data = {name: yf.download(ticker, start="2016-01-01", end="2021-12-31")['Adj Close'] for name, ticker in assets.items()}

# DataFrame으로 합치기
df = pd.DataFrame(data)

# 2. 데이터 전처리 (결측치 제거 및 로그 수익률 계산)
df = df.dropna()  # 결측치 제거
returns = df.pct_change().dropna()  # 일일 수익률 계산

# 3. 상관관계 계산
corr_matrix = returns.corr()

# 4. 상관관계표 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Asset Correlation Matrix')
plt.show()

# 5. 상관관계표 출력
print(corr_matrix)
