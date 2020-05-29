from django.db import models
from datetime import date

#Grava os dados inseridos via url externa
class Monitor(models.Model):
    # CNPJ da empresa
    company_document = models.name = models.CharField('C.N.P.J', max_length=30,blank=False, null=False)

    # Nome da empresa
    company_name = models.name = models.CharField('Razão Social', max_length=150,blank=False, null=False)
    
    # Nome da chave
    key_name = models.name = models.CharField('Chave', max_length=20, blank=False, null=False)
    
    # Identificador
    identify_name = models.name = models.CharField('Identificador', max_length=20, blank=False, null=False)

    # Valor do identificador
    data_value = models.name = models.CharField('Valor',max_length=200,blank=False,null=False)

	# Versão da sistema
    system_version = models.CharField('Versão', max_length=20, null=False, blank=False)
    
    # Date em que foi inserido a informação
    date_insert = models.DateField('Inserido em',default=date.today)

	# Data em que recebeu a informação
    date_update = models.DateField('Atualizado em',auto_now=True)

    def __str__(self):
        return self.company_document