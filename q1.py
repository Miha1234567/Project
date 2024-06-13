import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('banan.jpg')

data = pd.read_csv("rus_car_prices3.csv")
data_fl = pd.read_csv("df_fl.csv")
data_ca = pd.read_csv("df_ca.csv")
data_tx = pd.read_csv("df_tx.csv")
df_f_150 = pd.read_csv("df_f_150.csv")
DF_F_150 = pd.read_csv("DF_F_150.csv")
df_R_R = pd.read_csv("df_R_R.csv")
df_Audi = pd.read_csv("df_Audi.csv")


def main():
    page = st.sidebar.selectbox("Выбрать исследование:", 
                            ["-------------------",
                             "Сравнение Пробега и Стоимости автомобилей", 
                             "Продажи по штатам",
                             "Флорида,Калифорния,Техас", 
                             "Ford F-150",
                             "Rolls-Royce",
                             "Audi"
                            ])

    if page == "-------------------":
        st.header("""Проект:  Исследования рынка продажи автомобилей с использованием технологий анализа данных""")
        st.write(
        """    
        ### Представлен анализ рынка продажи автомобилей в Соединенных штатах америки с 2014 по 2015 гг. #### 
        """)
        st.image(image)

    elif page == "Сравнение Пробега и Стоимости автомобилей":
        st.header("""Сравнение Пробега и Стоимости автомобилей""")
        fig, ax = plt.subplots()
        plt.scatter(data['Пробег'], data['Цена продажи'], color='b', label='Автомобили')
        plt.xlabel('Пробег')
        plt.ylabel('Стоимость')
        plt.title('Сравнение Пробега и Стоимости автомобилей')
        plt.legend()
        st.pyplot(fig)
        st.write(
         """
         ### Вывод:
         По графику видно, что, в целом, с увеличением пробега автомобиля его стоимость имеет тенденцию к снижению. Это ожидаемая динамика, так как пробег обычно считается одним из ключевых факторов, влияющих на стоимость автомобиля.
         Так же можно заметить, что есть скопление точек с низким пробегом и высокой стоимостью, что может указывать на особенно ценные или новые модели.
         """
         )


    elif page == "Продажи по штатам":
         st.header("""Продажи по штатам""")
         fig, ax = plt.subplots()
         data['Штат продажи'].value_counts(ascending = True).plot(kind = 'barh', title = 'Продажи по штатам')
         st.pyplot(fig)
         st.write(
         """
         ### Вывод:
         Из представленного графика видно, что определенные штаты выделяются в объемах продаж. Это свидетельствует о наличии предпочтений у покупателей и особенностей рыночной динамики в этих регионах
         """
         )

    

    elif page == "Флорида,Калифорния,Техас":
        st.header("""Топ-10 автомобилей по продажам во Флориде""")
        fig, ax = plt.subplots()
        data_fl['Компания'].value_counts()
        l_10 = len(data_fl['Компания'].value_counts())
        ll= l_10-10
        data_fl['Компания'].value_counts(ascending =True)[ll:l_10].plot(kind = 'barh', title = 'Топ-10 автомобилей по продажам во Флориде')
        st.pyplot(fig)
        

        st.header("""Топ-10 автомобилей по продажам в Калифорнии""")
        fig, ax = plt.subplots()
        data_ca['Компания'].value_counts()
        l_10 = len(data_ca['Компания'].value_counts())
        ll= l_10-10
        data_ca['Компания'].value_counts(ascending =True)[ll:l_10].plot(kind = 'barh', title = 'Топ-10 автомобилей по продажам в Калифорнии')
        st.pyplot(fig)
       

        st.header("""Топ-10 автомобилей по продажам в Техасе""")
        fig, ax = plt.subplots()
        data_tx['Компания'].value_counts()
        l_10 = len(data_tx['Компания'].value_counts())
        ll= l_10-10
        data_tx['Компания'].value_counts(ascending =True)[ll:l_10].plot(kind = 'barh', title = 'Динамика продаж по Техасу')
        st.pyplot(fig)
        
    elif page == "Ford F-150":
        st.header("""Ford F-150""")
        fig, ax = plt.subplots()
        plt.scatter(df_f_150['Пробег'], df_f_150['Цена продажи'], color='b', label='Автомобили')
        plt.xlabel('Пробег')
        plt.ylabel('Стоимость')
        plt.title('Сравнение Пробега и Стоимости автомобилей')
        plt.legend()
        st.pyplot(fig)
        
        #fig, ax = plt.subplots()
        #st.header("""Ford F-150""")
        #DF_F_150.groupby('Цвет').size().plot(kind='pie')    
        #st.pyplot(fig)


    elif page == "Rolls-Royce":
        st.header("""Rolls-Royce""")
        fig, ax = plt.subplots()
        plt.scatter(df_R_R['Пробег'], df_R_R['Цена продажи'], color='b', label='Автомобили')
        plt.xlabel('Пробег')
        plt.ylabel('Стоимость')
        plt.title('Сравнение Пробега и Стоимости автомобилей')
        plt.legend()
        plt.show()
        st.pyplot(fig)


    elif page == "Audi":
        st.header("""Audi""")
        fig, ax = plt.subplots()
        plt.scatter(df_Audi['Пробег'], df_Audi['Цена продажи'], color='b', label='Автомобили')
        plt.xlabel('Пробег')
        plt.ylabel('Стоимость')
        plt.title('Сравнение Пробега и Стоимости автомобилей')
        plt.legend()
        plt.show()
        st.pyplot(fig)



if __name__ == "__main__":
          main()