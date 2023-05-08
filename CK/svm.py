# N19DCCN180 - Nguyễn Văn Tuấn
# N19DCCN210 - Tạ Minh Trí
# N19DCCN230 - Nguyễn Thị Yến Vy
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
#B1:Chuẩn bị dữ liệu: Đầu tiên, ta phải chuẩn bị dữ liệu và tạo ra tập huấn luyện và tập kiểm tra.
# Ta sử dụng tập dữ liệu iris có sẵn trong scikit-learn để làm ví dụ.
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#B2:Huấn luyện mô hình SVM : Sau khi chuẩn bị dữ liệu, ta sẽ huấn luyện mô hình SVM. Trong trường hợp này,
# ta sẽ sử dụng SVM với kernel function là linear để tìm siêu phẳng tối ưu trong không gian hai chiều.
from sklearn.svm import SVC
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
#B3:Kiểm tra độ chính xác của mô hình: Sau khi huấn luyện mô hình,
# ta sẽ kiểm tra độ chính xác của mô hình bằng cách sử dụng tập kiểm tra.
from sklearn.metrics import accuracy_score
y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
#B4:Điều chỉnh tham số của mô hình: Nếu độ chính xác của mô hình không đạt yêu cầu,
# ta có thể điều chỉnh các tham số của mô hình để cải thiện độ chính xác.
# Ví dụ, ta có thể thay đổi kernel function hoặc giá trị của tham số C trong thuật toán SVM.
svm = SVC(kernel='rbf', C=10)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
