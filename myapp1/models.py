from distutils.command.upload import upload
from django.db import models

class Baza_client(models.Model):
    
    # STATUSE_CASES = (("Підготовка документів","Підготовка документів" ),
    #                 (" Справа перебуває на розгляді суду "," Справа перебуває на розгляді суду "), 
    #                 ("Справа закрита", "Справа закрита" ) )
 
    # TYPE_CASE = (("Кримінальна","Кримінальна"  ), 
    #              ( "Процесуальна","Процесуальна"),
    #              ("Адміністративна","Адміністративна")
    #               )
   
    name_client = models.CharField('ПІБ клієнта',max_length= 100)
    contract_number = models.IntegerField('Номер договору')
    date_contract = models.DateField('Дата договору'  )
    type_case = models.ForeignKey('TypeCase',  null = True, on_delete=models.CASCADE)
    date = models.DateField('Дата подачі справи')
    status_case = models.ForeignKey('StatusCase', null = True, on_delete=models.CASCADE)
    documents_case = models.FileField('Загрузка документів', upload_to = 'DownloadFile/%Y/%m/%d/')

    def __str__(self):
        return self.name_client

class StatusCase(models.Model):
    NameStatusCase = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.NameStatusCase



class TypeCase(models.Model):
    NameTypeCase = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.NameTypeCase


