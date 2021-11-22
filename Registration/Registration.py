import random
import re
login_list = ["Alex"]
pass_list = ["Aa1!aaaa"]

def username(n: str, l: list):
    """Sisestatud kasutaja nimi otsing

    Tagastab olemasolek järjendis bool formaadis

    :param str n: otsing nimi
    :rtype: bool
    """
    if n in l:
        t = True
    else:
        t = False
    return t
def auto_reg():
    """Salasõna genireerimine
    
    Tagastab salasõna str formaadis 
    
    :rtype: str
    """
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    password = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(f"Ваш пароль: {password}")
    return password
def my_reg():
    '''
    Salasõna kirjutamine
    
    Tagastab salasõna str formaadis
    
    :rtype: str
    '''
    print("Пароль должен содержать: минимум 8 символов, 1 букву в верхнем регистре, 1 букву в нижнем регистре, 1 спецсимол, 1 цифру")
    password = input("Введите пароль: ")
    sym = ".,:;!_*-+()/#¤%&)"
    i = 0
    while True:
        if passcheck(password) == True:
            break
        else:
            password = input("Введите пароль: ")
           
    return password
def passcheck(p: str):
    '''Parooli kontroll

    Tagastab True/False

    :param str p: Parool
    :rtype: bool
    '''
    if len(p) < 8:
        print("Пароль должен содержать минимум 8 символов")
    elif re.search('[A-Z]', p) is None:
        print("Пароль должен содержать буквы в верхнем регистре")
    elif re.search('[a-z]', p) is None:
        print("Пароль должен содержать буквы в нижнем регистре")
    elif re.search('[.,:;!_*-+()/\#¤%&@]', p) is None:
        print("Пароль должен содержать спецсимволы")
    elif re.search('[0-9]', p) is None:
        print("Пароль должен содержать цифры")
    else:
        return True
    return False
def reg(l: list, p: list):   
    """Inimese registreerimine
    
    Tagastab loginide ja salasõnade listid 
    
    :param str v: kasutaja parooli loomise viis
    :rtype: list,list
    """
    print("Регистрация")

    log = input("Введите логин: ")
    u = username(log, login_list)
    i = 0
    while u == True:
        print("Данный логин уже существует.")
        log = input("Введите другой логин: ")
        u = username(log, login_list)


    v = input("Создать пароль автоматически? (y/n): ")
    if v == "y":
        p = auto_reg()
    else:
        p = my_reg()

    login_list.append(log)
    pass_list.append(p)
    print("Аккаунт создан")
    return l, p
def author():
    '''Autoriseerimine

    Tagastab True/False
    
    :rtype: bool
    '''
    x = input("Введите логин: ")
    u = username(x, login_list)
    if u == True:
        login = login_list.index(x)
        x = input("Введите пароль: ")
        if pass_list[login] == x:
            return True
        else:
            print("Неверный пароль")
            return False
    else:
        print("Неверный логин")
        return False

while 1:
    print("Регистрация / Aвторизация / Данные / Выход из системы")
    v = input("1/ 2/ 3/ 4: ")
    if v == "1":
        reg(login_list, pass_list)
    elif v == "2":
        print("Авторизация")
        i = 0
        while i < 3:
            t = author()
            if t == True:
                print("Авторизация успешна.")
                i = 3
            else:
                i+=1
    elif v == "3":
        print(login_list)
        print(pass_list)
    else:
        print("The end")
        break