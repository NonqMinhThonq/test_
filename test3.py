# giả định tất cả các cho sinh của 20 lớp sẽ nằm trong list classes
classes = [
]
age = 'số tuổi'
month = 'tháng'
average_age_months = 20 * 12 + 8
threshold_high = average_age_months + 6
threshold_low = average_age_months - 6

def classify_students(class_data):
    """Hàm phân loại học sinh lớn hơn hoặc nhỏ hơn ngưỡng tuổi
       classes là tổng số lớp 
       cls là 1 lớp cụ thể 
       student là số học sinh trong cls"""
    for cls in classes:
        for student in cls:
            older_students = [], younger_students = []
            student = age * 12 + month
            if student > threshold_high:
                older_students.append(student)
            elif student < threshold_low:
                younger_students.append(student)
    return f'Lớp {cls} có {student} học sinh. trong đó {len(older_students)} học sinh lớn hơn tuổi trung bình và {len(younger_students)} học sinh nhỏ hơn tuổi trung bình.'

for class_info in classes:
    print(classify_students(class_info))