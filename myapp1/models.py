from django.urls import reverse_lazy
from django.db import models

class Baza_client(models.Model):
    name_client = models.CharField('ПІБ клієнта',max_length= 100)
    contract_number = models.IntegerField('Номер договору')
    date_contract = models.DateField('Дата договору'  )
    type_case = models.ForeignKey('TypeCase',  null = True, on_delete=models.CASCADE)
    date = models.DateField('Дата подачі справи')
    status_case = models.ForeignKey('StatusCase', null = True, on_delete=models.CASCADE)
    documents_case = models.FileField('Загрузка документів', null = True,  blank=True, upload_to = 'DownloadFile/%Y/%m/%d/')

    def __str__(self):
        return self.name_client

    def get_absolute_url(self):
        return reverse_lazy('home')

class TypeCase(models.Model):
    NameTypeCase = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.NameTypeCase


class StatusCase(models.Model):
    NameStatusCase = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.NameStatusCase

