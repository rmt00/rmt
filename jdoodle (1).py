class Client:
    def __init__(self, name, loan):
        self.name = name
        self.__loan = loan

    def show(self):
        print("Name: ", self.name, 'Loan:', self.__loan)

cli = Client('Ari', 3000)

cli.show()