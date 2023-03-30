class ProblemaLab:

    def __init__(self, idProblema, nrLaborator_Problema, descriereProblema, deadlineProblema):
        """
        Creeaza un obiect de tipul ProblemaLab
        :param nrLaborator_Problema: numarul laboratorului si al problemei
                                     de tip tuple
        :param descriereProblema: descrierea problemei, sir de caractere
        :param deadlineProblema: data pana la care trebuie rezolvata problema, de tip data calendaristica
        :return:-
        """
        self.__idProblema = idProblema
        self.__nrLaborator_Problema = nrLaborator_Problema
        self.__deadlineProblema = deadlineProblema
        self.__descriereProblema = descriereProblema

    def getIdProblema(self):
        """
        Returneaza id-ul problemei de laborator
        :return: id-ul problemei de laborator
        """
        return self.__idProblema

    def getNrLaborator_Problema(self):
        """
        Returneaza numarul problemei de laborator
        :return: numarul problemei de laborator
        """
        return self.__nrLaborator_Problema

    def getDescriereProblema(self):
        """
        Returneaza descrierea problemei de laborator
        :return: descrierea problemei de laborator, sir de caractere
        """
        return self.__descriereProblema

    def getDeadlineProblema(self):
        """
        Returneaza deadline-ul problemei de laborator
        :return: deadline-ul problemei de laborator, de tip data
        """
        return self.__deadlineProblema

    def setNrLaborator_Problema(self, numarNou):
        """
        Mofica numarul problemei de laborator
        :param numarNou: noul numar al problemei, de tip numar natural
        :return: -; numarul problemei de laborator este modificat
        """
        self.__nrLaborator_Problema = numarNou

    def setDescriereProblema(self, descriereNoua):
        """
        Modifica descrierea problemei
        :param descriereNoua: noua descrieire a problemei, de tip sir de caractere
        :return: -; descrierea problemei este modificata
        """
        self.__descriereProblema = descriereNoua

    def setDeadlineProblema(self, deadlineNou):
        """
        Modifica deadline-ul problemei
        :param deadlineNou: noul deadline al probleemi,  de tip data calendaristica
        :return: -; Deadline-ul problemei este modificat
        """
        self.__deadlineProblema = deadlineNou

    def __str__(self):
        """
        Returneaza sirul de caractere aferent problemei
        :return: sirul de caractere aferent problemei
        """
        return "Id-ul problemei: " + str(self.__idProblema) + " Numar laborator si problema: " + \
               str(self.__nrLaborator_Problema) + ", descriere: " + \
               str(self.__descriereProblema) + ", deadline: " + str(self.__deadlineProblema)

