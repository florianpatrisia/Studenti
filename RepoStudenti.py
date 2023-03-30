# from Domain.student import Student
from Exceptii.Exceptii import RepoException


class RepositoryStudenti:
    def __init__(self):
        """
        Creaza un obiect de tip RepositoryStudenti
        detine lista de studenti
        """
        self._lst_studenti = list()

    def getAll(self):
        """
        Returneaza lista de studenti
        :return: lista de studenti, de tip lista
        """
        # return [str(x) for x in self._lst_studenti]
        return self._lst_studenti

    def getStudentById(self, idStudent):
        """
        Retruneaza un student in functie de id
        :param idStudent: id-ul studnetului cautat, numar natural
        :return: studentul cautat, daca exista in lista de studenti
                 arunca exceptie de tip RepoException cu mesajul "Student inexistent!", daca studentul nu se afla \
                 in lista
        """
        for elem in self._lst_studenti:
            if elem.getIdStudent() == idStudent:
                return elem
        raise RepoException("Student inexistent!\n")

    def adauga(self, student):
        """
        Adauga un student in lista de studenti
        :param student: studentul dat, obiect de tip Student
        :return:-; daca studentul este adaugat cu succes
                arunca exceptie de tip RepoException cu mesajul "Student existent", daca studentul se afla deja in lista
        """
        for elem in self._lst_studenti:
            if student.getIdStudent() == elem.getIdStudent():
                raise RepoException("Student existent!\n")
        self._lst_studenti.append(student)

    def sterge(self, id_student):
        """
        Sterge un student care are id-ul id_student din lista de studenti
        :param id_student: id-ul studentului ce va fi sters
        :return: -, daca acesta este sters cu succes
                 arunca excaptie de tip RepoException cu mesajul "Student inexistent!", daca studentul nu exista \
                 in lista de studenti
        """
        student = self.getStudentById(id_student)
        self._lst_studenti.remove(student)

    def modifica(self, id_student, numeNou, grupaNoua):
        """
        Modifica numele si grupa unui student din lista care are id-ul id
        :param id_student: id-ul studentului car etrebuie modificta, numar natural
        :param numeNou: numele nou al studentului, de tip sir de caractere
        :param grupaNoua: grupa noua a studentului, de tip numar natural
        :return: -; daca studentula  fost modificat cu succes
                 arunca excaptie de tip RepoException cu mesajul "Student inexistent!", daca studentul nu exista \
                 in lista de studenti
        """
        for elem in self._lst_studenti:
            if elem.getIdStudent() == id_student:
                elem.setNumeStudent(numeNou)
                elem.setGrupaStudent(grupaNoua)
                return
        raise RepoException("Student inexistent!\n")

    def __len__(self):
        """
        Returneaza lungimea listei de studenti
        :return: nr de studenti din lista
        """
        return len(self._lst_studenti)
