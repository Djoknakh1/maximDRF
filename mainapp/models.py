from django.db import models


class Metro(models.Model):
    station_name = models.CharField(max_length=255)
    line_name = models.CharField(max_length=255)
    station_id = models.CharField(max_length=255)
    line_id = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=255)
    raw = models.CharField(max_length=255)
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE)


class Currency(models.Model):
    name = models.CharField(max_length=5)


class Salary(models.Model):
    from_1 = models.IntegerField()
    to = models.IntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    gross = models.BooleanField()


class Employer(models.Model):
    name = models.CharField(max_length=255)
    accredited_it_employer = models.BooleanField()
    trusted = models.BooleanField()


class Snippet(models.Model):
    requirement = models.CharField(max_length=255)
    responsibility = models.CharField(max_length=255)


class Schedule(models.Model):
    name = models.CharField(max_length=255)
    id = models.CharField(primary_key=True, unique=True, max_length=255)


class Professions(models.Model):
    name = models.CharField(max_length=255)


class Experience(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=255)
    name = models.CharField(max_length=255)


class Employment(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=255)
    name = models.CharField(max_length=255)


class Area(models.Model):
    name = models.CharField(max_length=255)


class Type(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=255)
    name = models.CharField(max_length=255)


class Vacancy(models.Model):
    premium = models.BooleanField()
    name = models.CharField(max_length=255)
    department = models.CharField(null=True, max_length=255)
    has_test = models.BooleanField()
    response_letter_required = models.BooleanField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary,null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    response_url = models.CharField(max_length=255)
    sort_point_distance = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField()
    show_logo_in_search = models.BooleanField()
    insider_interview = models.BooleanField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    professional_roles = models.ManyToManyField(Professions)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)