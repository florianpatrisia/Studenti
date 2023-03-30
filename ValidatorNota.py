from Exceptii.Exceptii import ValidationException


class ValidatorNota:
    @staticmethod
    def valideazaNota(nota):
        """
        Valideaz o nota
        :param nota: nota ce trebuie validata
        :return: -; daca nota este valida
                arunca exceptie de tip ValidationExpception daca datele notei sunt incorecte
        """
        errors = ""
        if nota.getIdNota() <= 0:
            errors += "Id-ul notei este invalid!\n"
        if nota.getIdStudent() <= 0:
            errors += "Id-ul studentului este invalid!\n"
        if nota.getIdProblemaLab() <= 0:
            errors += "Numarulul laboratorului este invalid!\n"
        if nota.getValoareNota() < 1 or nota.getValoareNota() > 10:
            errors += "Valoarea notei este invalida!\n"
        if len(errors) > 0:
            raise ValidationException(errors)
