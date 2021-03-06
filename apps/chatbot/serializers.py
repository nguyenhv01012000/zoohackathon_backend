from rest_framework import serializers
from rest_framework.exceptions import APIException
from .models import Chat, Contact
from .utils import get_user_contact

class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants')
        read_only = ('id')
    
    def create(self, validated_data):
        participants = validated_data.pop('participants')
        #create Chat()
        chat = Chat()
        chat.save()    
        for username in participants:        
            contact = get_user_contact(username)
            chat.participants.add(contact)
        chat.save()
        
        return chat