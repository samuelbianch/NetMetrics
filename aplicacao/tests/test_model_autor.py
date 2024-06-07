from django.test import TestCase
from aplicacao.models import Autor
from datetime import datetime
import pytz

class AutorModelTest(TestCase):

    def setUp(self):
        self.timezone = pytz.UTC
        self.autor = Autor.objects.create(
            nome_autor='Nome do Autor',
            link_lattes='http://lattes.cnpq.br/1234567890123456',
            cpf='12345678901',
            resumo='Resumo do autor.',
            data_nascimento=datetime(1980, 1, 1, tzinfo=self.timezone)
        )

    def test_create_autor(self):
        autor = Autor.objects.create(
            nome_autor='Novo Autor',
            link_lattes='http://lattes.cnpq.br/6543210987654321',
            cpf='10987654321',
            resumo='Resumo do novo autor.',
            data_nascimento=datetime(1990, 2, 2, tzinfo=self.timezone)
        )
        self.assertEqual(autor.nome_autor, 'Novo Autor')
        self.assertEqual(autor.link_lattes, 'http://lattes.cnpq.br/6543210987654321')
        self.assertEqual(autor.cpf, '10987654321')
        self.assertEqual(autor.resumo, 'Resumo do novo autor.')
        self.assertEqual(autor.data_nascimento, datetime(1990, 2, 2, tzinfo=self.timezone))

    def test_read_autor(self):
        autor = Autor.objects.get(id=self.autor.id)
        self.assertEqual(autor.nome_autor, 'Nome do Autor')
        self.assertEqual(autor.link_lattes, 'http://lattes.cnpq.br/1234567890123456')
        self.assertEqual(autor.cpf, '12345678901')
        self.assertEqual(autor.resumo, 'Resumo do autor.')
        self.assertEqual(autor.data_nascimento, datetime(1980, 1, 1, tzinfo=self.timezone))

    def test_update_autor(self):
        self.autor.nome_autor = 'Autor Atualizado'
        self.autor.save()
        autor = Autor.objects.get(id=self.autor.id)
        self.assertEqual(autor.nome_autor, 'Autor Atualizado')

    def test_delete_autor(self):
        autor_id = self.autor.id
        self.autor.delete()
        with self.assertRaises(Autor.DoesNotExist):
            Autor.objects.get(id=autor_id)

    def test_autor_str(self):
        self.assertEqual(str(self.autor), 'Nome do Autor')
