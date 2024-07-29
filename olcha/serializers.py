from rest_framework import serializers
from .models import Category,Group,Image,Product,Comment,ProductAttribute
from django.db.models.functions import Round
from django.db.models import Avg
from django.contrib.auth.models import User
#For Image
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'is_primary','product','group','category']
        
#For Group
class GroupModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id','slug',   'group_name', 'image']

    def get_image(self, instance):
        image = Image.objects.filter(group=instance, is_primary=True).first()
        request = self.context.get('request')
        if image:
            image_url = image.image.url
            return request.build_absolute_uri(image_url)
        return None

#For Category
class CategoryModelSerializer(serializers.ModelSerializer):
    
    # images = ImageSerializer(many=True, read_only=True,source='category_images')
    category_image = serializers.SerializerMethodField(method_name='get_images')
    groups = GroupModelSerializer(many=True,read_only = True)
    
    def get_images(self, instance):
        image = Image.objects.filter(category=instance, is_primary=True).first()
        request = self.context.get('request')
        if image:
            image_url = image.image.url
            return request.build_absolute_uri(image_url)     
        return None

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'slug', 'category_image','groups']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ()
    
#For Product        
class ProductSerializer(serializers.ModelSerializer):
    # group = GroupModelSerializer(many=False)
    # group_name = serializers.CharField(source = 'group.group_name')
    category_name = serializers.CharField(source = 'group.category.category_name', read_only = True)
    category_slug  = serializers.SlugField(source = 'group.category.slug',read_only =True)  
    primary_images = serializers.SerializerMethodField()
    all_images = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    #comments = CommentSerializer(many=True,read_only = True)
    comments_count = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    
    def get_attributes(self,instance):
        attributes = ProductAttribute.objects.filter(product = instance).values_list('key_id','key__attribute_name',
                                                                                     'value_id','value__attribute_value')
        characters = [
            {
            'attribute_id':key_id,
            'attribute_name':key_name,
            'attribute_value_id':value_id,
            'attribute_value':value_name
            }
            for key_id,key_name,value_id,value_name in attributes
        ]
        return characters
    # simple version to take avarage rating
    """ def get_avg_rating(self,instance):
        comments = Comment.objects.filter(product = instance)
        try:
            avg_rating = round(sum([comment.rating for comment in comments]) / comments.count())
        except ZeroDivisionError:
            avg_rating = 0
        return avg_rating  """ 
        
    #django annotate and aggregate version to take avarage rating 
    def get_avg_rating(self,instance):
        avg_rating = Comment.objects.filter(product=instance).aggregate(avg_rating=Round(Avg('rating')))
        if avg_rating.get('avg_rating'):
            return avg_rating.get('avg_rating')
        return 0
    
    def get_comments_count(self,instance):
        count = Comment.objects.filter().count()
        return count 
    
    
    def get_is_liked(self,instance):
        user = self.context.get('request').user
        if not user.is_authenticated:
            return False
        all_likes = instance.users_like.all()
        if user in all_likes:
            return True
        return False
        
        
    
    def get_all_images(self,instance):
        images = Image.objects.all().filter(product=instance)
        all_images = []
        request = self.context.get('request')
        for image in images:
            all_images.append(request.build_absolute_uri(image.image.url))
        return all_images
        
    
    def get_primary_images(self,instance):
        image = Image.objects.filter(product=instance, is_primary = True).first()
        request = self.context.get('request')
        if image:
            image_url = image.image.url
            return request.build_absolute_uri(image_url)
     
    class Meta:
        model = Product
        exclude = ('users_like',)
        extra_fields = ['group','category_name','category_slug','primary_images','all_images','is_liked']


#Token Authentication orqali Login, Register , Logout

class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    username = serializers.CharField(read_only = True)
    password = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['id','username','password']





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'<write only true>': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
       username = serializers.CharField(required=True)
       password = serializers.CharField(required=True)
       

class LogoutSerializer(serializers.Serializer):
    pass
  


        
    
      
    
