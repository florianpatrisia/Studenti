from Domain.student import Student
import random

from Utils.utils import random_string


class ServiceStudenti:

    def __init__(self, validator_student, repo_studenti):
        """
        Creeaza un obiect de tip ServiceStudenti
        :param validator_student: validator de studenti, obiect de tip ValidatorStudent
        :param repo_studenti: repository de studenti, obiect de tip RepositoryStudenti
        """
        self.__validator_student = validator_student
        self.__repo_studenti = repo_studenti

    def getAll(self):
        """
        Returneaaz lista de studenti
        :return: lisat de studenti, lista
        """
        return self.__repo_studenti.getAll()

    def getSudentByIDService(self, id_student):
        """
        Returneaza stundentul din lista cu id-ul Id
        :param id_student: numar natural, id-ul studentului
        :return: studentul cautat, daca exista in lista
                 arunca exceptie de tip ValidationException daca id-ul dat este invalid
                                        RepoException, daca studentul nu exista
        """
        student = self.__repo_studenti.getStudentById(id_student)
        self.__validator_student.valideazaStudent(student)
        return student

    def adaugaStudentService(self, id_student, nume, grupa):
        """
        Adauga un student in lista de studenti
        :param id_student: id-ul studentului, numar natural
        :param nume: numele studentuului, sir de caractere
        :param grupa: grupa studentului, numar natural
        :return: -, daca se adauga studentulul cu succes
                arunca exceptie de tip Validationxception daca id-ul, numele sau grupa sunt invalide
                                       RepoException daca studentul exista deja in lista de studenti
        """
        student = Student(id_student, nume, grupa)
        self.__validator_student.valideazaStudent(student)
        self.__repo_studenti.adauga(student)

    def stergeStudentService(self, id_student):
        """
        Sterge un student dupa id
        :param id_student: id-ul studentului ce trebuie modificat, nuamr natural
        :return: -, daca stergerea studentului se efectueaza cu succes
                 arunca exceptie de tip Validationxception daca id-ul, numele sau grupa studentului sunt invalide
                                        RepoException daca studentul nu se afla in lista de studenti
        """
        student = self.__repo_studenti.getStudentById(id_student)
        self.__validator_student.valideazaStudent(student)
        self.__repo_studenti.sterge(id_student)

    def modificaStudentService(self, id_student, numeNou, grupaNoua):
        """
        Modifica studentul care are id-ul id
        :param id_student: id-ul studentului care trebuie modificat, nuamr natural
        :param numeNou: noul nume al studentului, sir de caractere
        :param grupaNoua: noua grupa a studentului, numar natural
        :return: -, daca studentul a fost modificat cu succes
                 arunca exceptie de tip Validationxception daca id-ul, numele sau grupa sunt invalide
                                        RepoException daca studentul nu se afla in lista de studenti
        """
        student = Student(id_student, numeNou, grupaNoua)
        self.__validator_student.valideazaStudent(student)
        self.__repo_studenti.modifica(id_student, numeNou, grupaNoua)

    def adaugaStudentRandom(self):
        """
        Adauga un student cu un id, nume si grupa random in lista
        :return:-; daca studentul a fost adaugat cu succes
                 arunca exceptie de tip Validationxception daca id-ul, numele sau grupa sunt invalide
                                        RepoException daca studentul se afla in lista de studenti

        """
        id_student = random.randint(1, 50)
        lungime = random.randint(1, 15)
        nume = random_string(lungime)
        grupa = random.randint(1, 10)
        student = Student(id_student, nume, grupa)
        self.__validator_student.valideazaStudent(student)
        self.__repo_studenti.adauga(student)

    def __len__(self):
        return self.__repo_studenti.__len__()
