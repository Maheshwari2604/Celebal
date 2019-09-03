import graphene

from graphene_django.types import DjangoObjectType

from app1.models import profile , subprofile

class profiletype(DjangoObjectType):
    class Meta:
        model = profile


class subprofiletype(DjangoObjectType):
    class Meta:
        model = subprofile


class Query(object):
    all_categories = graphene.List(profiletype)
    all_ingredients = graphene.List(subprofiletype)
    category = graphene.Field(profiletype, id=graphene.Int(), name=graphene.String())
    ingredients = graphene.Field(subprofiletype, id=graphene.Int() , name=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        return profile.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return subprofile.objects.select_related('profile').all()

    def resolve_category(self, info , **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        
        if id is not None:
            return profile.objects.get(pk=id)

        if name is not None:
            return profile.objects.get(name=name)

        return None
    
    def resolve_ingredients(self, info , **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        
        if id is not None:
            return subprofile.objects.get(pk=id)
        
        if name is not None:
            return subprofile.objects.get(name = name)

        return None
