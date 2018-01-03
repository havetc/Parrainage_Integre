import csv
from participant import Parrain, Filleul


class csv_import(object):
    def __init__(self, filename):
        super().__init__()
        with open(filename, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            self.reader = csv.reader(csvfile, dialect)
            self.first_line = next(self.reader)
            self.data = [p for p in self.reader]

    def __str__(self, *args, **kwargs):
        # quick and dirty way to print the data read: the first line isn't contained in data
        return repr(self.first_line) + "\n".join([str(elem) for elem in self.data])

class database_creator():
    def __init__(self, filename_parrain, filename_filleul):
        parrains = csv_import(filename_parrain)
        filleuls = csv_import(filename_filleul)
        self.parrain_list = self.create_parrain_from_data(parrains)
        self.filleul_list = self.create_filleul_from_data(filleuls)

    def create_parrain_from_data(self, parrains):
        res = []
        for parrain in parrains.data:
            # it would be REALLY easier if the column name in the CSV were short and consistent
            res.append(Parrain(parrain[1], parrain[2], parrain[3], parrain[4],
                               parrain[5], parrain[6], parrain[7], parrain[8],
                               parrain[9], parrain[10], parrain[11], parrain[12:15], parrain[16]))
        return res

    def create_filleul_from_data(self, filleuls):
        res = []
        for filleul in filleuls.data:
            # it would be REALLY easier if the column name in the CSV were short and consistent
            res.append(Filleul(filleul[1], filleul[2], filleul[3], filleul[4],
                               filleul[5], filleul[6], filleul[7], filleul[8],
                               filleul[9], filleul[10], filleul[11], filleul[12:15]))
        return res


    def __str__(self):
        return "\n\n".join([str(e) for e in self.parrain_list]) + "\n\n"+\
               "\n\n".join([str(e) for e in self.filleul_list])

if __name__ == "__main__":
    # reader = csv_import("Exemple parrainage (parrain) - Feuille 1.csv")
    # print(reader)
    base = database_creator("Exemple parrainage (parrain) - Feuille 1.csv", "Exemple parrainage (filleul) - Feuille 1.csv")
    print(base)