
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from pytdx.exhq import TdxExHq_API, TDXParams
api = TdxExHq_API(heartbeat=True)


future_info=pd.read_csv("select_list.csv",index_col=0)

def get_day_minute(name):
    with api.connect("202.106.83.241",7721):
        market_code,code=future_info[future_info["name"]==name][["market","code"]].values[0][:]
        market_data=pd.DataFrame(api.get_minute_time_data(market_code,code))
    return market_data


option = st.selectbox(
    '当日主力连续分钟线',
    set(future_info["name"].values) )

st.write(option)
market_data=get_day_minute(option)


if len (market_data)>0:
    price_data=market_data["price"].values
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    ax.plot(price_data)
    plt.grid()
    st.pyplot(fig)
else:
    st.write("暂无数据")

