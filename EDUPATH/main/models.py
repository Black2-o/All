from django.db import models

class Classes(models.Model):
    name= models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name
    
class Books(models.Model):
    name= models.CharField(max_length=200, null=True)
    classe= models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
    
class Chapter(models.Model):
    name= models.CharField(max_length=200, null=True)
    classe= models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    book= models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
    
class SingleClass(models.Model):
    url= models.CharField(max_length=200, null=True)
    classe= models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    book= models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    chapter= models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)


class BookPdf(models.Model):
    name= models.CharField(max_length=200, null=True)
    url= models.CharField(max_length=800, null=True)
    
    def __str__(self) -> str:
        return self.name