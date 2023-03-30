from Exceptii.Exceptii import RepoException


class RepositoryNote:
    def __init__(self):
        """
        Creeazza un obiect de tip RepositoryNote (detine lista de note)
        """
        self._note = []

    def getAll(self):
        """
        Returneaza lista cu obiecte de tip Nota
        :return: lista cu obiecte de tip Nota, de tip lista
        """
        return self._note

    def getNotaById(self, id_nota):
        """
        Returneaza o nota in functie de id
        :param id_nota: id-ul notei, numar natural
        :return: nota care are id-ul dat, daca exista
                 arunca exceptie de tip RepoException cu masajul "Nota inexistenta!", daca nota nu se afla in lista
        """
        for nota in self._note:
            if nota.getIdNota() == id_nota:
                return nota
        raise RepoException("Nota inexistenta!\n")

    def adauga(self, nota):
        """
        Adauga o nota in lista de note
        :param nota: nota data, un obiect de tip Nota
        :return: -; daca nota este adaugata cu succes
                    arunca o exceptie de tip RepoException cu mesajul "Nota existenta!", daca nota se afla deja in lista
        """
        for elem in self._note:
            if nota.getIdNota() == elem.getIdNota():
                raise RepoException("Nota existenta!\n")
        self._note.append(nota)

    def sterge(self, id_nota):
        """
        Sterge nota care are id-ul id_nota din lista de note
        :param id_nota: id-ul notei care trebuie stersa, numar natural
        :return: -; daca nota este stearsa cu succes
                 arunca exceptie de tip RepoException cu mesajul "Nota inexistenta!", daca nota nu se afla in lista
        """
        nota = self.getNotaById(id_nota)
        self._note.remove(nota)

    def modifica(self, id_nota, valoareNoua):
        """
        Modifica valoarea notei care are id-ul id
        :param id_nota: id-ul notei care trebuie modificata, numar natural
        :param valoareNoua: noua valoare a notei, numar real
        :return: -; daca nota este modificata cu succes
                 arunca exceptie de tip RepoException cu mesajul "Nota inexistenta!", daca nota nu se afla in lista

        """
        for nota in self._note:
            if nota.getIdNota() == id_nota:
                nota.setValoareNota(valoareNoua)
                return
        raise RepoException("Nota inexistenta!\n")


