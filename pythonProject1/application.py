import numpy as np
import streamlit as st
import pickle

model_pipe = pickle.load(open('model_pipe.pkl','rb'))
df = pickle.load(open('dataset.pkl','rb'))

st.title("The Right Price Predictor")

company = st.selectbox("Brand Name: ",df['Company'].unique())

type = st.selectbox("Laptop Type: ",df['TypeName'].unique())

ram_list = [2,4,6,8,12,16,24,32,64]
ram = st.selectbox("Ram: ",ram_list)

gpu = st.selectbox("GPU: ",df['Gpu'].unique())

opsys = st.selectbox("Operating System: ",df['OpSys'].unique())

weight = st.number_input("Weight: ")

touchscreen = st.selectbox('Touchscreen: ',['Yes','No'])

ips_panel = st.selectbox("IPS Panel: ",['Yes','No'])

sc_size = st.number_input("Screen Size (Inches): ")

resolution_market = [
    "1366 x 768",
    "1600 x 900",
    "1920 x 1080",
    "2304 x 1440",
    "2560 x 1440",
    "2560 x 1600",
    "2880 x 1800",
    "3000 x 2000",
    "3200 x 1800",
    "3840 x 2160"
]
resol = st.selectbox('Resolution: ',resolution_market)

processor = st.selectbox('Processor: ',df['Processor'].unique())

hdd = st.selectbox('HDD GB: ',[0,128,256,512,1024,2048])
ssd = st.selectbox('SSD GB: ',[0,128,256,512,1024,2048])
#hybrid_stg = st.selectbox('Hybrid: ',df['Hybrid'].unique())
#flash_stg = st.selectbox('Flash Storage: ',df['Flash_Storage'].unique())

if st.button("Calculate Price"):

    if ips_panel == 'Yes':
        ips_panel = 1
    else:
        ips_panel = 0

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    # calculating the ppi
    res = resol.split('x')
    x = int(res[0])
    y = int(res[1])
    ppi = (((x**2 + y**2)**0.5) / sc_size)
    my_query = [np.array([company,type,ram,gpu,opsys,weight,touchscreen,ips_panel,ppi,processor,hdd,ssd])]
    ans = int(np.exp(model_pipe.predict(my_query)[0]))
    st.title(ans)












