class Participant:
    """
    ATM it could be possible to only use this class, but if specific criteria must be added in the future it will be
    easier with separate child class.
    """
    def __init__(self, firstName, lastName, age, sex, email, university, nationality, subject, hobbies, languages,
                 address):
        self.email = email
        self.age = age
        self.sex = sex
        self.subject = subject
        self.university = university
        self.hobbies = hobbies
        self.languages = languages
        self.nationality = nationality
        self.lastName = lastName
        self.firstName = firstName
        self.address = address

    def __str__(self):
        return " FN: %s | LN: %s | AGE: %s" \
               "\nSEX: %s| EM: %s|\nUNI: %s |" \
               "NA: %s | SU: %s| HO: %s\nLA: %s" % (self.firstName, self.lastName, self.age, self.sex,
                                                    self.email, self.university, self.nationality,
                                                    self.subject, self.hobbies,
                                                    self.languages)


class Parrain(Participant):
    def __init__(self, lastName, firstName, email, age, sex,
                 nationality, languages, address, hobbies, dateAvailable, university, subject, okWithMultipleFilleul):
        super().__init__(firstName, lastName, age, sex, email, university,
                         nationality, subject, hobbies, languages, address)
        self.dateAvailable = dateAvailable
        self.okWithMultipleFilleul = okWithMultipleFilleul

    def __str__(self):
        return "Parrain " + super().__str__() + "| DA " + self.dateAvailable


# filleul object contains all useful info about a filleul in a variable

class Filleul(Participant):
    def __init__(self, lastName, firstName, email, age, sex,
                 nationality, languages, address, hobbies, dateArrival, university, subject):
        super().__init__(firstName, lastName, age, sex, email, university,
                         nationality, subject, hobbies, languages, address)
        self.dateArrival = dateArrival

    def __str__(self):
        return "Filleul " + super().__str__() + "| DA " + self.dateArrival
