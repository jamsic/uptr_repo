from django.db import models


class MenuItem(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    explicit_url = models.CharField(max_length=100, blank=True,
                                    null=True, unique=True)
    named_url = models.CharField(max_length=100, blank=True,
                                 null=True, unique=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)
    root_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
