# N19DCCN180 - Nguyễn Văn Tuấn
# N19DCCN210 - Tạ Minh Trí
# N19DCCN230 - Nguyễn Thị Yến Vy
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import svm

def room_cancel_prediction(input_data):

    hotel_dataset = pd.read_csv('Hotel_Reservations.csv')
    # training, testing = train_test_split(hotel_dataset, test_size = 0.2, random_state=2)
    # training.to_csv('train.csv',index=False)
    # testing.to_csv('test.csv',index=False)
#Tiền xử lý bộ dữ liệu
    meal_dic = {
        "Meal Plan 1": 1,
        "Meal Plan 2": 2,
        "Meal Plan 3": 3,
        "Not Selected": 0
    }
    room_type_dic = {
        "Room_Type 1": 1,
        "Room_Type 2": 2,
        "Room_Type 3": 3,
        "Room_Type 4": 4,
        "Room_Type 5": 5,
        "Room_Type 6": 6,
        "Room_Type 7": 7
    }
    market_dic = {
        "Offline": 1,
        "Online": 2,
        "Corporate": 3,
        "Aviation": 4,
        "Complementary": 5
    }
    cancel_dic = {
        "Not_Canceled": 1,
        "Canceled": 2
    }

    hotel_dataset['type_of_meal_plan'] = hotel_dataset['type_of_meal_plan'].map(meal_dic)
    hotel_dataset['room_type_reserved'] = hotel_dataset['room_type_reserved'].map(room_type_dic)
    hotel_dataset['market_segment_type'] = hotel_dataset['market_segment_type'].map(market_dic)
    hotel_dataset['booking_status'] = hotel_dataset['booking_status'].map(cancel_dic)
#Huấn luyện dữ liệu 
    X = hotel_dataset.drop(hotel_dataset.columns[[0, 18]], axis=1)
    Y = hotel_dataset['booking_status']

    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

    model = svm.SVC(kernel='rbf', C=10)
    model.fit(X_train, y_train)

#Tiền xử lý dữ liệu cần dự đoán
    replaced_list1 = [x if x not in meal_dic else meal_dic[x] for x in input_data]
    replaced_list2 = [x if x not in room_type_dic else room_type_dic[x] for x in replaced_list1]
    replaced_list3 = [x if x not in market_dic else market_dic[x] for x in replaced_list2]


    data_to_np_array = np.asarray(replaced_list3)
    std_data = data_to_np_array.reshape(1, -1)
    prediction = model.predict(std_data)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)
    return prediction

if __name__=="__main__":
    input_data = [2,0,0,3,'Meal Plan 1',0,'Room_Type 1',271,2018,9,21,'Offline',0,0,0,101.33,1]
    prediction = room_cancel_prediction(input_data)
    if (prediction[0] == 1):
       print("Result of prediction: Not_Canceled.")
    else:
       print("Result of prediction: Canceled.")
