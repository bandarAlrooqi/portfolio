from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    project_photo = models.ImageField(upload_to='media/')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
