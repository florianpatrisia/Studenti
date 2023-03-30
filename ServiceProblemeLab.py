import datetime
import random

from Domain.problema_lab import ProblemaLab
from Utils.utils import random_string


class ServiceProbleme:
    def __init__(self, validator_problema, repo_probleme):
        """
        Creeaza un obiect de tip ServiceProblema
        :param validator_problema: validator de probleme, obiect de tip ValidatorProblema
        :param repo_probleme: repository de probleme, obiect de tip RepoProblemaLab
        """
        self.__validator_problema = validator_problema
        self.__repo_probleme = repo_probleme

    def getAll(self):
        """
        Returneaza lista de probleme
        :return: lista de probleme, lista
        """
        return self.__repo_probleme.getAll()

    def getProblemaByIdService(self, id_problema):
        """
        Returneaza problema care are numarul laboratorului si problema nr_lab_pb, tuplu
        :param id_problema: id-ul problemei care trebuie returnata
        :return: problema de laborator, daca exista
                 arunca exceptie de tip ValidationException, daca id-ul dat este incorect
                                        RepoException, daca problema nu se afla in lista
        """
        problema = self.__repo_probleme.getProblemaById(id_problema)
        self.__validator_problema.valideazaProblema(problema)
        return problema

    def adaugaProblemaService(self, id_problema, nr_lab_problema, descriere, deadline):
        """
        Adauga o problema in lista de probleme
        :param id_problema: id-ul problemei date, numar natrual
        :param nr_lab_problema: numarul laboratorului si numarul probblemei,de tip tuplu
        :param descriere: descrierea problemei, sir de carcatere
        :param deadline: deadline-ul problemei, lista de 3
        :return: -; daca problema a fost adaugata cu succes
                 arunca exceptie de tip ValidationException, daca datele de intrare sunt incorecte
                                        RepoException, daca problema nu se afla in lista

        """
        problema = ProblemaLab(id_problema, nr_lab_problema, descriere, deadline)
        self.__validator_problema.valideazaProblema(problema)
        self.__repo_probleme.adauga(problema)

    def stergeProblemaService(self, id_problema):
        """
        Sterge o problema care are un anumit id
        :param id_problema: id-ul problemei care trebuie stearsa, numar natural
        :return: -; daca problema a fost stears acu succes
                 arunca exceptie de tip ValidationException, daca id-ul dat este incorect
                                        RepoException, daca problema nu se afla in lista

        """
        problema = self.__repo_probleme.getProblemaById(id_problema)
        self.__validator_problema.valideazaProblema(problema)
        self.__repo_probleme.sterge(id_problema)

    def modificaProblemaService(self, id_problema, nrLabPbNoua, descriereNoua, deadlineNou):
        """
        Modifica nrLabProblema, descrierea si deadline-ul problemei care are id-ul problema
        :param id_problema: id-ul problemei care trebuie modificat
        :param nrLabPbNoua: noul numar de laborator si problema al problemei
        :param descriereNoua: noua descriere a problemei
        :param deadlineNou: noul deadline al problemei
        :return: -; daca modificarea s a efectuat cu succes
                 arunca exceptie de tip ValidationException, daca id-ul dat este incorect
                                        RepoException, daca problema nu se afla in lista

        """
        problema = ProblemaLab(id_problema, nrLabPbNoua, descriereNoua, deadlineNou)
        self.__validator_problema.valideazaProblema(problema)
        self.__repo_probleme.modifica(id_problema, nrLabPbNoua, descriereNoua, deadlineNou)

    def adaugaProblemaRandom(self):
        """
        Adauga o problema cu id, nr_laborator_problema, descriere, si deadline random
        :return: -; daca exista problema generata random a fost adaugata cu succes
                 arunca exceptie de tip ValidationException, daca id-ul dat este incorect
                                        RepoException, daca problema nu se afla in lista

        """
        id_problema = random.randint(1, 50)
        nr_lab_pb = []
        nr = random.randint(1, 15)
        nr_lab_pb.append(nr)
        nr = random.randint(1, 50)
        nr_lab_pb.append(nr)
        lungime = random.randint(1, 15)
        descriere = random_string(lungime)
        year = random.randint(2022, 2050)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        deadline = datetime.date(year, month, day)
        problema = ProblemaLab(id_problema, nr_lab_pb, descriere, deadline)
        self.__validator_problema.valideazaProblema(problema)
        self.__repo_probleme.adauga(problema)
