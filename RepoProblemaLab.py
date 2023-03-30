from Exceptii.Exceptii import RepoException


class RepoProblemaLab:
    def __init__(self):
        """
        Creaza un obiect de tip Repository ProblemaLab
        """
        self._lst_probleme = []

    def getAll(self):
        """
        Returneaza lista de probleme
        :return: lista de probleme, de tip lista
        """
        return [str(x) for x in self._lst_probleme]

    def getProblemaById(self, id_problema):
        """
        Returneaza o problema de lab care are un anumit id
        :param id_problema: id-ul problemei de laborator, numar natural
        :return: problema de laborator care are id-ul id_problema
                arunca exceptie de tip RepoException cu mesajul "Problema inexistenta!", daca problema nu se alfa \
                in lista de probleme
        """
        for elem in self._lst_probleme:
            if elem.getIdProblema() == id_problema:
                return elem
        raise RepoException("Problema inexistenta!\n")

    def adauga(self, problema):
        """
        Adauga o problema noua in lista
        :param problema: problema noua, de tip ProblemaLab
        :return: -; daca problema este aduagta cu succes
                 arunca exceptie de tip RepoException cu mesajul "Problema cu acest id deja exista!!", daca problema \
                 nu se alfa in lista de probleme
        """
        for elem in self._lst_probleme:
            if problema.getIdProblema() == elem.getIdProblema():
                raise RepoException("Problema cu acest id deja exista!")
        self._lst_probleme.append(problema)

    def sterge(self, id_problema):
        """
        Sterge o problema dupa id-ul acesteia
        :param id_problema: id-ul problemei care trebuie stearsa
        :return: -; daca s a efectuat stergerea cu succes
                arunca exceptie de tip RepoException cu mesajul "Problema inexistenta!", daca problema nu se alfa \
                in lista de probleme
        """
        problema = self.getProblemaById(id_problema)
        self._lst_probleme.remove(problema)

    def modifica(self, id_problema, nrLabPbNou, descriereNoua, deadlineNou):
        """
        Modifica o problema care are id-ul id_problema
        :param id_problema: id-ul problemei care trebuie modificata
        :param nrLabPbNou: noul numar de labaorator si problema al problemei, de tip tuplu
        :param descriereNoua: noua descriere a problemei, de tip sir de carcatere
        :param deadlineNou: noul deadline al problemei, de tip data calendaristica
        :return: -; modificarea s a efectuat cu succes
                 arunca exceptie de tip RepoException cu mesajul "Problema inexistenta!", daca problema nu se alfa \
                 in lista de probleme
        """
        for elem in self._lst_probleme:
            if elem.getIdProblema() == id_problema:
                elem.setNrLaborator_Problema(nrLabPbNou)
                elem.setDescriereProblema(descriereNoua)
                elem.setDeadlineProblema(deadlineNou)
                return
        raise RepoException("Problema inexistenta!\n")

    def __len__(self):
        """
        Returneaza lungimea listei de probleme
        :return: lungimea listei de probleme, de tip numar natural
        """
        return len(self._lst_probleme)
