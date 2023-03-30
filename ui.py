import datetime

from Exceptii.Exceptii import ValidationException, RepoException
from Utils import utils
from Utils.utils import gnomeSort


# def random_string(length):
#     """
#     Functia genereaza un sir random
#     :param length: lungimea sirului generat, numar natural
#     :return: stringul
#     """
#     letters = string.ascii_lowercase + string.ascii_uppercase
#     new_string = ''.join(random.choice(letters) for i in range(length))
#     return new_string


def print_meniu():
    print("\nMeniu:")
    print("\nSTUDENT")
    print("1. Adauga")
    print("2. Sterge")
    print("3. Modifica")
    print("4. Cauta un student dupa id")
    print("5. Adauga 10 studenti random")
    print("6. Afiseaza toti studentii din lista")

    print("\nPROBLEMA DE LABORATOR")
    print("7. Adauga")
    print("8. Sterge")
    print("9. Modifica")
    print("10. Cauta o problema de laborator")
    print("11. Adauga 10 probleme de laborator random")
    print("12. Afiseaza toate problemele din lista")

    print("\nNOTA")
    print("13. Adauga")
    print("14. Sterge")
    print("15. Modifica")
    print("16. Afiseaza toate notele")
    print("17. Sorteaza lista de note")
    print("18. Afiseaza studentii cu media notelor sub 5")
    print("19. Afiseaza studentul cu cea mai mare medie")

    print("\nLAB 12- functii recursive")
    print("20. Suma notelor unui student")
    print("21. Numarul de note ale unui studnet")
    print("22. Afiseaza crescator notele unui student- Gnome Sort")
    print("23. Afiseaza crescator numele studentilor ordonati cresacator")
    print("24. Ordoneaza numele si notele asignate unei probleme")

    print("\n0. Exit!\n")


# def gnomeSort(lista, n):
#     index = 0
#     while index < n:
#         if index == 0:
#             index = index + 1
#         if lista[index] >= lista[index - 1]:
#             index = index + 1
#         else:
#             lista[index], lista[index - 1] = lista[index - 1], lista[index]
#             index = index - 1
#
#     return lista


# def quickSort(arr): #Functie recursiva
#     elements = len(arr)
#
#     # Base case
#     if elements < 2:
#         return arr
#
#     current_position = 0  # Position of the partitioning element
#
#     for i in range(1, elements):  # Partitioning loop
#         if arr[i] <= arr[0]:
#             current_position += 1
#             temp = arr[i]
#             arr[i] = arr[current_position]
#             arr[current_position] = temp
#
#     temp = arr[0]
#     arr[0] = arr[current_position]
#     arr[current_position] = temp  # Brings pivot to it's appropriate position
#
#     left = quickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
#     right = quickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot
#
#     arr = left + [arr[current_position]] + right  # Merging everything together
#     return arr

# def QuickSort(lista, st, dr):
#     i = st
#     j = dr
#     x = int((i + j) / 2)
#     mij = lista[x]
#     while i <= j:
#         while lista[i] < mij:
#             i = i + i
#         while lista[j] < mij:
#             j = j - 1
#         if i <= j:
#             lista[i], lista[j] = lista[j], lista[i]
#             i = i + 1
#             j = j - 1
#     if st < j:
#         QuickSort(lista, st, j)
#     if i < dr:
#         QuickSort(lista, i, dr)


class UI:
    def __init__(self, service_studenti, service_probleme, service_note):
        self.__service_studenti = service_studenti
        self.__service_probleme = service_probleme
        self.__service_note = service_note

    # def quickSort(self, lista, st, dr):
    #     x = int((st + dr) / 2)
    #     i = st, j = dr, pivot = lista[x]
    #     while i <= j:
    #         while lista[i] < pivot:
    #             i = i + i
    #         while lista[j] < pivot:
    #             j = j - 1
    #         if i <= j:
    #             lista[i], lista[j] = lista[j], lista[i]
    #             i = i + 1
    #             j = j - 1
    #     if st < j:
    #         self.quickSort(lista, st, j)
    #     if i < dr:
    #         self.quickSort(lista, i, dr)

    # def partition(self, lista, low, high):
    #     pivot = lista[high] - 1
    #     i = low - 1
    #     for j in range(low, high):
    #         if low[j] <= pivot:
    #             i = i + 1
    #             (lista[i], lista[j]) = (lista[j], lista[i])
    #     (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])
    #
    #     return i + 1
    #
    # def quickSort(self, lista, low, high):
    #     if low < high:
    #         pi = self.partition(lista, low, high)
    #         self.quickSort(lista, low, pi - 1)
    #         self.quickSort(self, pi + 1, high)

    def suma(self, lista, id_student, n):
        """
        RECURSIV
        Returneaza suma notelor unui student
        :param id_student: id-ul studentului pentru care trebuie sa facem suma notelor, numar natural
        :return: suma notelor, numar natural
        """
        if n == -1:
            return 0
        elif lista[n].getIdStudent() == id_student:
            return self.suma(lista, id_student, n - 1) + lista[n].getValoareNota()
        else:
            return self.suma(lista, id_student, n - 1)

    def nr_probleme_student(self, lista, id_student, n):
        """
        RECURSIV
        Returneaza numar de probleme pe care le-a rezolvat un student
        :param lista: lista de note
        :param id_student: id-ul studentului, numar natural
        :param n: numarul de note din lista
        :return: numarul de note ale unui student
        Complexitate:
        Best case O(1) - daca n=-1/ lista goala
        Worst case O(n) - n-nr de note din lista
        Average case O(n)
        """
        if n == -1:
            return 0
        elif lista[n].getIdStudent() == id_student:
            return self.nr_probleme_student(lista, id_student, n - 1) + 1
        else:
            return self.nr_probleme_student(lista, id_student, n - 1)

    def ordoneaza_nume_nota(self):
        """
        Se da numele unui laborator si problema, iar studenti care au asignati note la acel laborator si probleme \
        trebuie ordonati crescator dupa nume si nota
        :return: lista cu numele studentilor si nota lor la problema si laboratorul respectiv, ordonta crescator
        """
        print("Introduceti numarul laboratorului si problema pentru care doriti sa creati statistica")
        nr_laborator = int(input("Laborator: "))
        nr_problema = int(input("Problema: "))
        id_problema = -1
        for elem in self.__service_probleme:
            if elem.getNrLaborator_Problema()[0] == nr_laborator and elem.getNrLaborator_Problema()[1] == nr_problema:
                id_problema = elem.getIdProblema()
        if id_problema == -1:
            print("Nu exista nici-o nota asignata acestui laborator si probleme!")
            return

        lista_note = []
        for elem in self.__service_note.getAll():
            if elem.getIdProblemaLab() == id_problema:
                # nume=self.__service_studenti.getSudentByIDService(elem.getIdStudent())
                # nota=elem.getValoareNota()
                lista_note.append(elem)

        lista_note.sort(key=lambda x: (self.__service_studenti.getSudentByIDService(x.getIdStudent().getNumeStudent()),
                                       x.getValoareNota()))
        for elem in lista_note:
            nume = self.__service_studenti.getSudentByIDService(elem.getIdStudent().getNumeStudent())
            print(nume + str(elem.getValoareNota()) + "\n")

    def media_notelor_sub_5(self):
        """
        Toți studenții cu media notelor de laborator mai mic decât 5. (nume student și notă)
        :return: afiseaza studetnii care indeplinesc cerinta data
        Complexitate:
        Best case
        Worst case
        Average case
        """
        lista = self.__service_note.getAll()
        picati = []
        for i in range(len(lista)):
            idStudent1 = lista[i].getIdStudent()
            if idStudent1 not in picati:
                s = 0
                k = 0
                for j in range(len(lista)):
                    idStudent2 = lista[j].getIdStudent()
                    if idStudent1 == idStudent2:
                        s = s + lista[j].getValoareNota()
                        k = k + 1
                if k > 0:
                    s = s / k
                    picati.append(idStudent1)
                    if s < 5:
                        print(self.__service_studenti.getSudentByIDService(idStudent1), s)

    def studentul_cu_cea_mai_mare_medie(self):
        """
        Afiseaza studnetul cu cea mai mare medie
        :return: un obiect de tip student si media acestuia
        """
        lista = self.__service_note.getAll()
        verificati = []
        media_min = 1
        idStudent = lista[0].getIdStudent()
        salveaza_student = self.__service_studenti.getSudentByIDService(idStudent)
        for i in range(len(lista)):
            idStudent1 = lista[i].getIdStudent()
            if idStudent1 not in verificati:
                s = 0
                k = 0
                for j in range(len(lista)):
                    idStudent2 = lista[j].getIdStudent()
                    if idStudent1 == idStudent2:
                        s = s + lista[j].getValoareNota()
                        k = k + 1
                if k > 0:
                    s = s / k
                    verificati.append(idStudent1)
                    if s > media_min:
                        media_min = s
                        salveaza_student = self.__service_studenti.getSudentByIDService(idStudent1)
        print(salveaza_student, "\nmedia studentului este: ", media_min)

    def ordoneaza_note_student(self, id_student):
        """
        Ordoneaza cresactor notele unui student folosing gnome sort
        :param id_student: id-ul studnetuui ale carui note trebuie returnate, numar natural
        :return: lista cu notele unui student
        """
        lista_note = []
        for elem in self.__service_note.getAll():
            if elem.getIdStudent() == id_student:
                lista_note.append(elem.getValoareNota())
        print("lista de noyte neordonata: ", lista_note)
        n = len(lista_note) - 1
        utils.gnomeSort(lista_note, n)
        return lista_note

    def ordoneaza_nume_studneti(self):
        """
        Ordoneaza crescator numele studnetilor
        :return: lista de nume ale studentilor ordonati crescator, lista
        """
        lista_nume = []
        for elem in self.__service_studenti.getAll():
            lista_nume.append(elem.getNumeStudent())
        print("Lista de nume studenti neordonata: ", lista_nume)
        n = len(lista_nume) - 1
        gnomeSort(lista_nume, n)
        return lista_nume

    def adauga_student(self):

        id_student = int(input("id: "))
        nume = input("nume: ")
        grupa = int(input("grupa: "))
        try:
            self.__service_studenti.adaugaStudentService(id_student, nume, grupa)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def sterge_student(self):
        id_student = int(input("id: "))
        try:
            # for i in range(len(self.__service_note.getAll())-1):
            #     nota = self.__service_note.getAll()[i]
            #     if nota.getIdStudent() == id_student:
            #         self.__service_note.stergeNota(nota.getIdNota())
            #         i = i - 1

            # daca stergem un student din lista de studeti trebuie sa stergem si notele care sunt asignate studentului
            for elem in self.__service_note.getAll():
                if elem.getIdStudent() == id_student:
                    # nota=self.__service_note.
                    self.__service_note.stergeNota(elem.getIdNota())

            self.__service_studenti.stergeStudentService(id_student)

        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def modifica_student(self):
        id_student = int(input("id: "))
        nume = input("nume nou: ")
        grupa = int(input("grupa noua: "))
        try:
            self.__service_studenti.modificaStudentService(id_student, nume, grupa)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def cauta_student(self):
        id_student = int(input("id: "))
        try:
            print(self.__service_studenti.getSudentByIDService(id_student))
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def adauga_stud_random(self):
        try:
            for i in range(0, 10):
                self.__service_studenti.adaugaStudentRandom()
            for student in self.__service_studenti.getAll():
                print(student)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def afiseaza_studenti(self):
        for student in self.__service_studenti.getAll():
            print(student)
        # corect= print(*self.__service_studenti.getAll_s(), sep='\n')
        # corect= print(self.__service_studenti.getAll_s())

    def adauga_problema(self):
        id_problema = int(input("id: "))
        nr_lab_pb = []
        nr = int(input("nr lab: "))
        nr_lab_pb.append(nr)
        nr = int(input("nr problema: "))
        nr_lab_pb.append(nr)
        descriere = input("descirere: ")
        print("deadline(year, month, day): ")
        y = int(input(""))
        m = int(input(""))
        d = int(input(""))
        deadline = datetime.date(y, m, d)
        try:
            self.__service_probleme.adaugaProblemaService(id_problema, nr_lab_pb, descriere, deadline)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def sterge_problema(self):
        id_problema = int(input("id: "))
        try:
            # daca stergem o problema din lista de probleme trebuie sa stergem si notele asignate acelei probleme
            # for i in range(len(self.__service_note.getAll)):
            #     if self.__service_note.getAll[i].getIdProblemaLab() == id_problema:
            #         self.__service_note.stergeNota[i](0)

            for elem in self.__service_note.getAll():
                if elem.getIdProblemaLab() == id_problema:
                    self.__service_note.stergeNota(elem.getIdNota())
            self.__service_probleme.stergeProblemaService(id_problema)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def modifica_problema(self):
        id_problema = int(input("id: "))
        print("se introduc datele noi ale problemei:\n")
        nr_lab_pb_Nou = []
        nr = int(input("nr lab: "))
        nr_lab_pb_Nou.append(nr)
        nr = int(input("nr problema: "))
        nr_lab_pb_Nou.append(nr)
        descriere = input("descirere noua: ")
        print("deadline nou(year, month, day):")
        y = int(input())
        m = int(input())
        d = int(input())
        deadline = datetime.date(y, m, d)
        try:
            self.__service_probleme.modificaProblemaService(id_problema, nr_lab_pb_Nou, descriere, deadline)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def cauta_problema(self):
        id_problema = int(input("id: "))
        try:
            print(self.__service_probleme.getProblemaByIdService(id_problema))
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def adauga_problema_random(self):
        try:
            for i in range(0, 10):
                self.__service_probleme.adaugaProblemaRandom()
            for problema in self.__service_probleme.getAll():
                print(problema)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def afiseaza_toate_problemele(self):
        for problema in self.__service_probleme.getAll():
            print(problema)
        # print(self.__service_probleme.getAll())

    def adauga_nota(self):
        id1 = int(input("id nota: "))
        id2 = int(input("id student: "))
        id3 = int(input("id problema: "))
        val = float(input("valoare nota: "))
        try:
            self.__service_note.adaugaNota(id1, id2, id3, val)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def sterge_nota(self):
        id1 = int(input("id nota: "))
        try:
            self.__service_note.stergeNota(id1)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def modifica_nota(self):
        id1 = int(input("id nota: "))
        val = float(input("valoare noua nota: "))
        try:
            self.__service_note.modificaNota(id1, val)
        except ValidationException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def afiseaza_toate_notele(self):
        for nota in self.__service_note.getAll():
            print(nota)

    def sortare_note(self):
        self.ordoneaza_nume_nota()

    def suma_note(self):
        id_student = int(input("Id ul studetului: "))
        lista = self.__service_note.getAll()
        n = len(self.__service_note.getAll()) - 1
        print(self.suma(lista, id_student, n))

    def numar_probleme_student(self):
        id_student = int(input("Id ul studetului: "))
        lista = self.__service_note.getAll()
        n = len(self.__service_note.getAll()) - 1
        print(self.nr_probleme_student(lista, id_student, n))

    def ordoneaza_note(self):
        id_student = int(input("Id ul studetului: "))
        print(self.ordoneaza_note_student(id_student))

    #print_meniu()

    def run(self):
        while True:
            # print_meniu()
            option = int(input("Optiunea ta este: "))
            if option == 1:
                self.adauga_student()
            elif option == 2:
                self.sterge_student()
            elif option == 3:
                self.modifica_student()
            elif option == 4:
                self.cauta_student()
            elif option == 5:
                self.adauga_stud_random()
            elif option == 6:
                self.afiseaza_studenti()
            elif option == 7:
                self.adauga_problema()
            elif option == 8:
                self.sterge_problema()
            elif option == 9:
                self.modifica_problema()
            elif option == 10:
                self.cauta_problema()
            elif option == 11:
                self.adauga_problema_random()
            elif option == 12:
                self.afiseaza_toate_problemele()
            elif option == 13:
                self.adauga_nota()
            elif option == 14:
                self.sterge_nota()
            elif option == 15:
                self.modifica_nota()
            elif option == 16:
                self.afiseaza_toate_notele()
            elif option == 17:
                self.sortare_note()
            elif option == 18:
                self.media_notelor_sub_5()
            elif option == 19:
                self.studentul_cu_cea_mai_mare_medie()
            elif option == 20:
                # print(self.__service_note[0])
                self.suma_note()
            elif option == 21:
                self.numar_probleme_student()
            elif option == 22:
                self.ordoneaza_note()
            elif option == 23:
                print(self.ordoneaza_nume_studneti())
            elif option == 24:
                self.ordoneaza_nume_nota()
            elif option == 0:
                print("Programul s-a oprit!")
                return
            else:
                print("Optiune invalida! Introduceti alta comanda!")
