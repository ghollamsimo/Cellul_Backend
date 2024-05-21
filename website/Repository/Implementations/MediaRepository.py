import uuid
from abc import ABC
import os

import website
from website.Models.MediaModel import Media
from website.Repository.Interfaces.MediaInterface import MediaInterface
from django.conf import settings


class MediaRepository(MediaInterface, ABC):
    def store(self, file, event):
        base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        storage_directory = os.path.join(base_directory, 'website', 'Storage')

        if not os.path.exists(storage_directory):
            os.makedirs(storage_directory)

        unique_name = f"{uuid.uuid4()}_{file.name}"
        file_path = os.path.join(storage_directory, unique_name)

        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        media_instance = Media(file_path=file_path, event=event)
        media_instance.save()

        return file_path
