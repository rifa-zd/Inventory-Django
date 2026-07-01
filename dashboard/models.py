from django.db import models
from django.utils import timezone


class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/%Y/%m/')
    file_type = models.CharField(max_length=10, blank=True)
    size = models.PositiveIntegerField(default=0)
    uploaded_by = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_new = self._state.adding  # True only on first save (creation)

        if self.file:
            if not self.file_type:
                self.file_type = self.file.name.split('.')[-1].upper()
            if not self.size:
                self.size = self.file.size

        super().save(*args, **kwargs)

        if is_new:
            DocumentLog.objects.create(document_name=self.name, 
                                       file_type=self.file_type,
                size=self.size,
                uploaded_by=self.uploaded_by,
                action=DocumentLog.ADDED)

    def delete(self, *args, **kwargs):
        DocumentLog.objects.create(
            document_name=self.name,
            file_type=self.file_type,
            size=self.size,
            uploaded_by=self.uploaded_by,
            action=DocumentLog.REMOVED,
        )
        super().delete(*args, **kwargs)

    @property
    def size_display(self):
        size = self.size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.0f}{unit}" if unit == 'B' else f"{size:.1f}{unit}"
            size /= 1024
        return f"{size:.1f}TB"


class DocumentLog(models.Model):
    """Permanent record of add/remove events, used to power dashboard counts."""

    ADDED = 'added'
    REMOVED = 'removed'
    ACTION_CHOICES = [(ADDED, 'Added'), (REMOVED, 'Removed')]

    document_name = models.CharField(max_length=255)  # kept even after the Document is deleted
    file_type = models.CharField(max_length=10, blank=True)
    size = models.PositiveIntegerField(default=0)
    uploaded_by = models.CharField(max_length=100, blank=True)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.document_name} — {self.action}"
    
    @property
    def size_display(self):
        size = self.size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.0f}{unit}" if unit == 'B' else f"{size:.1f}{unit}"
            size /= 1024
        return f"{size:.1f}TB"