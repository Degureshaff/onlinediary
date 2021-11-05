from django.db import models

class mgBCOsh(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgFronOsh(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgFullOsh(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgUIOsh(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class mgBCBi(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgFronBi(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgFullBi(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgUIBi(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class mgBCUz(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgFronUz(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgFullUz(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class mgUIUz(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#----------------------------------- 

class evBCOsh(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evFronOsh(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evFullOsh(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evUIOsh(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class evBCBi(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evFronBi(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evFullBi(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evUIBi(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class evBCUz(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evFronUz(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evFullUz(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class evUIUz(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"фамилия")
    mobile  = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    summ1 = models.CharField(max_length=255)
    summ2 = models.CharField(max_length=255)
    summ3 = models.CharField(max_length=255)
    summfull = models.CharField(max_length=255)

    def __str__(self):
        return self.name
