from Exceptii.Exceptii import ValidationException


class ValidatorProblema:

    def valideazaProblema(self, problema):
        """
        Valideaza o problema
        :param problema: un obiect de tip problema
        :return: eroare daca datele sunt incorecte
        """
        errors = ""
        if problema.getIdProblema() <= 0:
            errors += "Id-ul problemei este invalid!\n"
        if problema.getNrLaborator_Problema()[0] <= 0:
            errors += "Numarul laboratorului este invalid!\n"
        if problema.getNrLaborator_Problema()[1] <= 0:
            errors += "Numarul problemei este invalid!\n"
        if len(problema.getDescriereProblema()) <= 1:
            errors += "Problema nu are descriere!\n"
        # nu avem nevoie de validare pentru deadline pentru ca este de tip date si se face automat
        if len(errors) > 0:
            raise ValidationException(errors)
