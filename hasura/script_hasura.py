a = "A"
b = "table1"
c = "CharField"

#   CharField = Text / varchar
#   IntegerField = Integer / Numeric
#   BooleanField = Boolean
#   DateTimeField(auto_now_add=True) = Timestamp
#   TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True) = Time
#   DateField(_(u"Conversation Date"), blank=True) = Date
#   UUIDField = UUID
#   jsonfield.JSONField() = JSONB



f = open("model.py" , "a")
f.write("Class " + a + ": \n\t" + b + " : models."+ c + "() \n\t")
f.close()