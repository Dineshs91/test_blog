import datetime
from haystack import indexes
from models import UserPosts

class UserPostsIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Creating index for UserPosts model.
    """
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='username')
    post_title = indexes.CharField(model_attr='post_title')
    put_date = indexes.DateTimeField(model_attr='created_timestamp')
    
    def get_model(self):
        return UserPosts
        
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
        