import graphene
import graphql_jwt
import app1.schema
import users.schema


class Query(app1.schema.Query, users.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(app1.schema.Mutation, users.schema.Mutation , graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()     


schema = graphene.Schema(query=Query , mutation = Mutation)