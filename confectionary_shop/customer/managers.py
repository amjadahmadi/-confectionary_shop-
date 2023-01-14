from django.db import models
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):
    class STATUS:
        PENDING = 1
        APPROVED = 2
        REJECTED = 3

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id,
                                                status=self.STATUS.APPROVED)
        return qs

    def filter_by_instance_all_comments(self,instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs

    def all_comments(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def approved(self):
        return self.filter(status=self.STATUS.APPROVED)

    def rejected(self):
        return self.filter(status=self.STATUS.REJECTED)

    def replies(self):
        qs = super(CommentManager, self).filter(parent__isnull=False)
        return qs
