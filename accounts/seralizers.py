from accounts.models import *
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_extra_fields.fields import Base64ImageField


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserSubSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubSubCategory
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at')


class UserSubCategorySerializer(serializers.ModelSerializer):
    sub_sub_categories = UserSubSubCategorySerializer(many=True, required=False)
    class Meta:
        model = UserSubCategory
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at', 'sub_sub_categories')


class UserCategorySerializer(serializers.ModelSerializer):
    sub_categories = UserSubCategorySerializer(many=True, required=False)
    class Meta:
        model = UserCategory
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at', 'sub_categories')


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'number', 'is_vendor', 'password', 'password2')

        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})

            return attrs

    def create(self, validated_data):
        user = User.objects.create(
            number = validated_data['number'],
            is_vendor = validated_data['is_vendor'],
            # is_store = validated_data['is_store']
            # password = make_password(validate_password['password'])
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id', 'title', 'logo', 'created_at', 'updated_at')


class SocialIconCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialIcon
        fields = ('id', 'url', 'social_media', 'user', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    cover_image = Base64ImageField(required=False)
    logo = Base64ImageField(required=False)
    social_icons = SocialIconCreateSerializer(many=True, required=False)
    
    class Meta:
        model = User
        fields = ('id', 'number', 'name', 'is_vendor',  'email', 'rating', 'address_addtional', 'social_icons', 'cover_image', 'logo', 'city', 'category', 'region', 'avenue', 'street')

    def update(self, instance, validated_data):
        try:
            social_icons = validated_data['social_icons']
            print(social_icons)
            icons = instance.social_icons.all()
            # icons = list(icons)
            # print(social_icons)
            instance.name = validated_data.get('name', instance.name)
            instance.number = validated_data.get('number', instance.number)
            instance.email = validated_data.get('email', instance.email)
            instance.address_addtional = validated_data.get('address_addtional', instance.address_addtional)
            instance.cover_image = validated_data.get('cover_image', instance.cover_image)
            instance.logo = validated_data.get('logo', instance.logo)
            instance.category = validated_data.get('category', instance.category)
            instance.city = validated_data.get('city', instance.city)
            instance.region = validated_data.get('region', instance.region)
            instance.avenue = validated_data.get('avenue', instance.avenue)
            instance.street = validated_data.get('street', instance.street)
            instance.save()

            for icon in range(len(social_icons)):
                if len(icons) == 0:
                    social_icon = SocialIcon(url=social_icons[icon]['url'], social_media=social_icons[icon]['social_media'], user=instance)
                    social_icon.save()
        except:
            instance.name = validated_data.get('name', instance.name)
            # instance.address = validated_data.get('address', instance.address)
            instance.number = validated_data.get('number', instance.number)
            instance.email = validated_data.get('email', instance.email)
            instance.category = validated_data.get('category', instance.category)
            instance.address_addtional = validated_data.get('address_addtional', instance.address_addtional)
            instance.cover_image = validated_data.get('cover_image', instance.cover_image)
            instance.logo = validated_data.get('logo', instance.logo)
            instance.city = validated_data.get('city', instance.city)
            instance.region = validated_data.get('region', instance.region)
            instance.avenue = validated_data.get('avenue', instance.avenue)
            instance.street = validated_data.get('street', instance.street)
            instance.save()
        return instance


class SocialIconSerializer(serializers.ModelSerializer):
    social_media = SocialMediaSerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = SocialIcon
        fields = ('id', 'url', 'social_media', 'user', 'created_at', 'updated_at')


class UserShowSerializer(serializers.ModelSerializer):
    sub_sub_category = UserSubSubCategorySerializer(required=False)
    sub_category = UserSubCategorySerializer(required=False)
    category = UserCategorySerializer(required=False)
    social_icons = SocialIconSerializer(required=False)
    class Meta:
        model = User
        fields = ('id', 'number', 'name', 'is_vendor', 'is_verified', 'email', 'rating', 'address_addtional', 'social_icons', 'cover_image', 'logo', 'category', 'sub_category', 'sub_sub_category')


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'number', 'name', 'is_vendor', 'is_verified_by_admin', 'email', 'address_addtional')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        print(user.username)
        token['username'] = user.username
        token['email'] = user.email
        print(token['username'])
        print("qwe")
        return token


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'title', 'created_at', 'updated_at')


class AvenueSerializer(serializers.ModelSerializer):
    streets = StreetSerializer(many=True, required=False)
    class Meta:
        model = Avenue
        fields = ('id', 'title', 'streets', 'created_at', 'updated_at')


class RegionSerializer(serializers.ModelSerializer):
    avenues = AvenueSerializer(many=True, required=False)
    class Meta:
        model = Region
        fields = ('id', 'title', 'avenues', 'created_at', 'updated_at')


class CitySerializer(serializers.ModelSerializer):
    regions = RegionSerializer(many=True, required=False)
    class Meta:
        model = City
        fields = ('id', 'title', 'regions', 'created_at', 'updated_at')


class ResetPasswordSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=15)
    # code = serializers.CharField(max_length=6)
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

    def validate(self, data):
        user = User.objects.filter(number=data['number'])

        if not user:
            raise serializers.ValidationError("This number not found")
            
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password and confirm password not match")
        return data


class ForgetPasswordSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=15)

    def validate_number(self, value):
        if not User.objects.filter(number=value, is_active=True):
            raise serializers.ValidationError("This number not found")
        return value


class ResetPasswordTwoSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=6)
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

    def validate(self, data):
        user = User.objects.filter(number=data['number'])

        if not user:
            raise serializers.ValidationError("This number not found")
            
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password and confirm password not match")
        return data