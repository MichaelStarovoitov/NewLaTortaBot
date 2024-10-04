from common.fileWork import load_data, write_file


class userData:
    def __init__(self, path):
        self.path = path
        self.users = load_data(self.path)
    
    def appendUser(self, nUser):
        self.users.append(nUser)
        write_file(self.path, self.users)
    
    def checkUserById(self, idUser):
        return any(user['idChat'] == idUser for user in self.users)

    def returnUserById(self, idUser):
        return next((user for user in self.users if user['idChat'] == idUser), None)
    
    def cleanAll(self):
        write_file(self.path, [])