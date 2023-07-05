from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest

from ..models import StorageModel

from ..serializers import (
    StorageModelSerializer,
)


# =============================================GET=============================================

def get_storage_core(request: HttpRequest) -> List[StorageModel]:
    storage = StorageModel.objects.all()
    return StorageModelSerializer(storage, many=True)
