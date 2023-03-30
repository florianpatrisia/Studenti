from Domain.nota import Nota
from Domain.problema_lab import ProblemaLab
from Domain.student import Student
from Exceptii.Exceptii import ValidationException, RepoException
from Repository.FileRepoNote import FileRepositoryNote
from Repository.FileRepoProbleme import FileRepoProblemeLab
from Repository.FileRepoStudenti import FileRepositoryStudenti
from Repository.RepoNote import RepositoryNote
from Repository.RepoProblemaLab import RepoProblemaLab
from Repository.RepoStudenti import RepositoryStudenti
from Service.ServiceNote import ServiceNota
from Service.ServiceProblemeLab import ServiceProbleme
from Service.serviceStudenti import ServiceStudenti
from Validare.ValidatorNota import ValidatorNota
from Validare.Validator_Problema import ValidatorProblema
from Validare.Validator_Student import ValidatorStudent


class Testare:

    @staticmethod
    def goleste_fisier(nume_fisier):
        with open(nume_fisier, "w") as f:
            f.write("")

    def test_domain_student(self):
        """
        Testeaza functiile get si set din clasa student
        """
        id_student = 1
        nume = "Nume1"
        grupa = 2
        student = Student(id_student, nume, grupa)
        assert student.getIdStudent() == id_student
        assert student.getNumeStudent() == nume
        assert student.getGrupaStudent() == grupa
        student.setNumeStudent("Nume2")
        assert student.getNumeStudent() == "Nume2"
        student.setNumeStudent("Nume3")
        assert student.getNumeStudent() == "Nume3"
        student.setGrupaStudent(3)
        assert student.getGrupaStudent() == 3
        student.setGrupaStudent(7)
        assert student.getGrupaStudent() == 7

    def test_adauga_student(self):
        """
        Functia de test pentu adaugarea unui student
        """
        repoStudenti = RepositoryStudenti()
        assert len(repoStudenti.getAll()) == 0
        student1 = Student(1, "nume1", 2)
        try:
            repoStudenti.adauga(student1)
            assert True
        except RepoException:
            assert False
        assert len(repoStudenti.getAll()) == 1

        student2 = Student(2, "nume2", 5)
        try:
            repoStudenti.adauga(student2)
            assert True
        except RepoException:
            assert False

        try:
            repoStudenti.adauga(student2)
            assert False
        except RepoException as re:
            assert str(re) == "Student existent!\n"

        assert len(repoStudenti.getAll()) == 2

        student3 = Student(3, "nume3", 6)
        repoStudenti.adauga(student3)
        assert len(repoStudenti.getAll()) == 3

        student4 = Student(4, "nume4", 2)
        repoStudenti.adauga(student4)
        assert len(repoStudenti.getAll()) == 4

        student5 = Student(5, "nume5", 2)
        try:
            repoStudenti.adauga(student5)
            assert True
        except RepoException:
            assert False
        assert len(repoStudenti.getAll()) == 5

    def test_getStudentById(self):
        """
        Functia de test pentru getStudentById()
        """
        repoStudenti = RepositoryStudenti()
        student1 = Student(1, "nume1", 2)
        repoStudenti.adauga(student1)
        student2 = Student(2, "nume2", 5)
        repoStudenti.adauga(student2)
        student3 = Student(3, "nume3", 6)
        repoStudenti.adauga(student3)
        student4 = Student(4, "nume4", 2)
        repoStudenti.adauga(student4)
        student5 = Student(5, "nume5", 2)
        repoStudenti.adauga(student5)
        assert repoStudenti.getStudentById(1) == student1
        assert repoStudenti.getStudentById(2) == student2
        assert repoStudenti.getStudentById(3) == student3
        assert repoStudenti.getStudentById(4) == student4
        assert repoStudenti.getStudentById(5) == student5

    def test_stergeStudent(self):
        """
        Functia de test pentru stergeStundent()
        """
        repoStudenti = RepositoryStudenti()
        studenti = repoStudenti.getAll()
        assert len(studenti) == 0
        student1 = Student(1, "nume1", 2)
        repoStudenti.adauga(student1)
        student2 = Student(2, "nume2", 5)
        repoStudenti.adauga(student2)
        student3 = Student(3, "nume3", 6)
        repoStudenti.adauga(student3)
        student4 = Student(4, "nume4", 2)
        repoStudenti.adauga(student4)
        student5 = Student(5, "nume5", 2)
        repoStudenti.adauga(student5)
        assert len(repoStudenti.getAll()) == 5
        repoStudenti.sterge(1)
        assert len(repoStudenti.getAll()) == 4
        repoStudenti.sterge(2)
        assert len(repoStudenti.getAll()) == 3
        repoStudenti.sterge(3)
        assert len(repoStudenti.getAll()) == 2
        repoStudenti.sterge(4)
        assert len(repoStudenti.getAll()) == 1
        repoStudenti.sterge(5)
        assert len(repoStudenti.getAll()) == 0

    def test_modificaStudent(self):
        """
        Functia de test pentru moficaStudent
        """
        repoStudenti = RepositoryStudenti()
        studenti = repoStudenti.getAll()
        assert len(studenti) == 0
        student1 = Student(1, "nume1", 2)
        repoStudenti.adauga(student1)
        student2 = Student(2, "nume2", 5)
        repoStudenti.adauga(student2)
        student3 = Student(3, "nume3", 6)
        repoStudenti.adauga(student3)
        student4 = Student(4, "nume4", 2)
        repoStudenti.adauga(student4)
        student5 = Student(5, "nume5", 2)
        repoStudenti.adauga(student5)
        nume_nou = "nume50"
        grupa_noua = 2
        repoStudenti.modifica(1, nume_nou, grupa_noua)
        student = repoStudenti.getStudentById(1)
        assert student.getNumeStudent() == "nume50"
        assert student.getGrupaStudent() == grupa_noua

        nume_nou = "Maria"
        grupa_noua = 6
        repoStudenti.modifica(5, nume_nou, grupa_noua)
        student = repoStudenti.getStudentById(5)
        assert student.getNumeStudent() == nume_nou
        assert student.getGrupaStudent() == grupa_noua

        nume_nou = "Andrei"
        grupa_noua = 2
        repoStudenti.modifica(1, nume_nou, grupa_noua)
        student = repoStudenti.getStudentById(1)
        assert student.getNumeStudent() == nume_nou
        assert student.getGrupaStudent() == grupa_noua

        nume_nou = "Cristina"
        grupa_noua = 6
        repoStudenti.modifica(3, nume_nou, grupa_noua)
        student = repoStudenti.getStudentById(3)
        assert student.getNumeStudent() == nume_nou
        assert student.getGrupaStudent() == grupa_noua

    def test_validare_student(self):
        """
        Testeaza functia de validare a unui student
        """
        valid = ValidatorStudent()
        student1 = Student(-1, "nume", 3)
        try:
            valid.valideazaStudent(student1)
            assert False
        except ValidationException as ve:
            assert str(ve) == "Id-ul studentului este invalid!\n"

        student2 = Student(1, "n", 2)
        try:
            valid.valideazaStudent(student2)
            assert False
        except ValidationException as ve:
            assert str(ve) == "Numele studentului este invalid!\n"

        student3 = Student(1, "nume student", 0)
        try:
            valid.valideazaStudent(student3)
            assert False
        except ValidationException as ve:
            assert str(ve) == "Grupa studentului este invalida!\n"

    def test_repo_file_studenti(self):
        """
        Testeaza functiile din repo-ul cu fisiere pentru studenti
        """
        nume_fisier = "Testare/studenti_test.txt"
        self.goleste_fisier(nume_fisier)
        repoFile = FileRepositoryStudenti(nume_fisier)

        # ADAUGA
        assert len(repoFile.getAll()) == 0
        student1 = Student(1, "nume1", 4)
        repoFile.adauga(student1)
        assert len(repoFile.getAll()) == 1
        student2 = Student(2, "nume2", 4)
        repoFile.adauga(student2)
        student3 = Student(3, "nume3", 4)
        student4 = Student(4, "nume4", 4)

        try:
            repoFile.adauga(student2)
            assert False
        except RepoException as re:
            assert str(re) == "Student existent!\n"

        try:
            repoFile.adauga(student4)
            assert True
        except RepoException:
            assert False
        repoFile.adauga(student3)

        assert len(repoFile.getAll()) == 4

        # STERGE

        repoFile.sterge(4)
        assert len(repoFile.getAll()) == 3

        try:
            repoFile.sterge(4)
            assert False
        except RepoException as re:
            assert str(re) == "Student inexistent!\n"

        try:
            repoFile.sterge(3)
            assert True
        except RepoException:
            assert False

        assert len(repoFile.getAll()) == 2

        # MODIFICA

        try:
            repoFile.modifica(1, "Marcela", 7)
            assert True
        except RepoException:
            assert False

        student = repoFile.getStudentById(1)
        assert student.getNumeStudent() == "Marcela"
        assert student.getGrupaStudent() == 7
        student3 = Student(3, "nume3", 4)
        student4 = Student(4, "nume4", 4)
        repoFile.adauga(student3)
        repoFile.adauga(student4)

        try:
            repoFile.modifica(7, "Ion", 6)
            assert False
        except RepoException as re:
            assert str(re) == "Student inexistent!\n"

        try:
            repoFile.modifica(4, "Darius", 4)
            assert True
        except RepoException:
            assert False
        student = repoFile.getStudentById(4)
        assert student.getNumeStudent() == "Darius"
        assert student.getGrupaStudent() == 4

        repoFile.modifica(3, "Iulia", 2)
        student = repoFile.getStudentById(3)
        assert student.getIdStudent() == 3
        assert student.getGrupaStudent() == 2
        assert student.getNumeStudent() == "Iulia"

    def test_service_studenti(self):
        """
        Testeaza functiile din service-ul de studenti
        """
        valid = ValidatorStudent()
        repo = RepositoryStudenti()
        service = ServiceStudenti(valid, repo)

        # ADAUGA
        assert len(service.getAll()) == 0
        service.adaugaStudentService(1, "nume1", 4)
        assert len(service.getAll()) == 1
        service.adaugaStudentService(2, "nume2", 4)

        try:
            service.adaugaStudentService(1, "nume1", 4)
            assert False
        except RepoException as re:
            assert str(re) == "Student existent!\n"
        except ValidationException:
            assert False

        try:
            service.adaugaStudentService(4, "", 4)
            assert False
        except RepoException:
            assert False
        except ValidationException as ve:
            assert str(ve) == "Numele studentului este invalid!\n"
        service.adaugaStudentService(3, "nume3", 4)

        assert len(service.getAll()) == 3

        # STERGE
        try:
            service.stergeStudentService(4)
            assert False
        except RepoException as re:
            assert str(re) == "Student inexistent!\n"
        except ValidationException:
            assert False

        assert len(service.getAll()) == 3

        try:
            service.stergeStudentService(3)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False

        try:
            service.stergeStudentService(30)
            assert False
        except RepoException as re:
            assert str(re) == "Student inexistent!\n"
        except ValidationException as ve:
            assert str(ve) == "Id-ul studentului este invalid!\n"

        assert len(service.getAll()) == 2

        # MODIFICA

        try:
            service.modificaStudentService(1, "Marcela", 7)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False
        student = service.getSudentByIDService(1)
        assert student.getNumeStudent() == "Marcela"
        assert student.getGrupaStudent() == 7
        service.adaugaStudentService(3, "nume3", 4)
        service.adaugaStudentService(4, "nume4", 4)

        try:
            service.modificaStudentService(-7, "", -66)
            assert True
        except RepoException as re:
            assert str(re) == "Student inexistent!\n"
        except ValidationException as ve:
            assert str(ve) == "Id-ul studentului este invalid!\nNumele studentului este invalid!\n" \
                              "Grupa studentului este invalida!\n"

        try:
            service.modificaStudentService(-4, "Darius", 4)
            assert False
        except RepoException as re:
            assert str(re) == "Student inexistent!\n"
        except ValidationException as ve:
            assert str(ve) == "Id-ul studentului este invalid!\n"

        try:
            service.modificaStudentService(4, "D", 4)
            assert True
        except RepoException:
            assert False
        except ValidationException as ve:
            assert str(ve) == "Numele studentului este invalid!\n"

        try:
            service.modificaStudentService(4, "Darius", 0)
            assert True
        except RepoException:
            assert False
        except ValidationException as ve:
            assert str(ve) == "Grupa studentului este invalida!\n"

        service.modificaStudentService(3, "Iulia", 2)
        student = service.getSudentByIDService(3)
        assert student.getIdStudent() == 3
        assert student.getGrupaStudent() == 2
        assert student.getNumeStudent() == "Iulia"

    def test_domain_problema(self):
        """
        Testeaza functiile get si set din clasa student
        """
        id_problema = 1
        nr_lab_pb = [2, 3]
        descriere = "problema 5"
        deadline = 2002 - 2 - 2
        problema = ProblemaLab(id_problema, nr_lab_pb, descriere, deadline)
        assert problema.getIdProblema() == id_problema
        assert problema.getNrLaborator_Problema() == nr_lab_pb
        assert problema.getDescriereProblema() == descriere
        assert problema.getDeadlineProblema() == deadline
        problema.setNrLaborator_Problema([4, 13])
        assert problema.getNrLaborator_Problema() == [4, 13]
        problema.setDescriereProblema("Problema 15")
        assert problema.getDescriereProblema() == "Problema 15"
        problema.setDeadlineProblema(2022 - 2 - 2)
        assert problema.getDeadlineProblema() == 2022 - 2 - 2

    def test_adauga_problema(self):
        """
        Functia de test pentru adaugarea unei probleme
        """
        repoProbleme = RepoProblemaLab()
        assert len(repoProbleme.getAll()) == 0
        problema1 = ProblemaLab(1, [1, 3], "pb3", 2004 - 5 - 6)
        repoProbleme.adauga(problema1)
        assert len(repoProbleme.getAll()) == 1
        problema2 = ProblemaLab(2, [2, 6], "pb66", 1999 - 6 - 7)
        repoProbleme.adauga(problema2)
        assert len(repoProbleme.getAll()) == 2
        problema3 = ProblemaLab(3, [3, 10], "pb100", 2030 - 5 - 6)
        repoProbleme.adauga(problema3)
        assert len(repoProbleme.getAll()) == 3
        problema4 = ProblemaLab(4, [4, 8], "pb8", 2040 - 12 - 23)
        repoProbleme.adauga(problema4)
        assert len(repoProbleme.getAll()) == 4
        problema5 = ProblemaLab(5, [5, 12], "pb12", 2022 - 4 - 1)
        repoProbleme.adauga(problema5)
        assert len(repoProbleme.getAll()) == 5

    def test_sterge_problema(self):
        """
        Functia de test pentru stergerea unei probleme
        """
        repoProbleme = RepoProblemaLab()
        assert len(repoProbleme.getAll()) == 0
        problema1 = ProblemaLab(1, [1, 3], "pb3", 2004 - 5 - 6)
        repoProbleme.adauga(problema1)
        problema2 = ProblemaLab(2, [2, 66], "pb66", 1999 - 6 - 7)
        repoProbleme.adauga(problema2)
        problema3 = ProblemaLab(3, [3, 100], "pb100", 2030 - 5 - 6)
        repoProbleme.adauga(problema3)
        problema4 = ProblemaLab(4, [4, 8], "pb8", 2040 - 12 - 23)
        repoProbleme.adauga(problema4)
        problema5 = ProblemaLab(5, [5, 12], "pb12", 2022 - 4 - 1)
        repoProbleme.adauga(problema5)
        assert len(repoProbleme.getAll()) == 5
        repoProbleme.sterge(1)
        assert len(repoProbleme.getAll()) == 4
        repoProbleme.sterge(2)
        assert len(repoProbleme.getAll()) == 3
        repoProbleme.sterge(3)
        assert len(repoProbleme.getAll()) == 2
        repoProbleme.sterge(4)
        assert len(repoProbleme.getAll()) == 1
        repoProbleme.sterge(5)
        assert len(repoProbleme.getAll()) == 0

    def test_modifica_problema(self):
        """
        Functia de test pentru modifica problema
        """
        repoProbleme = RepoProblemaLab()
        assert len(repoProbleme.getAll()) == 0
        problema1 = ProblemaLab(1, [1, 3], "pb3", 2004 - 5 - 6)
        repoProbleme.adauga(problema1)
        problema2 = ProblemaLab(2, [2, 66], "pb66", 1999 - 6 - 7)
        repoProbleme.adauga(problema2)
        problema3 = ProblemaLab(3, [3, 100], "pb100", 2030 - 5 - 6)
        repoProbleme.adauga(problema3)
        assert len(repoProbleme.getAll()) == 3
        numar_nou = [6, 30]
        descriere_noua = "lab6, pb30"
        deadline_nou = 2050 - 2 - 2
        repoProbleme.modifica(1, numar_nou, descriere_noua, deadline_nou)
        problema = repoProbleme.getProblemaById(1)
        assert problema.getNrLaborator_Problema() == numar_nou
        assert problema.getDescriereProblema() == descriere_noua
        assert problema.getDeadlineProblema() == deadline_nou

        numar_nou = [12, 3]
        descriere_noua = "lab12, pb3"
        deadline_nou = 2023 - 4 - 7
        repoProbleme.modifica(3, numar_nou, descriere_noua, deadline_nou)
        problema = repoProbleme.getProblemaById(3)
        assert problema.getNrLaborator_Problema() == [12, 3]
        assert problema.getDescriereProblema() == "lab12, pb3"
        assert problema.getDeadlineProblema() == 2023 - 4 - 7

        problema = repoProbleme.getProblemaById(2)
        assert problema.getNrLaborator_Problema() == [2, 66]
        assert problema.getDescriereProblema() == "pb66"
        assert problema.getDeadlineProblema() == 1999 - 6 - 7

        repoProbleme.modifica(2, [1, 14], "laborator 1, problema 14", 2025 - 6 - 1)
        problema = repoProbleme.getProblemaById(2)
        assert problema.getNrLaborator_Problema() == [1, 14]
        assert problema.getDescriereProblema() == "laborator 1, problema 14"
        assert problema.getDeadlineProblema() == 2025 - 6 - 1

    def test_validare_problema(self):
        """
        Testeaza functia de validare a unei probleme de laborator
        """
        valid = ValidatorProblema()
        problema = ProblemaLab(-11, [1, 3], "pb3", 2004 - 5 - 6)
        try:
            valid.valideazaProblema(problema)
            assert False
        except ValidationException as ve:
            assert str(ve) == "Id-ul problemei este invalid!\n"

        problema = ProblemaLab(1, [0, 0], "pb3", 2004 - 5 - 6)
        try:
            valid.valideazaProblema(problema)
            assert False
        except ValidationException as ve:
            assert str(ve) == "Numarul laboratorului este invalid!\nNumarul problemei este invalid!\n"

        problema = ProblemaLab(1, [7, 0], "pb3", 2004 - 5 - 6)
        try:
            valid.valideazaProblema(problema)
            assert False
        except ValidationException as ve:
            assert str(ve) == "Numarul problemei este invalid!\n"

        problema = ProblemaLab(1, [5, 6], "", 2004 - 5 - 6)
        try:
            valid.valideazaProblema(problema)
            assert False
        except ValidationException as ve:
            assert str(ve) == "Problema nu are descriere!\n"

    def test_file_repo_problema(self):
        """
        Testeaza functiile din repo-ul cu fisiere pentru disciplina
        """

        nume_fisier = "Testare/probleme_test.txt"
        self.goleste_fisier(nume_fisier)
        repoFile = FileRepoProblemeLab(nume_fisier)

        # ADAUGA
        assert len(repoFile.getAll()) == 0
        problema1 = ProblemaLab(1, [1, 3], "pb3", 2004 - 5 - 6)
        problema2 = ProblemaLab(2, [2, 6], "pb66", 1999 - 6 - 7)
        problema3 = ProblemaLab(3, [3, 10], "pb100", 2030 - 5 - 6)
        problema4 = ProblemaLab(4, [4, 8], "pb8", 2040 - 12 - 23)
        problema5 = ProblemaLab(5, [5, 12], "pb12", 2022 - 4 - 1)

        repoFile.adauga(problema1)
        assert len(repoFile.getAll()) == 1

        try:
            repoFile.adauga(problema1)
            assert False
        except RepoException as re:
            assert str(re) == "Problema cu acest id deja exista!"

        try:
            repoFile.adauga(problema2)
            assert True
        except RepoException:
            assert False

        assert len(repoFile.getAll()) != 3
        assert len(repoFile.getAll()) == 2
        repoFile.adauga(problema5)
        repoFile.adauga(problema4)
        try:
            repoFile.adauga(problema3)
            assert True
        except RepoException:
            assert False
        assert len(repoFile.getAll()) == 5

        # STERGE
        repoFile.sterge(5)
        assert len(repoFile.getAll()) == 4
        try:
            repoFile.sterge(5)
            assert False
        except RepoException as re:
            assert str(re) == "Problema inexistenta!\n"

        try:
            repoFile.sterge(1)
            assert True
        except RepoException:
            assert False
        assert len(repoFile.getAll()) == 3

        try:
            repoFile.sterge(3)
            assert True
        except RepoException:
            assert False
        assert len(repoFile.getAll()) == 2

        # MODIFICA
        try:
            repoFile.modifica(2, [1, 3], "pb3", 2004 - 5 - 6)
            assert True
        except RepoException:
            assert False
        problema = repoFile.getProblemaById(2)
        assert problema.getIdProblema() == 2
        assert problema.getNrLaborator_Problema()[0] == 1
        assert problema.getNrLaborator_Problema()[1] == 3
        assert problema.getDescriereProblema() == "pb3"

        repoFile.modifica(4, [5, 7], "descriere", 2024 - 7 - 8)
        problema = repoFile.getProblemaById(4)
        assert problema.getIdProblema() == 4
        assert problema.getNrLaborator_Problema()[0] == 5
        assert problema.getNrLaborator_Problema()[1] == 7
        assert problema.getDescriereProblema() == "descriere"

    def test_service_problema(self):
        """
        Testeaza functiile din service-ul de probleme de laborator
        """
        valid = ValidatorProblema()
        repo = RepoProblemaLab()
        service = ServiceProbleme(valid, repo)

        # ADAUGA
        assert len(service.getAll()) == 0

        service.adaugaProblemaService(1, [1, 3], "pb3", 2004 - 5 - 6)
        assert len(service.getAll()) == 1

        try:
            service.adaugaProblemaService(1, [1, 3], "pb3", 2004 - 5 - 6)
            assert False
        except RepoException as re:
            assert str(re) == "Problema cu acest id deja exista!"
        except ValidationException:
            assert False

        try:
            service.adaugaProblemaService(2, [2, 6], "pb66", 1999 - 6 - 7)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False

        assert len(service.getAll()) != 3
        assert len(service.getAll()) == 2
        service.adaugaProblemaService(5, [5, 12], "pb12", 2022 - 4 - 1)
        service.adaugaProblemaService(4, [4, 8], "pb8", 2040 - 12 - 23)
        try:
            service.adaugaProblemaService(3, [3, 10], "pb100", 2030 - 5 - 6)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False
        assert len(service.getAll()) == 5

        try:
            service.adaugaProblemaService(-13, [3, 10], "pb100", 2030 - 5 - 6)
            assert False
        except RepoException:
            assert False
        except ValidationException as ve:
            assert str(ve) == "Id-ul problemei este invalid!\n"

        try:
            service.adaugaProblemaService(8, [-5, 0], "", 2030 - 5 - 6)
            assert False
        except RepoException:
            assert False
        except ValidationException as ve:
            assert str(ve) == "Numarul laboratorului este invalid!\nNumarul problemei este invalid!\nProblema nu are " \
                              "descriere!\n"
        assert len(service.getAll()) == 5

        # STERGE
        service.stergeProblemaService(5)
        assert len(service.getAll()) == 4
        try:
            service.stergeProblemaService(5)
            assert False
        except RepoException as re:
            assert str(re) == "Problema inexistenta!\n"
        except ValidationException:
            assert False

        try:
            service.stergeProblemaService(1)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False
        assert len(service.getAll()) == 3

        try:
            service.stergeProblemaService(3)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False

        try:
            service.stergeProblemaService(-93)
            assert True
        except RepoException as re:
            assert str(re) == "Problema inexistenta!\n"
        except ValidationException as ve:
            assert str(ve) == "Id-ul problemei este invalid!\n"
        assert len(service.getAll()) == 2

        # MODIFICA
        try:
            service.modificaProblemaService(2, [1, 3], "pb3", 2004 - 5 - 6)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False
        problema = service.getProblemaByIdService(2)
        assert problema.getIdProblema() == 2
        assert problema.getNrLaborator_Problema()[0] == 1
        assert problema.getNrLaborator_Problema()[1] == 3
        assert problema.getDescriereProblema() == "pb3"

        service.modificaProblemaService(4, [5, 7], "descriere", 2024 - 7 - 8)
        problema = service.getProblemaByIdService(4)
        assert problema.getIdProblema() == 4
        assert problema.getNrLaborator_Problema()[0] == 5
        assert problema.getNrLaborator_Problema()[1] == 7
        assert problema.getDescriereProblema() == "descriere"

        try:
            service.modificaProblemaService(-3, [-1, -3], "", 2004 - 5 - 6)
            assert False
        except RepoException as re:
            assert str(re) == "Problema inexistenta!\n"
        except ValidationException as ve:
            assert str(ve) == "Id-ul problemei este invalid!\nNumarul laboratorului este invalid!\n" \
                              "Numarul problemei este invalid!\nProblema nu are descriere!\n"

    def test_domain_nota(self):
        """
        testeaza functiile get si set din clasa student
        """
        id_nota = 1
        id_student = 4
        id_problema = 3
        valoare_nota = 6.8
        nota = Nota(id_nota, id_student, id_problema, valoare_nota)
        assert nota.getIdNota() == 1
        assert nota.getIdStudent() == 4
        assert nota.getIdProblemaLab() == 3
        assert nota.getValoareNota() == 6.8

        nota.setValoareNota(7.9)
        assert nota.getValoareNota() == 7.9
        nota.setValoareNota(10.0)
        assert nota.getValoareNota() == 10.0

    def test_valideazaNota(self):
        """
        Testeaza functia de validare a unei note
        """
        valid = ValidatorNota()
        nota = Nota(0, 0, 6, 8)
        try:
            valid.valideazaNota(nota)
            assert False
        except ValidationException as ve:
            assert str(ve) == "Id-ul notei este invalid!\nId-ul studentului este invalid!\n"

    def test_adaugaNota(self):
        """
        Functia de test pentru adaugare unei note
        """
        repoNote = RepositoryNote()
        nota1 = Nota(1, 1, 1, 9.0)
        assert len(repoNote.getAll()) == 0
        repoNote.adauga(nota1)
        assert len(repoNote.getAll()) == 1
        nota2 = Nota(2, 6, 7, 5.8)
        nota3 = Nota(3, 7, 9, 7.8)
        nota4 = Nota(4, 3, 1, 0.8)
        nota5 = Nota(5, 2, 9, 10.0)
        repoNote.adauga(nota2)
        assert len(repoNote.getAll()) == 2
        repoNote.adauga(nota3)
        assert len(repoNote.getAll()) == 3
        repoNote.adauga(nota4)
        assert len(repoNote.getAll()) == 4
        repoNote.adauga(nota5)
        assert len(repoNote.getAll()) == 5

    def test_stergeNota(self):
        """
        Functia de test pentru stergerea unei note din repo
        """
        repoNote = RepositoryNote()
        assert len(repoNote.getAll()) == 0
        nota1 = Nota(1, 1, 1, 9.0)
        nota2 = Nota(2, 6, 7, 5.8)
        nota3 = Nota(3, 7, 9, 7.8)
        nota4 = Nota(4, 3, 1, 0.8)
        nota5 = Nota(5, 2, 9, 10.0)
        repoNote.adauga(nota1)
        repoNote.adauga(nota2)
        repoNote.adauga(nota3)
        repoNote.adauga(nota4)
        repoNote.adauga(nota5)
        assert len(repoNote.getAll()) == 5

        try:
            repoNote.sterge(4)
            assert True
        except RepoException:
            assert False

        try:
            repoNote.sterge(4)
            assert False
            # nu putem sa-l stergem inca o data pe 4, pentru ca fost sters mai inainte
        except RepoException:
            assert True
            # astfel se va arunca exceptie de tip RepoException cu mesajul "Nota inexistenta!"

        repoNote.sterge(2)
        assert len(repoNote.getAll()) == 3
        repoNote.sterge(5)
        assert len(repoNote.getAll()) == 2
        repoNote.sterge(1)
        assert len(repoNote.getAll()) == 1
        repoNote.sterge(3)
        assert len(repoNote.getAll()) == 0

    def test_modificaNota(self):
        """
        Functia de test pentru modificare unei note
        """
        repoNote = RepositoryNote()
        assert len(repoNote.getAll()) == 0
        nota1 = Nota(1, 1, 1, 9.0)
        nota2 = Nota(2, 6, 7, 5.8)
        nota3 = Nota(3, 7, 9, 7.8)
        repoNote.adauga(nota1)
        repoNote.adauga(nota2)
        repoNote.adauga(nota3)
        assert len(repoNote.getAll()) == 3

        nota = repoNote.getNotaById(1)
        assert nota.getValoareNota() == 9.0
        repoNote.modifica(1, 10.0)
        assert nota.getValoareNota() == 10.0

        nota = repoNote.getNotaById(3)
        assert nota.getValoareNota() == 7.8
        repoNote.modifica(3, 9.98)
        assert nota.getValoareNota() == 9.98

        nota = repoNote.getNotaById(2)
        assert nota.getValoareNota() == 5.8
        repoNote.modifica(2, 6.865)
        assert nota.getValoareNota() == 6.865

    def test_file_repo_note(self):
        """
        Testeaza functiile din repo-ul cu fisiere pentru note
        """
        nume_fisier = "Testare/note_test.txt"
        self.goleste_fisier(nume_fisier)
        repoFile = FileRepositoryNote(nume_fisier)

        # ADAUGA
        nota1 = Nota(1, 1, 1, 9.0)
        nota2 = Nota(2, 6, 7, 5.8)
        nota3 = Nota(3, 7, 9, 7.8)
        nota4 = Nota(4, 3, 1, 0.8)
        nota5 = Nota(5, 2, 9, 10.0)
        assert len(repoFile.getAll()) == 0

        try:
            repoFile.adauga(nota1)
            assert True
        except RepoException:
            assert False

        assert len(repoFile.getAll()) == 1

        try:
            repoFile.adauga(nota1)
            assert False
        except RepoException as re:
            assert str(re) == "Nota existenta!\n"

        repoFile.adauga(nota2)
        repoFile.adauga(nota3)

        try:
            repoFile.adauga(nota4)
            assert True
        except RepoException:
            assert False

        try:
            repoFile.adauga(nota5)
            assert True
        except RepoException:
            assert False

        assert len(repoFile.getAll()) == 5

        # STERGE

        try:
            repoFile.sterge(1)
            assert True
        except RepoException:
            assert False

        assert len(repoFile.getAll()) == 4

        try:
            repoFile.sterge(1)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"

        repoFile.sterge(3)
        repoFile.sterge(2)
        try:
            repoFile.sterge(3)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"

        assert len(repoFile.getAll()) == 2

        # MODIFICA
        repoFile.modifica(4, 4.5)
        nota = repoFile.getNotaById(4)
        assert nota.getValoareNota() == 4.5
        assert nota.getIdNota() == 4

        try:
            repoFile.modifica(5, 7.865)
            assert True
        except RepoException:
            assert False
        nota = repoFile.getNotaById(5)
        assert nota.getValoareNota() == 7.865
        assert nota.getIdNota() == 5

        try:
            repoFile.modifica(9, 7.865)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"

        nota1 = Nota(1, 1, 1, 9.0)
        nota2 = Nota(2, 6, 7, 5.8)
        repoFile.adauga(nota1)
        try:
            repoFile.modifica(1, 3.4)
            assert True
        except RepoException:
            assert False

        try:
            repoFile.modifica(2, 6.7)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"
        repoFile.adauga(nota2)
        try:
            repoFile.modifica(2, 6.7)
            assert True
        except RepoException:
            assert False

    def test_service_note(self):
        """
        Testeaza functiile din service-ul de note
        """
        valid = ValidatorNota()
        repoNote = RepositoryNote()
        repoStudenti = RepositoryStudenti()
        repoProbleme = RepoProblemaLab()
        service = ServiceNota(repoNote, repoStudenti, repoProbleme, valid)

        # ADAUGA
        assert len(service.getAll()) == 0

        try:
            service.adaugaNota(1, 1, 1, 9.0)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False

        assert len(service.getAll()) == 1

        try:
            service.adaugaNota(1, 1, 1, 9.0)
            assert False
        except RepoException as re:
            assert str(re) == "Nota existenta!\n"
        except ValidationException:
            assert False

        service.adaugaNota(2, 6, 7, 5.8)
        service.adaugaNota(3, 7, 9, 7.8)

        try:
            service.adaugaNota(4, 3, 1, 1.8)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert True

        try:
            service.adaugaNota(5, 2, 9, 10.0)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False

        assert len(service.getAll()) == 5

        try:
            service.adaugaNota(-75, 0, 9, 10.0)
            assert True
        except RepoException:
            assert False
        except ValidationException as ve:
            assert str(ve) == "Id-ul notei este invalid!\nId-ul studentului este invalid!\n"

        try:
            service.adaugaNota(8, 5, -7, -7.8)
            assert True
        except RepoException:
            assert False
        except ValidationException as ve:
            assert str(ve) == "Numarulul laboratorului este invalid!\nValoarea notei este invalida!\n"

            # STERGE

        try:
            service.stergeNota(1)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False
        assert len(service.getAll()) == 4

        try:
            service.stergeNota(1)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"
        except ValidationException:
            assert False

        service.stergeNota(3)
        service.stergeNota(2)
        try:
            service.stergeNota(3)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"
        except ValidationException:
            assert False

        assert len(service.getAll()) == 2

        # MODIFICA
        service.modificaNota(4, 4.5)
        nota = service.getNotaByIDService(4)
        assert nota.getValoareNota() == 4.5
        assert nota.getIdNota() == 4

        try:
            service.modificaNota(5, 7.865)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False
        nota = service.getNotaByIDService(5)
        assert nota.getValoareNota() == 7.865
        assert nota.getIdNota() == 5

        try:
            service.modificaNota(9, 7.865)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"
        except ValidationException:
            assert False

        service.adaugaNota(1, 1, 1, 9.0)
        try:
            service.modificaNota(1, 3.4)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False

        try:
            service.modificaNota(2, 6.7)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"
        except ValidationException:
            assert False
        service.adaugaNota(2, 6, 7, 5.8)
        try:
            service.modificaNota(2, 6.7)
            assert True
        except RepoException:
            assert False
        except ValidationException:
            assert False

        try:
            service.modificaNota(-8, -6.7)
            assert False
        except RepoException as re:
            assert str(re) == "Nota inexistenta!\n"
        except ValidationException as ve:
            assert str(ve) == "Id-ul notei este invalid!\nValoarea notei este invalida!\n"

    def ruleaza_teste(self):
        # Teste Student
        self.test_domain_student()
        self.test_adauga_student()
        self.test_getStudentById()
        self.test_stergeStudent()
        self.test_modificaStudent()
        self.test_validare_student()
        self.test_repo_file_studenti()
        self.test_service_studenti()

        # Teste Problema de laborator
        self.test_domain_problema()
        self.test_adauga_problema()
        self.test_sterge_problema()
        self.test_modifica_problema()
        self.test_validare_problema()
        self.test_file_repo_problema()
        self.test_service_problema()

        # Teste Nota
        self.test_domain_nota()
        self.test_valideazaNota()
        self.test_adaugaNota()
        self.test_stergeNota()
        self.test_modificaNota()
        self.test_file_repo_note()
        self.test_service_note()
