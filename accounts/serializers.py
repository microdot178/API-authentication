
from rest_framework import serializers
from accounts.models import MyUser

class UserListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MyUser
        fields = ['user', 'id', 'username', 'email', 'last_login']
