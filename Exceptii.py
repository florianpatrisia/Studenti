class RepoException(Exception):
    def __init__(self, errors):
        """
        Creaza un obiect de tip RepoException(o exceptioe legata de persistenta/ repository)
        :param errors:mesaj de eroare, sir de caractere
        """
        self.__errors = errors

    def getMessaje(self):
        """
        Returneaza mesajul unei exceptii de tip RepoException
        :return: mesaj de eroare, sir de caractere
        """
        return self.__errors


class ValidationException(Exception):
    def __init__(self, errors):
        """
        Creaza un obiect de tip ValidationException (o exceptie legata de validarea datelor de intrare)
        :param errors:mesaj de eroare, sir de caractere
        """
        self.__errors = errors

    def getMessaje(self):
        """
        Returneaza mesajul unei exceptii de tip ValidationException
        :return: mesaj de eroare, sir de caractere
        """
        return self.__errors
