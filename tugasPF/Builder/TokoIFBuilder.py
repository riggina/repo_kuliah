from Hmif import HMIFProject
from HmifBuilder import HMIFBuilder

class TokoIFBuilder(HMIFBuilder):
    def __init__(self):
        self.project = HMIFProject()

    def setName(self):
        self.project.name= "Toko IF HMIF ITK"
        return self
    
    def setDescription(self):
        self.project.description = "Menyediakan Merchandise Seputar Informatika"
        return self

    def setLanguage(self, language):
        self.project.language = language
        return self
    
    def setPattern(self, pattern):
        self.project.pattern = pattern
        return self

    def setFramework(self, framework):
        self.project.framework = framework
        return self
    
    def buildProject(self):
        self.setName()
        self.setDescription()
    
    def getHMIFProject(self):
        return self.project.getHMIFProject()