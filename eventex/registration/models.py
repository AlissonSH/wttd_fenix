from django.db import models
from eventex.subscriptions.validators import validate_cpf


class Registration(models.Model):
    student = models.ForeignKey('subscriptions.Subscription', verbose_name='Aluno', on_delete=models.PROTECT)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    phone = models.CharField('Telefone', max_length=20, blank=True)
    observation = models.CharField('Observação', max_length=2500, blank=True)

    class Meta:
        verbose_name_plural = "Participantes"
        verbose_name = "Participante"

    def __str__(self):
        return self.student.name
