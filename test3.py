import random

# Số lớp và số học sinh trong mỗi loại lớp
classes = {
    '35_students': 5,
    '45_students': 6,
    '30_students': 10,
    '40_students': 4
}

# Tuổi trung bình là 20 năm và 8 tháng
average_age_months = 20 * 12 + 8

# Ngưỡ tuổi lớn hơn và nhỏ hơn 6 tháng so với tuổi trung bình
upper_age_months = average_age_months + 6
lower_age_months = average_age_months - 6

# Tạo danh sách tuổi cho mỗi lớp
def generate_ages(num_students):
    return [random.randint(12 * 12, 22 * 12) for _ in range(num_students)]

# Đếm số học sinh có tuổi lớn hơn hoặc nhỏ hơn ngưỡ tuổi
def count_students(ages, lower, upper):
    above = sum(1 for age in ages if age > upper)
    below = sum(1 for age in ages if age < lower)
    return above, below

# Tính toán cho mỗi lớp
for class_type, num_classes in classes.items():
    num_students = int(class_type.split('_')[0])
    print(f"{class_type}: {num_classes} classes, {num_students} students each")
    for class_num in range(1, num_classes + 1):
        ages = generate_ages(num_students)
        above, below = count_students(ages, lower_age_months, upper_age_months)
        print(f"  Class {class_num}:")
        print(f"    Students above average age: {above}")
        print(f"    Students below average age: {below}")