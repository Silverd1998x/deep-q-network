# DEEP Q NETWORK

## 1. Setup conda environment
Khởi động terminal. Khởi tạo môi trường conda:
```
conda create -n deep-q python=3.7
```
activate môi trường vừa tạo
```
conda activate deep-q
```
## 2. git clone
sử dụng git-clone để tải thư mục về
```
git clone https://github.com/Silverd1998x/deep-q-network.git
```
di chuyển đến thư mục vừa git-clone
```
cd deep-q-network
```

## 3. Setup chương trình
Cài đặt các thư viện cần thiết bằng pip:
```
pip install -r setup.txt
```
Chạy file main.py, điền đầy đủ tham số --> Enter:
```
python main.py
```
Các tham số có thể được cấu hình bằng cách chỉnh sửa file `main.py`. Các tham số được cung cấp bao gồm:

- `ENV`: Tên của môi trường học tăng cường. Mặc định là "CartPole-v1".
- `N_EPISODES`: Số lượng tối đa các episode được huấn luyện. vd: 1000
- `N_TIMESTEPS`: Số lượng tối đa các bước trong mỗi episode. vd: 500.

sau đó, chạy file run.py. nhập tham số --> Enter:
```
python run.py
```
Các tham số có thể được cấu hình bằng cách chỉnh sửa file `run.py`. Các tham số được cung cấp bao gồm:

- `ENV`: Tên của môi trường học tăng cường. Mặc định là "CartPole-v1" (lưu ý: phải trùng với `ENV` trong file `main.py`).
- `N_TIMESTEPS`: Số lượng tối đa các bước trong lúc chạy chương trình. vd: 500 (chương trình sẽ chạy trong `500 time steps` rồi `stop`).

ngoài ra còn có các tham số khác có thể điều chỉnh trong file `agent.py`:
- `GAMMA`: Hệ số giảm giá cho các reward tương lai. Mặc định là 0.99.
- `EPSILON`: Giá trị của epsilon ban đầu. Mặc định là 1.0.
- `EPSILON_MIN`: Giá trị của epsilon kết thúc. Mặc định là 0.01.
- `EPSILON_DECAY`: Tốc độ giảm của epsilon. Mặc định là 0.98.
- `LEARNING_RATE`: Tốc độ học của optimizer. Mặc định là 0.001.
- `UPDATE_TARGET_NN_RATE`: Tần suất cập nhật mô hình mục tiêu. Mặc định là 10.

# Kết luận
Đó là hướng dẫn cài đặt và chạy code trên Github. Nếu bạn cần hỗ trợ thêm, vui lòng liên hệ với chúng tôi.
