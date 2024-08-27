from django.db import models
import string
import random

def generate_short_url():
    length = 6
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, default=generate_short_url)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = generate_short_url()
            while URL.objects.filter(short_url=self.short_url).exists():
                self.short_url = generate_short_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"
