# DEEP Q NETWORK
Clone repository:
```bash

git clone https://github.com/Silverd1998x/deep-q-network.git

```



Cài đặt các thư viện cần thiết bằng pip:
bash
Copy code
pip install -r requirements.txt
Cách chạy
Di chuyển đến thư mục chứa file code:
bash
Copy code
cd your_repository
Chạy file code:
bash
Copy code
python main.py
Các tham số
Các tham số có thể được cấu hình bằng cách chỉnh sửa file config.py. Các tham số được cung cấp bao gồm:

ENV_NAME: Tên của môi trường học tăng cường. Mặc định là "CartPole-v0".
EPISODES: Số lượng tối đa các episode được huấn luyện. Mặc định là 1000.
MAX_STEPS: Số lượng tối đa các bước trong mỗi episode. Mặc định là 500.
GAMMA: Hệ số giảm giá cho các reward tương lai. Mặc định là 0.99.
EPS_START: Giá trị của epsilon ban đầu trong chiến lược của epsilon-greedy. Mặc định là 0.9.
EPS_END: Giá trị của epsilon kết thúc trong chiến lược của epsilon-greedy. Mặc định là 0.05.
EPS_DECAY: Tốc độ giảm của epsilon trong chiến lược của epsilon-greedy. Mặc định là 200.
LR: Tốc độ học của optimizer. Mặc định là 0.001.
BATCH_SIZE: Kích thước batch được sử dụng trong quá trình huấn luyện. Mặc định là 128.
TARGET_UPDATE: Tần suất cập nhật mô hình mục tiêu. Mặc định là 10.
Kết luận
Đó là hướng dẫn cài đặt và chạy code trên Github. Nếu bạn cần hỗ trợ thêm, vui lòng liên hệ với chúng tôi.
