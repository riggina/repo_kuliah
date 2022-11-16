from AbstractFactory import OutfitKuliahFactory, OutfitRumahFactory

kuliah = OutfitKuliahFactory()
kuliah.getOutfit("Berkerah")
kuliah.getOutfit("Berkerah").Wear()

rumah = OutfitRumahFactory()
rumah.getOutfit("Bergambar")
rumah.getOutfit("Bergambar").Use()