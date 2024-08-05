from django import forms
from .models import User
from .models import User_info

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields =('description','type','selection','date_of_Add')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class Userreponse(forms.ModelForm):
    class Meta:
        model=User
        fields =('status','response','date_de_changement')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Userreponse, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class miseuser(forms.ModelForm):
    class Meta:
        model=User_info
        fields =('name','email','codeaffectation','password','mobile_number')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(miseuser, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'