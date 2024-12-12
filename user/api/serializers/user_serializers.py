from rest_framework import serializers
from user.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups','user_permissions', 'last_login')
        extra_kwarrgs={
            'password':{'write_only': True}
        }
    def create(self, validated_data):
        """
        Create a new user with a hashed password.
        """
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            name = validated_data['name'],
            last_name = validated_data['last_name'],
            phone = validated_data['phone']

        )
        return user
    

    def update(self, instance, validated_data):
        """
        Update an existing user and hash the password if provided.
        """
        
        password = validated_data.pop('password',None)
        for attr, value in validated_data.items():
            setattr(instance,attr,value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance