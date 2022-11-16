class HMIFProject:
    def __init__(self):
        self.name = None
        self.description = None
        self.language = None
        self.pattern = None
        self.framework = None
    
    def getHMIFProject(self):
        str = "HMIF New Project Development wants to be started \n"

        str += f"Project Name: {self.name}\n"
        str += f"Project Description: {self.description}\n"
        str += f"Project Programming Language: {self.language}\n"
        str += f"Project Development Pattern: {self.pattern}\n"
        str += f"Project Framework: {self.framework}\n"

        return str
