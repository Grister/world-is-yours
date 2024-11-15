from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from user.tasks import send_email_verification
from user.models import Address

UserModel = get_user_model()


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateTimeField(format='%Y-%m-%d', required=False)
    address = AddressSerializer(required=False)

    class Meta:
        model = UserModel
        fields = ["id", "first_name", "last_name", "email", "phone", "address", "date_of_birth", "image"]

    def validate_email(self, value):
        instance = self.instance
        if instance and instance.email != value and UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    address = AddressSerializer(required=False)
    date_of_birth = serializers.DateTimeField(format='%Y-%m-%d', required=False)

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email", "phone", "date_of_birth", "address", "image", "password"]

    def validate(self, data):
        email = data["email"]
        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email is already registered.")
        if data['password']:
            validate_password(data['password'])
        return data

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        user_data = UserModel.objects.create_user(**validated_data)

        if address_data:
            address = Address.objects.create(**address_data)
            user_data.address = address
            user_data.save()

        return user_data

    def save(self, **kwargs):
        user = super(UserCreateSerializer, self).save(**kwargs)
        send_email_verification.delay(user_id=user.id)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    image = serializers.ImageField()
    address = AddressSerializer()
    date_of_birth = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = UserModel
        fields = ["id", "first_name", "last_name", "email", "phone", "address", "date_of_birth", "image", "password"]

    def validate_email(self, value):
        instance = self.instance
        if instance and instance.email != value and UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate(self, data):
        if 'password' in data:
            validate_password(data['password'])
        return data

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            if instance.address:
                Address.objects.filter(id=instance.address.id).update(**address_data)
            else:
                instance.address = Address.objects.create(**address_data)

        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class PasswordChangeRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, data):
        email = data["email"]
        if not UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Please, enter your email address that you use to authorization to our site.")
        return data


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    code = serializers.UUIDField(required=True)

    class Meta:
        model = UserModel

    def validate(self, data):
        email = data["email"]
        if not UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Please, enter your email address that you use to authorization to our site.")
        return data


class ContactFormSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()
    subject = serializers.CharField()
    fullname = serializers.CharField()
