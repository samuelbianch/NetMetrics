from rest_framework import serializers
from aplicacao.models import Autor, Artigo, Rede

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class ArtigoSerializer(serializers.ModelSerializer):
    # autores = serializers.SerializerMethodField()
    class Meta:
        model = Artigo
        fields = ['id', 'nome_artigo', 'doi', 'resumo', 'autores']


class RedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rede
        fields = '__all__'

