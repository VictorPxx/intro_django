from aluraflix.models import Programa
from django.test import TestCase

class TestModelTesteCase(TestCase):
    
    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém em látim',
            data_lancamento = '2003-07-04'
        )
        
    def test_verifica_atributos_do_programa(self):
        '''Teste que verifica os atributos de um programa com valores default'''
        self.assertEqual(self.programa.titulo, 'Procurando ninguém em látim')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '2003-07-04')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0 )