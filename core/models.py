import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from pictures.models import PictureField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField(_('Criação'), auto_now_add=True)
    modificado = models.DateField(_('Atualização'), auto_now=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Grafico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )
    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField(_('Cargo'), max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField(_('Nome'), max_length=100)
    cargo = models.ForeignKey(Cargo, verbose_name=_('Cargo'), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    imagem = PictureField(
        verbose_name=_('Imagem'),
        upload_to=get_file_path,
        width_field='imagem_width',  # Adicione esta linha
        height_field='imagem_height',  # Adicione esta linha
        null=True,
        blank=True
    )
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    imagem_width = models.PositiveIntegerField(null=True, blank=True)  # Adicione esta linha
    imagem_height = models.PositiveIntegerField(null=True, blank=True)  # Adicione esta linha

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return self.nome


class Recursos(Base):
    ICONE_CHOICES = (
        ('lni-rocket', _('Foguete')),
        ('lni-laptop-phone', _('Laptop')),
        ('lni-cog', _('Engrenagem')),
        ('lni-leaf', _('Design')),
        ('lni-layers', _('Cores')),
    )
    recurso = models.CharField(_('Recurso'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Ícone'), max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Recurso')
        verbose_name_plural = _('Recursos')

    def __str__(self):
        return self.recurso

