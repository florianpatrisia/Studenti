from Domain.nota import Nota
from Exceptii.Exceptii import ValidationException


class ServiceNota:
    def __init__(self, repoNote, repoStudenti, repoProbleme, validatorNota):
        """
        Creaza un obiect de tip ServiceNota
        :param repoNote: repository de note, obiect de tip RepositoryNote
        :param repoStudenti: repository de student, obiect de tip RepositoryStudenti
        :param repoProbleme: repository de probleme, obiect de tip RepoProblemaLab
        """
        self.__repoNote = repoNote
        self.__repoStudenti = repoStudenti
        self.__repoProbleme = repoProbleme
        self.__validatorNota = validatorNota

    def getAll(self):
        """
        Returneaza lista de note
        :return: lisat de note, de tip lista
        """
        return self.__repoNote.getAll()

    def getNotaByIDService(self, id_nota):
        """
        Returneaza nota care are id-ul id_nota
        :param id_nota: id-ul notei care trebuie returnat, numar natural
        :return: nota cautata, daca exista
                arunca exceptie de tip ValidationException daca id-ul dat este invalid
                                        RepoException, daca nota nu exista
        """
        nota = self.__repoNote.getNotaById(id_nota)
        self.__validatorNota.valideazaNota(nota)
        return nota

    def adaugaNota(self, idNota, idStudent, idProblema, valoare):
        """
        Adaugam o nota in lista de note
        :param idNota: id-ul notei, numar natural
        :param idStudent: id-ul studentului, numar natural
        :param idProblema: numarul laboaratorului si al problemei la care va fi asignata nota, tuplu
        :param valoare: valoarea notei, numar real
        :return: -; daca se adauga nota cu succes
                 arunca exceptie de tip ValidationException daca id-ul Notei, id-ul studentului, id-ul problemei sau \
                 valoarea notei sunt invalide
                                        RepoException, daca studentul exista deja
        """
        nota = Nota(idNota, idStudent, idProblema, valoare)
        self.__validatorNota.valideazaNota(nota)
        # Verificam daca in lista de probleme si studenti e afla aceste id-uri
        # ok1 = ok2 = 0
        # for elem in self.__repoStudenti.getAll():
        #     if elem.getIdStudent() == idStudent:
        #         ok1 = 1
        # for elem in self.__repoProbleme.getAll():
        #     if elem.getIdProblemaLab() == idProblema:
        #         ok2 = 2
        #
        # if ok1 == 0 and ok2 == 0:
        #     raise ValidationException("Student-ul si problema cu aceste id-uri nu exista in lista!")
        # if ok1 == 0:
        #     raise ValidationException("Student-ul cu acest id nu exista in lista de studenti!")
        # if ok2 == 0:
        #     raise ValidationException("Problema cu acest id nu exista in lista de probleme!")

        self.__repoNote.adauga(nota)

    def stergeNota(self, id_nota):
        """
        Sterge o nota dupa id
        :param id_nota: id-ul notei care trebuie stearsa, numar natural
        :return: -; daca nota este stearsa cu succes
                arunca exceptie de tip ValidationException daca id-ul dat este invalid
                                        RepoException, daca studentul nu exista
        """
        nota = self.__repoNote.getNotaById(id_nota)
        self.__validatorNota.valideazaNota(nota)
        self.__repoNote.sterge(id_nota)

    def modificaNota(self, id_nota, valoareNoua):
        """
        Modifica o nota care are id-ul id_nota
        :param id_nota:id-ul notei care trebuie modificate, numar natural
        :param valoareNoua: noua valoare a notei, numar real
        :return: -; daca nota a fost modificata cu succes
        """
        nota = Nota(id_nota, 1, 1, valoareNoua)
        self.__validatorNota.valideazaNota(nota)
        self.__repoNote.modifica(id_nota, valoareNoua)

    def getNoteProblema(self, nr_lab_pb):
        """
        Returneaza studentii si notele lor la o problema de laborator data
        :param nr_lab_pb: numarul laboratorului si al problemei date, tuplu
        :return: studentii si notele lor la o problema
        """
        nr_lab = nr_lab_pb[0]
        nr_pb = nr_lab_pb[1]
        listaStudenti = []
        for nota in self.__repoNote.getAll():
            if nota.getProblemaLab().getNrLaborator_Problema()[0] == nr_lab and \
                    nota.getProblemaLab().getNrLaborator_Problema()[1] == nr_pb:
                pereche = (nota.getStudent(), nota.getValoareNota())
                listaStudenti.append(pereche)
                listaStudenti.append([nota.getStudent(), nota.getValoareNota()])
        return listaStudenti

    def sortNume(self, id_problema):
        """????
        ????
        ?????
        ?????
        VEEEZZZZIIII
        ?/?????????
        ??????????
        ?????????
        Returneaza lista cu studenti si notelor la o problema de lab, ordonti crescator
        :param id_problema: id-ul problemei dupa care trebuie selectati studentii
        :return: lista de note si studenti
        """
        lista_studenti = []
        for elem in self.__repoNote.getAll():
            if elem.getIdProblemaLab() == id_problema:
                lista_studenti.append(elem)

        # lista_studenti.sort(key=lambda x: x.getProblemaById(id_problema).getDescriereProblema())
        # lista_studenti lista de studetni care au id-ul problemei dat
        # for i in range(len(lista_studenti)-1):
        #     student1=lista_studenti[i]
        #     j=i+1
        #     for j in range(len(lista_studenti)):

        return lista_studenti[0]

        # for i in range(len(listaStudenti) - 1):
        #     j = i + 1
        #     for j in range(len(listaStudenti)):
        #         if listaStudenti[i].get > listaStudenti[j]:
        #             aux = listaStudenti[i]
        #             listaStudenti[i] = listaStudenti[j]
        #             listaStudenti[j] = aux
        # return listaStudenti

    def sortNote(self, listaStudenti):
        """
        Sorteaza liste de studenti dupa nume
        :param listaStudenti: lista de studenti, lista cu obiecte de tip Studenti
        :return: liste de studenti sortata dupa nume
        """
        for i in range(len(listaStudenti) - 1):
            j = i + 1
            for j in range(len(listaStudenti)):
                if listaStudenti[i][0] == listaStudenti[j][0]:
                    if listaStudenti[i][1] > listaStudenti[j][1]:
                        aux = listaStudenti[i]
                        listaStudenti[i] = listaStudenti[j]
                        listaStudenti[j] = aux
        return listaStudenti
