from Hmif import HMIFProject

blogHMIF = HMIFProject()
blogHMIF.setName("Blog Himpunan Mahasiswa Informatika")
blogHMIF.setDescription("Berikut merupakan blog khusus HMIF ITK")
blogHMIF.setLanguage("PHP")
blogHMIF.setPattern("MVC")
blogHMIF.setFramework("Laravel")
print(blogHMIF.getHMIFProject())

TokoIF = blogHMIF.copyHMIFWeb()
TokoIF.setName("Toko IF HMIF ITK")
TokoIF.setDescription("Toko Online Merchandise HMIF ITK")
TokoIF.setHmifCopied("Hacking")
print(TokoIF.getHMIFProject())