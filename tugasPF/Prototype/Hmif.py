class HMIFProject(object):
        name = None
        description = None
        language = None
        pattern = None
        framework = None
        extra = None
        copied = None

        def setName(self, name):
            self.name= name
            return self
        
        def setDescription(self, description):
            self.description = description
            return self

        def setLanguage(self, language):
            self.language = language
            return self
        
        def setPattern(self, pattern):
            self.pattern = pattern
            return self

        def setFramework(self, framework):
            self.framework = framework
            return self

        def setHmifExtra(self, extra):
            self.extra = extra
            return self 

        def setHmifCopied(self, copied):
            self.copied = copied
            return self    
        
        def getHMIFProject(self):
            str = "HMIF New Project Development wants to be started \n"

            str += f"Project Name: {self.name}\n"
            str += f"Project Description: {self.description}\n"
            str += f"Project Programming Language: {self.language}\n"
            str += f"Project Development Pattern: {self.pattern}\n"
            str += f"Project Framework: {self.framework}\n"

            if self.extra is not None:
                str += f"Extra: {self.extra}\n"
            
            if self.copied is not None:
                str += f"Copied Using: {self.copied}\n"

            return str
        
        def copyHMIFWeb(self):
            return HMIFProject()\
                .setName(self.name)\
                .setDescription(self.description)\
                .setLanguage(self.language)\
                .setPattern(self.pattern)\
                .setFramework(self.framework)\
                .setHmifExtra(self.extra)\
                .setHmifCopied(self.copied)
