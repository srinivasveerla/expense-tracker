from rest_framework.viewsets import ModelViewSet
from .serializers import EntrySerializer
from ..models import Entry

class EntryViewSet(ModelViewSet):

    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        custom_param = self.request.query_params.get('sid')
        if custom_param:
            queryset = queryset.filter(sheet_id=custom_param)
        return queryset