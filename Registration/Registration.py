import random
login_list = []
pass_list = []

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
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(psword)
    return psword
def my_reg():
    pass
def author():
    return
def reg(l: list, p: list):   
    """Inimese registreerimine
    
    Tagastab loginide ja salasõnade listid 
    
    :param str v: kasutaja parooli loomise viis
    :rtype: list,list
    """
    print("Регистрация")
    n = input("Введите логин: ")
    u = username(n, login_list)
    while u == True:
        n = input("Такой логин уже существует. Введите  логин еще раз: ")
        u = username(n, login_list)
    v = input("Создать пароль автоматически или нет? (y/n): ")
    if v == "y":
        p = auto_reg()
        login_list.append(n)
        pass_list.append(p)
    else:
        my_reg()
    return l, p

while 1:
    print("Регистрация / Авторизиция / Данные / Выход")
    v = input("1 / 2 / 3 / 4: ")
    if v == "1":
        reg(login_list, pass_list)
    elif v == "2":
        i = 0
        while i < 3:
            t = author() #True or False
            if author() == True:
                print("Добро пожаловать!")
            else:
                i+=1
    elif v == "3":
        print(login_list)
        print(pass_list)
    else:
        print("Выход.")
        break