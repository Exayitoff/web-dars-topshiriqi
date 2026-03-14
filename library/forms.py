from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Masalan, kitob band qilish'}),
            'message': forms.Textarea(attrs={'placeholder': 'Savolingiz yoki xabaringizni yozing', 'rows': 5}),
        }
        labels = {
            'name': 'Ismingiz',
            'email': 'Email',
            'subject': 'Mavzu',
            'message': 'Xabar',
        }
