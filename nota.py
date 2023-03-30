class Nota:
    def __init__(self, idNota, idStudent, idProblemaLab, valoareNota):
        """
        Creeaza un obiect de tip Nota
        :param idNota: id-ul notei, numar natural
        :param idStudent: studentul care primeste nota, obiect de tip Student
        :param idProblemaLab: problema de laborator care primeste nota, un obicet de tip ProblemaLab
        :param valoareNota: valoare notei, numar real
        """
        self.__idNota = idNota
        self.__idStudent = idStudent
        self.__idProblemalab = idProblemaLab
        self.__valoareNota = valoareNota

    def getIdNota(self):
        """
        Returneaza id-ul notei
        :return: id-ul notei, numar natural
        """
        return self.__idNota

    def getIdStudent(self):
        """
        Returneaza studentul notei
        :return: un obiect de tip Student
        """
        return self.__idStudent

    def getIdProblemaLab(self):
        """
        Returneaza problema de laborator a notei
        :return: un obiect de tip ProblemaLab
        """
        return self.__idProblemalab

    def getValoareNota(self):
        """
        Returneaza valoarea notei
        :return: valoarei notei, de tip numar real
        """
        return self.__valoareNota

    def setValoareNota(self, valoareNoua):
        """
        Modifica valoarea notei
        :param valoareNoua: valoarea notei, de tip numar real
        :return: -; valoarea notei este modificata
        """
        self.__valoareNota = valoareNoua

    def __str__(self):
        """
        Returneaza sirul de craactere aferent notei
        :return: sirul de cractere aferent notei
        """
        return "Id nota: " + str(self.__idNota) + ", Id Student:" + str(self.__idStudent) + \
               ", id Problema de Laborator: " + str(self.__idProblemalab) + ", valoare nota " + str(self.__valoareNota)
