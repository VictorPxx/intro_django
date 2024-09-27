from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer
from django.test import TestCase

class TestSerializersTestCase(TestCase):
    
    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém em látim',
            data_lancamento = '2003-07-04',
            tipo = 'F',
            likes = 2400,
            dislikes = 50
        )
        
        self.serializer = ProgramaSerializer(instance=self.programa)
        
    def test_verifica_campos_serializados(self):
        '''Teste que verifica campos que estão sendo serializados'''
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))
        
    def test_verifica_os_coteúdos_dos_campos_serializados(self):
        '''Teste que verifica os conteúdos dos campos serializados'''
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)
        