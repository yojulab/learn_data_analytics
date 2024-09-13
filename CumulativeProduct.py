from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
 
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0 # 일간 변동률의 첫 번째 값인 NaN을 0으로 변경한다.
sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100 # 일간 변동률 누적곱 계산

msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cp = ((100+msft_dpc)/100).cumprod()*100-100

import matplotlib.pyplot as plt
# 단순 비교 : 수치 차이로 비교 불가
plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
plt.show()

# 각 종목별 일간 변동률 히스토그램 작성
plt.hist(sec_dpc, bins=10)
plt.grid(True)
plt.show()
plt.hist(msft_dpc, bins=10)
plt.show()

# 일간 변동률로 비교 : 수치 %로 일치
plt.plot(sec.index, sec_dpc, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc, 'r--', label='Microsoft')
plt.show()

# 현재 시점 투자(start='2018-05-04') 대비 수익률
plt.plot(sec.index, sec_dpc_cp, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cp, 'r--', label='Microsoft')
plt.ylabel('Change %') 
plt.grid(True)
plt.legend(loc='best')
plt.show()
