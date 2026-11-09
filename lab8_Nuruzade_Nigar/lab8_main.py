import utils
from utils import average
from utils import build_username as make_user
import utils as u

# Tapşırıq 1
def print_student_card(name, group, year):
    print("Name: "+ name)
    print("Group: "+ group)
    print("Year: " +str(year))
print_student_card("Aysel Mammadova", "CE-101", 1)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")
# print_student_card("Aysel Mammadova", "CE-101")  # TypeError verən hissə

# Tapşırıq 2
print(utils.add_vat(100))
print(utils.add_vat(50, 10))
print(utils.add_vat(vat_percent=5, price=80))

# Tapşırıq 3
print(make_user("Nigar", "Nuruzade", 2026))

# Tapşırıq 6
print(average(80, 90, 100))
