from Domain.nota import Nota
from Repository.RepoNote import RepositoryNote


class FileRepositoryNote(RepositoryNote):
    def __init__(self, numeFisier):
        """
        Creaza un obiect de tip FileRepositoryNote
        :param numeFisier: numele fisierului, sir de caractere
        """
        RepositoryNote.__init__(self)
        self.__numeFisier = numeFisier

    def __read_all_from_file(self):
        """
        Incarca notele din fisier in lista de note
        :return: -; notele sunt incarcate in lista de note

        :return:
        """
        with open(self.__numeFisier, "r") as f:
            lines = f.readlines()
            self._note.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_nota = int(parts[0].strip())
                    id_student = int(parts[1].strip())
                    id_problema = int(parts[2].strip())
                    valoare_nota = float(parts[3].strip())
                    nota = Nota(id_nota, id_student, id_problema, valoare_nota)
                    self._note.append(nota)

    def __write_all_to_file(self):
        """
        Incarca in fisier notele din lista de note
        :return: -; notele sunt scrise in fisier
        :return:
        """
        with open(self.__numeFisier, "w") as f:
            for nota in self._note:
                f.write(
                    str(nota.getIdNota()) + "," + str(nota.getIdStudent()) + "," + str(nota.getIdProblemaLab()) + ","
                    + str(nota.getValoareNota()) + "\n")
                # f.write(str(nota) + "\n")

    def adauga(self, nota):
        """
        Adauga o nota in fisier
        :param nota: nota ce este adaugata, de tip Nota
        :return: -;nota este adaugata in fisier
        """
        self.__read_all_from_file()
        RepositoryNote.adauga(self, nota)
        self.__write_all_to_file()

    def sterge(self, id_nota):
        """
        Sterge nota care are id-ul id
        :param id_nota: id-ul notei care trebuie stearsa
        :return: -; daca nota este stearsa cu succes
                 arunca exceptie de tip RepoException cu mesajul "Nota inexistenta!", daca nota nu se afla in lista
        """
        self.__read_all_from_file()
        RepositoryNote.sterge(self, id_nota)
        self.__write_all_to_file()

    def modifica(self, id_nota, valoareNoua):
        """
        Modifica nota care are id-ul id
        :param id_nota: id-ul notei care trebuie stearsa, nuamr natural
        :param valoareNoua: noua valoare a notei
        :return: -; daca nota este modificata cu succes
                 arunca exceptie de tip RepoException cu mesajul "Nota inexistenta!", daca nota nu se afla in lista
        """
        self.__read_all_from_file()
        RepositoryNote.modifica(self, id_nota, valoareNoua)
        self.__write_all_to_file()

    def getAll(self):
        """
        Returneaza lista cu obiecte de tip Nota din fisier
        :return: lista cu obiecte de tip Nota, de tip lista
        """
        self.__read_all_from_file()
        return RepositoryNote.getAll(self)

    def getNotaById(self, id_nota):
        """
        Returneaza o nota in functie de id
        :param id_nota: id-ul notei care trebuie returnata
        :return: nota cautata, daca se afla in lista
                 arunca exceptie de tip RepoException cu masajul "Nota inexistenta!", daca nota nu se afla in lista
        """
        self.__read_all_from_file()
        return RepositoryNote.getNotaById(self, id_nota)
