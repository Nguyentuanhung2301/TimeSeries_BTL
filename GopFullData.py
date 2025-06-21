import csv
import os

# Danh sách các file theo thứ tự thời gian
file_paths = [
    r"C:\Users\nguye\CODE\TimeSeries\BTL\Data\2019-Oct.csv",
    r"C:\Users\nguye\CODE\TimeSeries\BTL\Data\2019-Nov.csv",
    r"C:\Users\nguye\CODE\TimeSeries\BTL\Data\2019-Dec.csv",
    r"C:\Users\nguye\CODE\TimeSeries\BTL\Data\2020-Jan.csv",
    r"C:\Users\nguye\CODE\TimeSeries\BTL\Data\2020-Feb.csv",
    r"C:\Users\nguye\CODE\TimeSeries\BTL\Data\2020-Mar.csv",
    r"C:\Users\nguye\CODE\TimeSeries\BTL\Data\2020-Apr.csv"
]

# File xuất ra
output_path = r"C:\Users\nguye\CODE\TimeSeries\BTL\Data\Time_Data.csv"

# Duyệt qua các tháng (trừ tháng cuối)
with open(output_path, 'w', newline='', encoding='utf-8') as out_file:
    writer = None

    for i in range(len(file_paths) - 1):
        cur_path = file_paths[i]
        next_path = file_paths[i + 1]
        month_label = os.path.basename(cur_path).replace(".csv", "")

        # Lấy danh sách user_id có purchase ở tháng kế tiếp
        next_month_buyers = set()
        with open(next_path, 'r', encoding='utf-8') as nf:
            reader = csv.DictReader(nf)
            for row in reader:
                if row['event_type'] == 'purchase':
                    next_month_buyers.add(row['user_id'])

        # Gắn nhãn churn cho tháng hiện tại
        with open(cur_path, 'r', encoding='utf-8') as cf:
            reader = csv.reader(cf)
            header = next(reader)
            if writer is None:
                header.append("churn")
                header.append("month")
                writer = csv.writer(out_file)
                writer.writerow(header)
            for row in reader:
                uid = row[header.index("user_id")]
                churn = "0" if uid in next_month_buyers else "1"
                row.append(churn)
                row.append(month_label)
                writer.writerow(row)

print("✅ Đã xử lý toàn bộ 6 tháng đầu và lưu vào Time_Data.csv.")
