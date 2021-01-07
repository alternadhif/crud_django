from django import forms  
from karyawan.models import Karyawan  
class FormKaryawan(forms.ModelForm):  
    class Meta:  
        model = Karyawan  
        fields = "__all__"  