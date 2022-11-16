from BlogHmifBuilder import BlogHmifBuilder
from TokoIFBuilder import TokoIFBuilder

builder = BlogHmifBuilder()
builder.setLanguage("Javascript").setFramework("ReactJS").setPattern("MVC")
builder.buildProject()
print(builder.getHMIFProject())

builder = TokoIFBuilder()
builder.setLanguage("Java").setFramework("Django").setPattern("MVC")
builder.buildProject()
print(builder.getHMIFProject())