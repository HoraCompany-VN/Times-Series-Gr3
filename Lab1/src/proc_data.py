import os
import pandas as pd
import shutil

def Process_data(path="H:\\HK1_2026-2027\\Times Series\\Lab1\\data\\raw\\daily-min-temperatures.csv"):

    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date') # Chuyển sang lấy cột Date làm cột chính
    df = df.asfreq('D') # Vì là dữ liệu theo ngày nên set 'D' hay Day
    df['Temp'] = df['Temp'].interpolate()

    df['Temp'].fillna(0, inplace=True)
    return df


def File_Exits(path):
    return os.path.exists(path)


def createFile(path):
    # Nếu chưa được xử lý dữ liệu sẽ chưa có file
    Destination = "H:\\HK1_2026-2027\\Times Series\\Lab1\\data\\processed"
    if ( not File_Exits(path)):
        os.makedirs(Destination, exist_ok=True)
        df = Process_data()
        df.to_csv("daily_temp_filter.csv")
        shutil.move("daily_temp_filter.csv", Destination)

if __name__ == "__main__":
    createFile()