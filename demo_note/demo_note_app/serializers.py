from rest_framework import serializers
from rest_framework import Note

class NoteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'