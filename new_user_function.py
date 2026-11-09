import random

def new_user():
    melog=f"Elvira__Magsumova_57_{random.randint(100, 999)}@yandex.ru"
    mepass=str(random.randint(100000, 999999))
    return melog, mepass