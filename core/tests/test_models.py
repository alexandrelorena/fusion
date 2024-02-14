import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTextCase(TestCase):

    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class RecursosTestCase(TestCase):

    def setUp(self):
        self.recurso = mommy.make('Recursos')

    def test_str(self):
        self.assertEquals(str(self.recurso), self.recurso.recurso)

