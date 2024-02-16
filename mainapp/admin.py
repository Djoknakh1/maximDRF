from django.contrib import admin


from mainapp.models import Vacancy, Metro, Address, Currency, Salary, Employer, Snippet, Schedule, Professions, \
    Experience, Employment, Area, Type

admin.site.register(Vacancy)
admin.site.register(Metro)
admin.site.register(Address)
admin.site.register(Currency)
admin.site.register(Salary)
admin.site.register(Employer)
admin.site.register(Snippet)
admin.site.register(Schedule)
admin.site.register(Professions)
admin.site.register(Experience)
admin.site.register(Employment)
admin.site.register(Area)
admin.site.register(Type)
