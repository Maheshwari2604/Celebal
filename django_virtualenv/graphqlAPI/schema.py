import graphene

import graphqlAPI.app1.schema


class Query(graphqlAPI.app1.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
