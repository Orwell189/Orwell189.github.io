
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pytdx.exhq import TdxExHq_API, TDXParams
import time




api = TdxExHq_API(heartbeat=True)



future_info = pd.read_csv("select_list.csv", index_col=0)

def get_day_minute(name):
    with api.connect("202.106.83.241", 7721):
        market_code, code = future_info[future_info["name"] == name][[
            "market", "code"]].values[0][:]
        market_data = pd.DataFrame(api.get_minute_time_data(market_code, code))
    return market_data


st.title("欢迎进入神经元策略系统")
st.write("算法结果仅供参考，依据算法结果进行决策风险自担")
NQS_list=['神经元NQ_S1','神经元NQ_S2','神经元NQ_S3']
option = st.sidebar.selectbox("查看算法详情",NQS_list)

if option in NQS_list:
    s_data=np.cumprod(  1+(  np.random.random(100)-0.3  )/100   )
    fig = plt.figure(figsize=[10,5],facecolor="black")
    ax = fig.add_subplot(1,1,1,facecolor="black") 
    ax.plot(s_data)
    plt.grid()
    st.pyplot(fig)
    st.sidebar.write("策略净值",round(s_data[-1],2))
    st.sidebar.write("仓位状况")

st.write("听首歌放松下")
st.audio("460526429.mp3",format='audio/mp3',start_time=6)
for i in range(10):
    st.snow()
    time.sleep(5)
