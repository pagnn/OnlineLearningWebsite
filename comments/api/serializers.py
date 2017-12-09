from django.contrib.staticfiles.templatetags.staticfiles import static
from rest_framework import serializers
from comments.models import Comment
from django.contrib.auth import get_user_model
User=get_user_model()
class UserPublicSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=[
			'username',
			'first_name',
			'last_name',
		]

class CommentSerializer(serializers.ModelSerializer):
	user=UserPublicSerializer(read_only=True)
	image=serializers.SerializerMethodField(read_only=True)
	class Meta:
		model=Comment
		fields=['id','user','url','content','timestamp','updated','image']

	def get_image(self,obj):
		image=static("img/user.png")
		return image
class CommentUpdateSerializer(serializers.ModelSerializer):
	user=UserPublicSerializer(read_only=True)
	image=serializers.SerializerMethodField(read_only=True)
	class Meta:
		model=Comment
		fields=['id','user','url','content','timestamp','updated','image']
		read_only_fields=['url']

	def get_image(self,obj):
		image=static("img/user.png")
		return image