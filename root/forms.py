from django import forms

# yeni bildiri oluşturmak için
class ArizaKaydiOlustur(forms.Form):
    name = forms.CharField(label="Ariza Adi", max_length=50)
    check = forms.BooleanField(required=False)
