def intoarcere(n):
    """
    Mai intai transformam numarul in valoarea absoluta a acestuia
    Pentru a intoarce numarul vom crea o inmulti variabila copn( care la inceput este 0) cu 10 si mai apoi vom adauga
    valoarea numarului % 10, astfel adaugam ultima cira
    Mai apoi vom imparti numarul la 10 astfel vom taia utima cifra pe care deja am adaugat-o, si repetam procedeul
    pana am inversat toate cifrele
    :param n: Numarul ale carui cifre dorim sa le inversam
    :return: Numarul cu cifrele inversate
    """
    n = int(n)
    n = abs(n)
    copn = 0
    while n > 0:
        copn *= 10
        copn += n%10
        n = int(n/10)
    return -copn


def cmmdc(a, b):
    """
    Algoritmul lui Euclid pentru cmmdc folosindu-ne de scaderi
    :param a: Una dintre cele 2 numere pentru care dorim cmmdc
    :param b: Una dintre cele 2 numere pentru care dorim cmmdc
    :return: Cmmdc dintre a si b
    """
    while a != b:
        if a > b:
            a -=b
        else:
            b -=a
    return a


def prim(n):
    """
    Daca numarul e 0 sau 1 atunci acesta nu e prim
    Daca numarul se imparte exact cu vreo valoarea intre 2 si jumatatea numarului atunci acesta nu e prim
    In celelalte cazuri numerele sunt prime
    :param n: Numarul pe care dorim sa il verificam daca e prim
    :return: 1, daca numarul e prim, 0 in caz contrar
    """
    if n == 0 or n == 1:
        return 0
    for i in range(2, int(n/2)):
        if n % i == 0:
            return 0
    return 1


def superprim(n):
    """
    Daca numarul e <= 1 atunci acesta nu e superprim
    Verificam pentru numar si pentru toate prefixele acestuia daca sunt prime
    In caz afirmativ vom returna 1
    In caz contrar vom returna 0
    :param n: Numarul pe care dorim sa il verificam daca e superprim
    :return: 1, daca e superprim, 0 in caz contrar
    """
    ok = 1
    if n <= 1:
        return 0
    while n:
        if prim(n) == 0:
            return 0
        else:
            n /= 10
    return 1


def cerinta_2(lst):
    """
    Parcurge lista si verificam daca avem vreun numar negativ, iar daca gasim vreun numar negativ il afisam
    :param lst: Lista noastra
    :return: Numerele dorite
    """
    ok = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            print(lst[i], " ")
            ok = 1
    if ok == 0:
        print("Nu exista numere strict negative")


def cerinta_3(lst):
    """
    Verifica daca exista vreun numar cu ultima cifra n
    Parcurgem lista si comparam cu valoarea minima fiecare valoare care verifica care are ultima cifra n, iar in caz
    afirmativ ii vom da valoarii minime valoarea gasita
    :param lst: Lista noastra
    :return: Valoarea minima
    """
    ok = 0
    mn = 0
    n = input("Dati cifra:")
    n = int(n)
    for i in range(len(lst)):
        if lst[i] % 10 == n:
            ok = 1
            mn = lst[i]
            break
    if ok == 0:
        print("Nu exista numere care sa aibe ultima cifra", n)
    else:
        for i in range(len(lst)):
            if lst[i] % 10 == n and lst[i] < mn:
                mn = lst[i]
        print(mn)


def cerinta_4(lst):
    """
    Afisa toate numerele superprime
    :param lst: Lista dorita
    :return: Toate numerele superprime
    """
    for i in range(len(lst)):
        if superprim(lst[i]):
            print(lst[i], " ")


def cerinta_5(lst):
    """
    Parcurgem lista si pentru toate numerele si pt cele pozitive facem cmmdc
    Vom atribui elementelor din lista noua cmmdc-ul gasit daca sunt pozitive si le inversam daca sunt negative
    :param lst: Lista dorita
    :return: Lista noua
    """
    n = 0
    lista = []
    for i in range(len(lst)):
        if lst[i] > 0 and n == 0:
            n = lst[i]
        elif lst[i] > 0:
            n = cmmdc(n, lst[i])
        else:
            pass
    for i in range(len(lst)):
        if lst[i] > 0:
            lista.append(n)
        elif lst[i] == 0:
            lista.append(0)
        elif lst[i] < 0:
            m = intoarcere(lst[i])
            lista.append(m)
    print(lista)


def test_prim():
    assert prim(17)
    assert prim(2)
    assert not prim(0)
    assert prim(23)
    assert not prim(45)
    assert prim(239)


def test_superprim():
    assert superprim(239)
    assert  superprim(173)
    assert not superprim(1)
    assert not superprim(-356)
    assert not superprim(-1)
    assert not superprim(0)
    assert superprim(2)


def test_intoarcere():
    assert intoarcere(-23) == -32
    assert intoarcere(-11) == -11
    assert intoarcere(-45) == -54

def test_cmmdc():
    assert cmmdc(1, 2) == 1
    assert cmmdc(3, 33) == 3
    assert cmmdc(5, 26) == 1
    assert cmmdc(5, 25) == 5
    assert cmmdc(11, 122) == 1

def meniu():
    print("1.Citire lista")
    print("2.Afisarea numerelor negative din lista")
    print("3.Afisarea celui mai mic numar cu ultima cifra data de la tastatura")
    print("4.Afisarea tuturor numerelor din lista care sunt superprime")
    print("5.Afisarea listei obtinute din lista initiala in urma transformarii numerelor pozitive in cmmdc-ul lor, iar"
          "celor negative inversandu-le cifrele")


def citire():
    """
    Se citeste un string de numere, care apoi devine o lista de stringuri, iar apoi o lista de numere intregi
    :return: Lista dorita
    """
    s = input("Dati lista:")
    lista = s.split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista


def run():
    test_intoarcere()
    test_superprim()
    test_prim()
    test_cmmdc()
    meniu()
    lst = []
    while True:
        str=input()
        if str == "1":
            lst[:] = citire()
        elif str == "2":
            cerinta_2(lst)
        elif str == "3":
            cerinta_3(lst)
        elif str == "4":
            cerinta_4(lst)
        elif str == "5":
            cerinta_5(lst)
        elif str == "exit":
            return
        else:
            pass

run()