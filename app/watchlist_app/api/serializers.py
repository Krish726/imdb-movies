from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


# Model Serializer

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        #fields = "__all__"
        
  
class WatchListSerializer(serializers.ModelSerializer):
    
    '''nested serializer '''
    reviews = ReviewSerializer(many=True,read_only = True)
    playform = serializers.CharField(source='platform.name')
    ''' custom serializers method filed len_name get_field_name'''
    len_name = serializers.SerializerMethodField()

    def get_len_name(self,object):
        return len(object.title)
    
    class Meta:
        model = WatchList
        fields = "__all__"
        #fields = ['id', 'name', 'description']
        #exclude = ['active']
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    # for entire json of the movie list but it String related field only string thatis defined in model
    watchlist = WatchListSerializer(many=True,read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    #watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie-detail')
    class Meta :
        model = StreamPlatform
        fields = "__all__"

'''  
# Validaions are switched off for IMDB clone project
      
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must not less than 2 characters")
        else:
            return value
        
    def validate(self, data):
        if(data['name']==data['description']):
            raise serializers.ValidationError("Name and description should not be same")        
        else:
            return data
'''
"""
def name_length(value):
    if len(value) > 5:
        raise serializers.ValidationError("Name must be less than 5 characters")
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
    
    # field lavel validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must not less than 2 characters")
        else:
            return value
    # Object lavel validation    
    def validate(self, data):
        if(data['name']==data['description']):
            raise serializers.ValidationError("Name and description should not be same")        
        else:
            return data
            
"""