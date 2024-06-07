from django.test import TestCase
from aplicacao.models import Rede
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
import pytz

class RedeModelTest(TestCase):

    def setUp(self):
        self.timezone = pytz.UTC
        self.file = SimpleUploadedFile("arquivo.txt", b"conteudo do arquivo")
        self.rede = Rede.objects.create(
            arquivo=self.file
        )

    def test_create_rede(self):
        file = SimpleUploadedFile("novo_arquivo.txt", b"novo conteudo do arquivo")
        rede = Rede.objects.create(arquivo=file)
        self.assertTrue(isinstance(rede, Rede))
        expected_path = 'redes/{:%Y/%m/%d}/novo_arquivo.txt'.format(rede.criado_em)
        self.assertTrue(rede.arquivo.name.startswith(expected_path.rsplit('/', 1)[0]))
        self.assertTrue(rede.criado_em)

    def test_read_rede(self):
        rede = Rede.objects.get(id=self.rede.id)
        self.assertEqual(rede, self.rede)
        expected_path = 'redes/{:%Y/%m/%d}/arquivo.txt'.format(rede.criado_em)
        self.assertTrue(rede.arquivo.name.startswith(expected_path.rsplit('/', 1)[0]))

    def test_update_rede(self):
        new_file = SimpleUploadedFile("arquivo_atualizado.txt", b"conteudo atualizado do arquivo")
        self.rede.arquivo = new_file
        self.rede.save()
        rede = Rede.objects.get(id=self.rede.id)
        expected_path = 'redes/{:%Y/%m/%d}/arquivo.txt'.format(rede.criado_em)
        self.assertTrue(rede.arquivo.name.startswith(expected_path.rsplit('/', 1)[0]))

    def test_delete_rede(self):
        rede_id = self.rede.id
        self.rede.delete()
        with self.assertRaises(Rede.DoesNotExist):
            Rede.objects.get(id=rede_id)

    def test_rede_str(self):
        self.assertEqual(str(self.rede), self.rede.criado_em.strftime('%Y-%m-%d %H:%M:%S'))
