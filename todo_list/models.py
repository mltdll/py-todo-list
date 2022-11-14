from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=127, unique=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=127)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "-created_at"]

    def toggle_completed(self) -> None:
        self.is_completed = not self.is_completed
        self.save()

    def __str__(self) -> str:
        return self.content
