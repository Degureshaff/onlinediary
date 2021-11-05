from django import forms
from .models import mgBCOsh,mgFronOsh,mgFullOsh,mgUIOsh,mgBCBi,mgFronBi,mgFullBi,mgUIBi,mgBCUz,mgFronUz,mgFullUz,mgUIUz,evBCOsh,evFronOsh,evFullOsh,evUIOsh,evBCBi,evFronBi,evFullBi,evUIBi,evBCUz,evFronUz,evFullUz,evUIUz
 
 

class mgBCOshform(forms.ModelForm):
    class Meta:
        model = mgBCOsh
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgFronOshform(forms.ModelForm):
    class Meta:
        model = mgFronOsh
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgFullOshform(forms.ModelForm):
    class Meta:
        model = mgFullOsh
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgUIOshform(forms.ModelForm):
    class Meta:
        model = mgUIOsh
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgBCBiform(forms.ModelForm):
    class Meta:
        model = mgBCBi
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgFronBiform(forms.ModelForm):
    class Meta:
        model = mgFronBi
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgFullBiform(forms.ModelForm):
    class Meta:
        model = mgFullBi
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgUIBiform(forms.ModelForm):
    class Meta:
        model = mgUIBi
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgBCUzform(forms.ModelForm):
    class Meta:
        model = mgBCUz
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgFronUzform(forms.ModelForm):
    class Meta:
        model = mgFronUz
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgFullUzform(forms.ModelForm):
    class Meta:
        model = mgFullUz
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class mgUIUzform(forms.ModelForm):
    class Meta:
        model = mgUIUz
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

#------------------- 

class evBCOshform(forms.ModelForm):
    class Meta:
        model = evBCOsh
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evFronOshform(forms.ModelForm):
    class Meta:
        model = evFronOsh
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evFullOshform(forms.ModelForm):
    class Meta:
        model = evFullOsh
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evUIOshform(forms.ModelForm):
    class Meta:
        model = evUIOsh
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evBCBiform(forms.ModelForm):
    class Meta:
        model = evBCBi
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evFronBiform(forms.ModelForm):
    class Meta:
        model = evFronBi
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evFullBiform(forms.ModelForm):
    class Meta:
        model = evFullBi
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evUIBiform(forms.ModelForm):
    class Meta:
        model = evUIBi
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evBCUzform(forms.ModelForm):
    class Meta:
        model = evBCUz
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evFronUzform(forms.ModelForm):
    class Meta:
        model = evFronUz
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evFullUzform(forms.ModelForm):
    class Meta:
        model = evFullUz
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]

class evUIUzform(forms.ModelForm):
    class Meta:
        model = evUIUz
        fields = [
            "name",
            "surname",
            "mobile",
            "summ1",
            "summ2",
            "summ3",
            "summfull"]
