#2
def add_vat(price, vat_percent=18):
    new_price = price + (price * vat_percent / 100)
    return new_price





#3
def build_username(first, last, year=""):
    username = first.lower() + "." + last.lower()
    if year != "":
        username = username + str(year)
    return username




#5
def add_bonus(scores, bonus):
    for i in range(len(scores)):
        new_score = scores[i] + bonus
        scores[i] = min(100, new_score)

def with_bonus(scores, bonus):
    new_scores = scores[:]
    for i in range(len(new_scores)):
        n_score = new_scores[i] + bonus
        new_scores[i] = min(100, n_score)
    return new_scores




#6
def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def make_course(code, **details):
    course = {"code": code}
    course.update(details)
    return course
