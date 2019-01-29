from django_elasticsearch_dsl import DocType, Index
from categories.models import Listing

listings =  Index('listings')

@listings.doc_type
class ListingDocument(DocType):
    class Meta:
        model = Listing

    fields = [
        'title',
        'short_description',
    ]

