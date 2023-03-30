from Domain.student import Student
from Repository.RepoStudenti import RepositoryStudenti


class FileRepositoryStudenti(RepositoryStudenti):
    def __init__(self, numeFisier):
        """
        Creaza un obiect de tip FileRepositoryStudent
        :param numeFisier: numele fisierului, sir de caractere
        """
        RepositoryStudenti.__init__(self)
        self.__numeFisier = numeFisier

    def __read_all_from_file(self):
        """
        Incarca studentii din fisier in lista de studenti
        :return: -; studentii sunt incarcati in lista de studenti
        """
        with open(self.__numeFisier, "r") as f:
            lines = f.readlines()
            self._lst_studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_student = int(parts[0].strip())
                    nume = parts[1].strip()
                    grupa = int(parts[2].strip())
                    student = Student(id_student, nume, grupa)
                    self._lst_studenti.append(student)
        return self._lst_studenti

    def __write_all_to_file(self):
        """
        Incarca in fisier studentii din lista de studenti
        :return: -; studentii sunt scrisi in fisier
        """
        with open(self.__numeFisier, "w") as f:
            for student in self._lst_studenti:
                f.write(str(student.getIdStudent()) + "," + student.getNumeStudent() + "," +
                        str(student.getGrupaStudent()) + "\n")

    def adauga(self, student):
        """
        Adauga un studet in fisier
        :param student: studentul ce este adaugat, obiect de tip Student
        :return: -; studentul este adaugat in fisier
                 arunca exceptie de tip RepoException cu mesajul "Student existent!", daca studentul se afla deja \
                 in fisier
        """
        self.__read_all_from_file()
        RepositoryStudenti.adauga(self, student)
        self.__write_all_to_file()

    def sterge(self, id_student):
        """
        Sterge stdentul care are id-ul id
        :param id_student: id-ul studnetului, numar natural
        :return: -; daca studentul este sters cu succes
                 arunca excaptie de tip RepoException cu mesajul "Student inexistent!", daca studentul nu exista \
                 in lista de studenti
        """
        self.__read_all_from_file()
        RepositoryStudenti.sterge(self, id_student)
        self.__write_all_to_file()

    def modifica(self, id_student, numeNou, grupaNoua):
        """
        Modifica un student care are id-ul id
        :param id_student: idul studentului, numar natural
        :param numeNou: noul nume al studentului, sir de caractere
        :param grupaNoua: noua grupa a studentului, numar natural
        :return: -; daca studentul este modificat cu succes
                 arunca excaptie de tip RepoException cu mesajul "Student inexistent!", daca studentul nu exista \
                 in lista de studenti
        """
        self.__read_all_from_file()
        RepositoryStudenti.modifica(self, id_student, numeNou, grupaNoua)
        self.__write_all_to_file()

    def getAll(self):
        """
        Returneaza lista de studenti din fisier
        :return: lisat de studenti
        """
        self.__read_all_from_file()
        return RepositoryStudenti.getAll(self)

    def getStudentById(self, idStudent):
        """
        Returneaza un student in functie de id
        :param idStudent: id- ul studentului care trebuie returnat
        :return: studentul cautat dupa id, daca se afla in lista
                 arunca exceptie de tip RepoException cu mesajul "Student inexistent!", daca studentul nu se afla \
                 in lista
        """
        self.__read_all_from_file()
        return RepositoryStudenti.getStudentById(self, idStudent)

    def __len__(self):
        """
        Returneaza lungimea listei de studenti din fisier
        :return: nr de studenti din fisier, de tip numar natural
        """
        self.__read_all_from_file()
        return RepositoryStudenti.__len__(self)
