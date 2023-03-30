from Repository.FileRepoNote import FileRepositoryNote
from Repository.FileRepoProbleme import FileRepoProblemeLab
from Repository.FileRepoStudenti import FileRepositoryStudenti
from Repository.RepoNote import RepositoryNote
from Service.ServiceNote import ServiceNota
from Testare.unit_tests import ruleaza_teste_unit
from UI.ui import UI
from Validare.ValidatorNota import ValidatorNota
from Validare.Validator_Problema import ValidatorProblema
from Validare.Validator_Student import ValidatorStudent
from Repository.RepoStudenti import RepositoryStudenti
from Repository.RepoProblemaLab import RepoProblemaLab
from Service.serviceStudenti import ServiceStudenti
from Service.ServiceProblemeLab import ServiceProbleme
from Testare.teste import Testare


def start():
    # unit test
    ruleaza_teste_unit()

    teste = Testare()
    teste.ruleaza_teste()

    validator_student = ValidatorStudent()
    validator_problema = ValidatorProblema()
    validator_nota = ValidatorNota()
    metoda = input("Introduceti metoda de persistenta(memorie/ fisier): ")
    if metoda == "memorie":
        repo_studenti = RepositoryStudenti()
        repo_probleme = RepoProblemaLab()
        repo_note = RepositoryNote()
    elif metoda == "fisier":
        repo_studenti = FileRepositoryStudenti("studenti.txt")
        repo_probleme = FileRepoProblemeLab("probleme.txt")
        repo_note = FileRepositoryNote("note.txt")
    else:
        print("Metoda de persistenta invalida!")
        return
    service_studenti = ServiceStudenti(validator_student, repo_studenti)
    service_probleme = ServiceProbleme(validator_problema, repo_probleme)
    service_note = ServiceNota(repo_note, repo_studenti, repo_probleme, validator_nota)
    consola = UI(service_studenti, service_probleme, service_note)
    consola.run()

    # repo_studenti = FileRepositoryStudenti("studenti.txt")
    # student = Student(1, "abc", 5)
    # repo_studenti.adauga(student)
    # #print(student.getIdStudent())
    # print(repo_studenti.getStudentById(student.getIdStudent()))
    #
    # repo_studenti=RepositoryStudenti()
    # student = Student(1, "abc", 5)
    # repo_studenti.adauga(student)
    # print(repo_studenti.getStudentById(1))

    # repo_studenti.adauga(Student(1, "nume 6", 1))
    # repo_studenti.adauga(Student(2, "nume 5", 5))
    # repo_studenti.adauga(Student(3, "nume 4", 2))
    # repo_studenti.adauga(Student(4, "nume 3", 7))
    # repo_studenti.adauga(Student(5, "nume 2", 1))
    # repo_studenti.adauga(Student(6, "nume 1", 3))
    # repo_studenti.adauga(Student(7, "nume 7", 9))
    # repo_studenti.adauga(Student(8, "nume 8", 4))
    # repo_studenti.adauga(Student(9, "nume 9", 5))
    # repo_studenti.adauga(Student(10, "nume 41", 7))
    # year = 2002
    # month = 7
    # day = 1
    # data = datetime(year, month, day)
    # repo_probleme.adauga(ProblemaLab(1, [2, 3], "laborator 2, problema 1", data))
    # year = 2003
    # month = 10
    # day = 27
    # data = datetime(year, month, day)
    # repo_probleme.adauga(ProblemaLab(2, [5, 6], "laborator 5, problema 6", data))
    # year = 2002
    # month = 6
    # day = 19
    # data = datetime(year, month, day)
    # repo_probleme.adauga(ProblemaLab(3, [10, 5], "laborator 10, problema 5", data))
    # year = 2002
    # month = 3
    # day = 8
    # data = datetime(year, month, day)
    # repo_probleme.adauga(ProblemaLab(4, [7, 1], "laborator 7, problema 1", data))
    # year = 2003
    # month = 11
    # day = 17
    # data = datetime(year, month, day)
    # repo_probleme.adauga(ProblemaLab(5, [2, 9], "laborator 2, problema 9", data))
    # year = 2030
    # month = 12
    # day = 24
    # data = datetime(year, month, day)
    # repo_probleme.adauga(ProblemaLab(6, [1, 3], "laborator 1, problema 3", data))
    # # id nota, id student, id problema, valoare nota
    # repo_note.adauga(Nota(1, 1, 1, 9))
    # repo_note.adauga(Nota(2, 2, 1, 7))
    # repo_note.adauga(Nota(3, 3, 1, 3))
    # repo_note.adauga(Nota(4, 4, 1, 6))
    # repo_note.adauga(Nota(5, 5, 1, 9))
    # repo_note.adauga(Nota(6, 6, 1, 3))
    # repo_note.adauga(Nota(7, 9, 1, 4))
    # repo_note.adauga(Nota(8, 7, 1, 4))
    # repo_note.adauga(Nota(9, 10, 1, 9))
    # repo_note.adauga(Nota(10, 8, 1, 2))
    # repo_note.adauga(Nota(11, 1, 2, 9))
    # repo_note.adauga(Nota(12, 2, 2, 1))
    # repo_note.adauga(Nota(13, 3, 2, 3))
    # repo_note.adauga(Nota(14, 4, 2, 1))
    # repo_note.adauga(Nota(15, 5, 2, 1))
    # repo_note.adauga(Nota(16, 5, 3, 3))
    # repo_note.adauga(Nota(17, 4, 3, 2))
    # repo_note.adauga(Nota(18, 3, 3, 2))
    # repo_note.adauga(Nota(19, 1, 3, 1))
    # repo_note.adauga(Nota(20, 2, 3, 3))


if __name__ == '__main__':
    start()
