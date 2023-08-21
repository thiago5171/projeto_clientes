from rest_framework import serializers
from clientes.models import Cliente
from .validators import cpf_valido, nome_valido, rg_validate, celular_valido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF é inválido'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'Não inclua números neste campo'})
        if not rg_validate(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve conter 9 digitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O celular deve seguir o padrão 99 99999-9999'})
        return data
    