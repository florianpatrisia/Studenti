import unittest

from Domain.nota import Nota
from Domain.problema_lab import ProblemaLab
from Domain.student import Student
from Exceptii.Exceptii import RepoException, ValidationException
from Repository.RepoNote import RepositoryNote
from Repository.RepoProblemaLab import RepoProblemaLab
from Repository.RepoStudenti import RepositoryStudenti
from Service.serviceStudenti import ServiceStudenti
from Validare.ValidatorNota import ValidatorNota
from Validare.Validator_Problema import ValidatorProblema
from Validare.Validator_Student import ValidatorStudent


def ruleaza_teste_unit():
    domain = TestCaseDomeniu()
    domain.setUp()
    domain.test_student()
    domain.test_probleme_lab()
    domain.test_nota()

    repo = TestCaseRepository()
    repo.setUp()
    repo.test_repo_studenti()
    repo.test_repo_problema()
    repo.test_repo_note()

    valid = TestCaseValidare()
    valid.setUp()
    valid.test_validare_student()
    valid.test_validare_problema_lab()
    valid.test_validare_nota()

    service = TestCaseService()
    service.setUp()
    service.test_service_studenti()


class TestCaseDomeniu(unittest.TestCase):
    def setUp(self) -> None:
        self.__student1 = Student(1, "nume1", 2)
        self.__student2 = Student(2, "nume2", 4)
        self.__student3 = Student(3, "nume3", 7)
        self.__problema1 = ProblemaLab(1, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema2 = ProblemaLab(2, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema3 = ProblemaLab(3, [5, 6], "laborator 5, problema 6", 2025 - 2 - 12)
        self.__nota1 = Nota(1, 1, 1, 5)
        self.__nota2 = Nota(2, 2, 1, 3)
        self.__nota3 = Nota(3, 3, 1, 2)

    def test_student(self):
        """
        Testeaza functiile din clasa Student
        :return: -
        """
        self.assertEqual(self.__student1.getIdStudent(), 1)
        self.assertEqual(self.__student1.getNumeStudent(), "nume1")
        self.assertEqual(self.__student1.getGrupaStudent(), 2)
        self.__student1.setNumeStudent("nume2")
        self.assertEqual(self.__student1.getNumeStudent(), "nume2")
        self.assertEqual(str(self.__student1), "ID student: 1, nume: nume2, grupa: 2")
        self.__student2.setGrupaStudent(2)
        self.assertNotEqual(self.__student1, self.__student2)

    def test_probleme_lab(self):
        """
        Testeaza functiile din clasa ProblemaLab
        :return: -
        """
        self.assertEqual(self.__problema1.getIdProblema(), 1)
        self.assertEqual(self.__problema1.getNrLaborator_Problema(), [2, 3])
        self.assertEqual(self.__problema1.getDescriereProblema(), "laborator 2, problema 3")
        self.assertEqual(self.__problema1.getDeadlineProblema(), 2023 - 4 - 5)
        self.__problema1.setDeadlineProblema(2028 - 1 - 1)
        self.assertEqual(self.__problema1.getDeadlineProblema(), 2028 - 1 - 1)
        self.__problema1.setDescriereProblema("descriere noua")
        self.assertEqual(self.__problema1.getDescriereProblema(), "descriere noua")
        # self.assertEqual(str(self.__problema1), "Id-ul problemei: 1 Numar laborator si problema: [2, 3], descriere: descriere noua, deadline: 2026")

    def test_nota(self):
        """
        Testeaza functiile din clasa Nota
        :return: -
        """
        self.assertEqual(self.__nota1.getIdNota(), 1)
        self.assertEqual(self.__nota1.getIdStudent(), 1)
        self.assertEqual(self.__nota1.getIdNota(), 1)
        self.assertEqual(self.__nota1.getValoareNota(), 5)
        self.__nota1.setValoareNota(10)
        self.assertEqual(self.__nota1.getValoareNota(), 10)


class TestCaseValidare(unittest.TestCase):
    def setUp(self):
        self.__validator_student = ValidatorStudent()
        self.__student1 = Student(1, "numeStudnet", 8)
        self.__student2 = Student(0, "2", -5)
        self.__student3 = Student(-8, "n", 7)
        self.__student4 = Student(-1, "", 0)

        self.__validator_problema = ValidatorProblema()
        self.__problema1 = ProblemaLab(1, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema2 = ProblemaLab(-2, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema3 = ProblemaLab(3, [-5, 6], "laborator 5, problema 6", 2025 - 2 - 12)
        self.__problema4 = ProblemaLab(4, [7, -16], "laborator 7, problema -16", 2025 - 2 - 12)
        self.__problema5 = ProblemaLab(5, [8, 4], "", 2025 - 2 - 12)
        self.__problema6 = ProblemaLab(-6, [-9, -5], "a", 2025 - 2 - 12)

        self.__validator_nota = ValidatorNota()
        self.__nota1 = Nota(1, 1, 1, 5)
        self.__nota2 = Nota(-2, 2, 1, 3)
        self.__nota3 = Nota(3, -3, 1, 2)
        self.__nota4 = Nota(4, 6, -1, 2)
        self.__nota5 = Nota(5, 7, 1, -2)
        self.__nota6 = Nota(-6, -3, -1, -2)

    def test_validare_student(self):
        self.__validator_student.valideazaStudent(self.__student1)
        self.assertRaises(ValidationException, self.__validator_student.valideazaStudent, self.__student2)
        self.assertRaises(ValidationException, self.__validator_student.valideazaStudent, self.__student3)
        self.assertRaises(ValidationException, self.__validator_student.valideazaStudent, self.__student4)

    def test_validare_problema_lab(self):
        self.__validator_problema.valideazaProblema(self.__problema1)
        self.assertRaises(ValidationException, self.__validator_problema.valideazaProblema, self.__problema2)
        self.assertRaises(ValidationException, self.__validator_problema.valideazaProblema, self.__problema3)
        self.assertRaises(ValidationException, self.__validator_problema.valideazaProblema, self.__problema4)
        self.assertRaises(ValidationException, self.__validator_problema.valideazaProblema, self.__problema5)
        self.assertRaises(ValidationException, self.__validator_problema.valideazaProblema, self.__problema6)

    def test_validare_nota(self):
        self.__validator_nota.valideazaNota(self.__nota1)
        self.assertRaises(ValidationException, self.__validator_nota.valideazaNota, self.__nota2)
        self.assertRaises(ValidationException, self.__validator_nota.valideazaNota, self.__nota3)
        self.assertRaises(ValidationException, self.__validator_nota.valideazaNota, self.__nota4)
        self.assertRaises(ValidationException, self.__validator_nota.valideazaNota, self.__nota5)
        self.assertRaises(ValidationException, self.__validator_nota.valideazaNota, self.__nota6)


class TestCaseRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.__repoStudenti = RepositoryStudenti()
        self.__student1 = Student(1, "nume1", 2)
        self.__student2 = Student(2, "nume2", 4)
        self.__student3 = Student(3, "nume3", 7)
        self.__student4 = Student(4, "nume4", 5)
        self.__student5 = Student(5, "nume5", 3)
        self.__student6 = Student(6, "nume6", 1)
        self.__student7 = Student(7, "nume7", 7)

        self.__repoProbleme = RepoProblemaLab()
        self.__problema1 = ProblemaLab(1, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema2 = ProblemaLab(2, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema3 = ProblemaLab(3, [5, 6], "laborator 5, problema 6", 2025 - 2 - 12)

        self.__repoNote = RepositoryNote()
        self.__nota1 = Nota(1, 1, 1, 5)
        self.__nota2 = Nota(2, 2, 1, 3)
        self.__nota3 = Nota(3, 3, 1, 2)
        self.__nota4 = Nota(4, 4, 1, 9)
        self.__nota5 = Nota(5, 5, 1, 2)
        self.__nota6 = Nota(6, 6, 1, 1)

    def test_repo_studenti(self):
        # ADAUGA
        self.__repoStudenti = RepositoryStudenti()
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 0)
        self.__repoStudenti.adauga(self.__student1)
        self.__repoStudenti.adauga(self.__student2)
        self.__repoStudenti.adauga(self.__student3)
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 3)

        self.__repoStudenti.adauga(self.__student4)
        self.__repoStudenti.adauga(self.__student5)
        self.__repoStudenti.adauga(self.__student6)
        self.__repoStudenti.adauga(self.__student7)

        self.assertTrue(len(studenti) == 7)
        self.assertTrue(studenti[1].getIdStudent() == 2)
        self.assertTrue(studenti[1].getNumeStudent() == "nume2")
        self.assertTrue(studenti[1].getGrupaStudent() == 4)
        self.assertTrue(studenti[2].getIdStudent() == 3)
        self.assertTrue(studenti[2].getNumeStudent() == "nume3")
        self.assertTrue(studenti[2].getGrupaStudent() == 7)
        self.assertTrue(studenti[6].getIdStudent() == 7)
        self.assertTrue(studenti[6].getNumeStudent() == "nume7")
        self.assertTrue(studenti[6].getGrupaStudent() == 7)

        # GET BY ID
        studentCautat1 = self.__repoStudenti.getStudentById(1)
        self.assertTrue(studentCautat1 == self.__student1)
        self.assertTrue(studentCautat1.getIdStudent() == 1)
        self.assertTrue(studentCautat1.getNumeStudent() == "nume1")
        self.assertTrue(studentCautat1.getGrupaStudent() == 2)
        studentCautat2 = self.__repoStudenti.getStudentById(2)
        self.assertTrue(studentCautat2 == self.__student2)
        self.assertTrue(studentCautat2.getIdStudent() == 2)
        self.assertTrue(studentCautat2.getNumeStudent() == "nume2")
        self.assertTrue(studentCautat2.getGrupaStudent() == 4)

        # STERGE
        self.__repoStudenti.sterge(1)
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 6)
        self.__repoStudenti.sterge(7)
        self.__repoStudenti.sterge(6)
        self.__repoStudenti.sterge(5)
        self.assertTrue(len(studenti) == 3)
        self.assertRaises(RepoException, self.__repoStudenti.sterge, 100)

        # MODIFICA
        self.assertTrue(len(studenti) == 3)
        self.__repoStudenti.modifica(2, "numeNou", 9)
        student = self.__repoStudenti.getStudentById(2)
        self.assertEqual(student.getIdStudent(), 2)
        self.assertEqual(student.getNumeStudent(), "numeNou")
        self.assertEqual(student.getGrupaStudent(), 9)

        self.__repoStudenti.modifica(3, "marcel", 3)
        student = self.__repoStudenti.getStudentById(3)
        self.assertEqual(student.getIdStudent(), 3)
        self.assertEqual(student.getNumeStudent(), "marcel")
        self.assertEqual(student.getGrupaStudent(), 3)
        self.assertNotEqual(student.getNumeStudent(), "nume3")

    def test_repo_problema(self):
        # ADAUGA
        probleme = self.__repoProbleme.getAll()
        self.assertTrue(len(probleme) == 0)
        self.__repoProbleme.adauga(self.__problema1)
        self.assertEqual(len(self.__repoProbleme.getAll()), 1)
        self.__repoProbleme.adauga(self.__problema2)
        self.assertEqual(len(self.__repoProbleme.getAll()), 2)
        self.__repoProbleme.adauga(self.__problema3)
        self.assertEqual(len(self.__repoProbleme.getAll()), 3)

        # GET BY ID
        # self.__problema3 = ProblemaLab(3, [5, 6], "laborator 5, problema 6", 2025 - 2 - 12)
        ProblemaCautata1 = self.__repoProbleme.getProblemaById(3)
        self.assertTrue(ProblemaCautata1 == self.__problema3)
        self.assertTrue(ProblemaCautata1.getIdProblema() == 3)
        self.assertTrue(ProblemaCautata1.getNrLaborator_Problema() == [5, 6])
        self.assertTrue(ProblemaCautata1.getDescriereProblema() == "laborator 5, problema 6")
        self.assertTrue(ProblemaCautata1.getDeadlineProblema() == 2025 - 2 - 12)

        ProblemaCautata2 = self.__repoProbleme.getProblemaById(1)
        self.assertTrue(ProblemaCautata2 == self.__problema1)
        self.assertTrue(ProblemaCautata2.getIdProblema() == 1)
        self.assertTrue(ProblemaCautata2.getNrLaborator_Problema() == [2, 3])
        self.assertTrue(ProblemaCautata2.getDescriereProblema() == "laborator 2, problema 3")
        self.assertTrue(ProblemaCautata2.getDeadlineProblema() == 2023 - 4 - 5)

        # STERGE
        self.assertTrue(len(self.__repoProbleme.getAll()) == 3)
        self.__repoProbleme.sterge(3)
        self.assertEqual(len(self.__repoProbleme.getAll()), 2)
        self.__repoProbleme.sterge(2)
        self.assertEqual(len(self.__repoProbleme.getAll()), 1)
        self.__repoProbleme.sterge(1)
        self.assertEqual(len(self.__repoProbleme.getAll()), 0)

        # MODIFICA
        self.__repoProbleme.adauga(self.__problema1)
        self.__repoProbleme.adauga(self.__problema2)
        self.__repoProbleme.adauga(self.__problema3)
        self.assertTrue(len(self.__repoProbleme.getAll()) == 3)
        self.__repoProbleme.modifica(2, [5, 6], "descrierenoua", 2030 - 4 - 5)
        problema = self.__repoProbleme.getProblemaById(2)
        self.assertTrue(problema.getIdProblema() == 2)
        self.assertTrue(problema.getNrLaborator_Problema() == [5, 6])
        self.assertTrue(problema.getDescriereProblema() == "descrierenoua")
        self.assertTrue(problema.getDeadlineProblema() == 2030 - 4 - 5)

    def test_repo_note(self):
        # ADAUGA
        note = self.__repoNote.getAll()
        self.assertTrue(len(note) == 0)
        self.__repoNote.adauga(self.__nota1)
        self.assertEqual(len(self.__repoNote.getAll()), 1)
        self.__repoNote.adauga(self.__nota2)
        self.assertEqual(len(self.__repoNote.getAll()), 2)
        self.__repoNote.adauga(self.__nota3)
        self.assertEqual(len(self.__repoNote.getAll()), 3)
        self.__repoNote.adauga(self.__nota4)
        self.assertEqual(len(self.__repoNote.getAll()), 4)
        self.__repoNote.adauga(self.__nota5)
        self.assertEqual(len(self.__repoNote.getAll()), 5)
        self.__repoNote.adauga(self.__nota6)
        self.assertEqual(len(self.__repoNote.getAll()), 6)

        # GET BY ID
        NotaCautata1 = self.__repoNote.getNotaById(1)
        self.assertTrue(NotaCautata1 == self.__nota1)
        self.assertTrue(NotaCautata1.getIdNota() == 1)
        self.assertTrue(NotaCautata1.getIdStudent() == 1)
        self.assertTrue(NotaCautata1.getIdProblemaLab() == 1)
        self.assertTrue(NotaCautata1.getValoareNota() == 5)

        NotaCautata2 = self.__repoNote.getNotaById(5)
        self.assertTrue(NotaCautata2 == self.__nota5)
        self.assertTrue(NotaCautata2.getIdNota() == 5)
        self.assertTrue(NotaCautata2.getIdStudent() == 5)
        self.assertTrue(NotaCautata2.getIdProblemaLab() == 1)
        self.assertTrue(NotaCautata2.getValoareNota() == 2)

        # STERGE
        self.assertEqual(len(self.__repoNote.getAll()), 6)
        self.__repoNote.sterge(6)
        self.assertEqual(len(self.__repoNote.getAll()), 5)
        self.__repoNote.sterge(5)
        self.assertEqual(len(self.__repoNote.getAll()), 4)
        self.__repoNote.sterge(4)
        self.assertEqual(len(self.__repoNote.getAll()), 3)
        self.__repoNote.sterge(3)
        self.assertEqual(len(self.__repoNote.getAll()), 2)

        # MODIFICA
        self.__repoNote.adauga(self.__nota5)
        self.__repoNote.adauga(self.__nota6)
        self.assertEqual(len(self.__repoNote.getAll()), 4)
        self.__repoNote.modifica(1, 5)
        nota = self.__repoNote.getNotaById(1)
        self.assertTrue(nota.getValoareNota() == 5)
        self.__repoNote.modifica(2, 8)
        nota = self.__repoNote.getNotaById(2)
        self.assertTrue(nota.getValoareNota() == 8)
        self.__repoNote.modifica(5, 9)
        nota = self.__repoNote.getNotaById(5)
        self.assertTrue(nota.getValoareNota() == 9)
        self.__repoNote.modifica(5, 10)
        nota = self.__repoNote.getNotaById(5)
        self.assertTrue(nota.getValoareNota() == 10)


class TestCaseService(unittest.TestCase):
    def setUp(self) -> None:
        self.__validStudent = ValidatorStudent()
        self.__repoStudneti = RepositoryStudenti()
        self.__serviceStudenti = ServiceStudenti(self.__validStudent, self.__repoStudneti)

        self.__student1 = Student(1, "nume1", 2)
        self.__student2 = Student(2, "nume2", 4)
        self.__student3 = Student(3, "nume3", 7)
        self.__student4 = Student(4, "nume4", 5)
        self.__student5 = Student(5, "nume5", 3)
        self.__student6 = Student(6, "nume6", 1)
        self.__student7 = Student(7, "nume7", 7)
        self.__repoStudneti.adauga(self.__student1)
        self.__repoStudneti.adauga(self.__student2)
        self.__repoStudneti.adauga(self.__student3)
        self.__repoStudneti.adauga(self.__student4)
        self.__repoStudneti.adauga(self.__student5)
        self.__repoStudneti.adauga(self.__student6)
        self.__repoStudneti.adauga(self.__student7)

    def test_service_studenti(self):
        studenti = self.__serviceStudenti.getAll()
        self.assertTrue(len(studenti) == 7)
        self.__serviceStudenti.adaugaStudentService(8, "nume8", 6)
        self.assertTrue(len(studenti) == 8)
        self.assertRaises(RepoException, self.__serviceStudenti.adaugaStudentService, 1, "nume1", 2)
        self.assertRaises(RepoException, self.__serviceStudenti.adaugaStudentService, 4, "nume4", 5)
        self.assertRaises(RepoException, self.__serviceStudenti.adaugaStudentService, 7, "nume7", 7)
        self.assertRaises(ValidationException, self.__serviceStudenti.adaugaStudentService, -7, "n", 7)
        self.assertRaises(ValidationException, self.__serviceStudenti.adaugaStudentService, -7, "nume7", 7)
        self.assertRaises(ValidationException, self.__serviceStudenti.adaugaStudentService, -7, "", -52)
        self.assertTrue(len(studenti) == 8)


class TestCaseUIfunctions(unittest.TestCase):

    def setUp(self) -> None:
        # self.__functii = UI()

        self.__student1 = Student(1, "nume1", 2)
        self.__student2 = Student(2, "nume2", 4)
        self.__student3 = Student(3, "nume3", 7)
        self.__student4 = Student(4, "nume4", 5)
        self.__student5 = Student(5, "nume5", 3)
        self.__student6 = Student(6, "nume6", 1)
        self.__student7 = Student(7, "nume7", 7)

        self.__problema1 = ProblemaLab(1, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema2 = ProblemaLab(2, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema3 = ProblemaLab(3, [5, 6], "laborator 5, problema 6", 2025 - 2 - 12)

        self.__nota1 = Nota(1, 1, 1, 5)
        self.__nota2 = Nota(2, 2, 1, 3)
        self.__nota3 = Nota(3, 3, 1, 2)
        self.__nota4 = Nota(4, 4, 1, 9)
        self.__nota5 = Nota(5, 5, 1, 2)
        self.__nota6 = Nota(6, 6, 1, 1)

    def test_sortare(self):
        note_studenti = []
        note_studenti.append(self.__nota1)
        note_studenti.append(self.__nota2)
        note_studenti.append(self.__nota3)
        note_studenti.append(self.__nota4)
        note_studenti.append(self.__nota5)
        note_studenti.append(self.__nota6)
        # self.__functii.sortare_note(note_studenti)
        # self.assertTrue(note_studenti[0] == self.__nota6)
