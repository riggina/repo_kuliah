#Abstract Factory
class OutfitKuliah:
    def Wear(self):
        raise NotImplementedError("CreateProduct()")

class OutfitRumah:
    def Use(self):
        raise NotImplementedError("CreateProduct()")

#for OutfitKuliah
class Kemeja(OutfitKuliah):
    def Wear(self):
        print("Kemeja")

class PoloTshirt(OutfitKuliah):
    def Wear(self):
        print("Polo Tshirt")

class Blouse(OutfitKuliah):
    def Wear(self):
        print("Blouse")

class PDH(OutfitKuliah):
    def Wear(self):
        print("PDH")

#for Outfit Rumah
class Kaos(OutfitRumah):
    def Use(self):
        print("Kaos")
class Pajamas(OutfitRumah):
    def Use(self):
        print("Pajamas")
class Daster(OutfitRumah):
    def Use(self):
        print("Daster")

class OutfitFactoryInterface:
    def getOutfit(shape) : pass

class OutfitKuliahFactory(OutfitFactoryInterface):
    @staticmethod
    def getOutfit(shape):
        if shape == "Berkerah":
            return Kemeja()
        if shape == "Atribut Kampus":
            return PDH()
        assert "Nothing", "Shape Undefined"

class OutfitRumahFactory(OutfitFactoryInterface):
    @staticmethod
    def getOutfit(shape):
        if shape == "Bergambar":
            return Kemeja()
        if shape == "Tidak Berkerah":
            return PDH()
        assert "Nothing", "Shape Undefined"
