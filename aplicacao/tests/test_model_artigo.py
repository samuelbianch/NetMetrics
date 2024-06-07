from django.test import TestCase
from aplicacao.models import Autor, Artigo
from datetime import datetime
import pytz

class ArtigoModelTest(TestCase):

    def setUp(self):
        self.timezone = pytz.UTC
        self.autor1 = Autor.objects.create(
            nome_autor='Autor 1',
            link_lattes='http://lattes.cnpq.br/1111111111111111',
            cpf='12345678901',
            resumo='Resumo do autor 1.',
            data_nascimento=datetime(1980, 1, 1, tzinfo=self.timezone)
        )
        self.autor2 = Autor.objects.create(
            nome_autor='Autor 2',
            link_lattes='http://lattes.cnpq.br/2222222222222222',
            cpf='10987654321',
            resumo='Resumo do autor 2.',
            data_nascimento=datetime(1990, 2, 2, tzinfo=self.timezone)
        )
        self.artigo = Artigo.objects.create(
            nome_artigo='Nome do Artigo',
            doi='http://doi.org/123456',
            resumo='Resumo do artigo.'
        )
        self.artigo.autores.add(self.autor1, self.autor2)

    def test_create_artigo(self):
        artigo = Artigo.objects.create(
            nome_artigo='Novo Artigo',
            doi='http://doi.org/654321',
            resumo='Resumo do novo artigo.'
        )
        artigo.autores.add(self.autor1)
        self.assertEqual(artigo.nome_artigo, 'Novo Artigo')
        self.assertEqual(artigo.doi, 'http://doi.org/654321')
        self.assertEqual(artigo.resumo, 'Resumo do novo artigo.')
        self.assertIn(self.autor1, artigo.autores.all())

    def test_read_artigo(self):
        artigo = Artigo.objects.get(id=self.artigo.id)
        self.assertEqual(artigo.nome_artigo, 'Nome do Artigo')
        self.assertEqual(artigo.doi, 'http://doi.org/123456')
        self.assertEqual(artigo.resumo, 'Resumo do artigo.')
        self.assertIn(self.autor1, artigo.autores.all())
        self.assertIn(self.autor2, artigo.autores.all())

    def test_update_artigo(self):
        self.artigo.nome_artigo = 'Artigo Atualizado'
        self.artigo.save()
        artigo = Artigo.objects.get(id=self.artigo.id)
        self.assertEqual(artigo.nome_artigo, 'Artigo Atualizado')

    def test_delete_artigo(self):
        artigo_id = self.artigo.id
        self.artigo.delete()
        with self.assertRaises(Artigo.DoesNotExist):
            Artigo.objects.get(id=artigo_id)

    def test_artigo_str(self):
        self.assertEqual(str(self.artigo), 'Nome do Artigo')
