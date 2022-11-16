
#Singleton
class MahasiswaITK():
    
    bayarUKT = None
    nim = None


    __instance = None


    def __init__(self):
        if MahasiswaITK.__instance != None:
            raise Exception("Mahasiswa ITK")
        else:
            MahasiswaITK.__instance = self

    
    @staticmethod
    def getInstance():
        if MahasiswaITK.__instance == None:
            MahasiswaITK()
        return MahasiswaITK.__instance


