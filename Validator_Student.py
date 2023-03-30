from Exceptii.Exceptii import ValidationException


class ValidatorStudent:
    def valideazaStudent(self, student):
        """
        Valideaza un student
        :param student: un obiect de tip student
        :return: -; daca studentul este invalid
                 arunca exceptie de tip ValidationException daca datele sunt incorecte
        """
        errors = ""
        if student.getIdStudent() < 0:
            errors += "Id-ul studentului este invalid!\n"
        if len(student.getNumeStudent()) <=1:
            errors += "Numele studentului este invalid!\n"
        if student.getGrupaStudent() <= 0:
            errors += "Grupa studentului este invalida!\n"
        if len(errors) > 0:
            raise ValidationException(errors)
