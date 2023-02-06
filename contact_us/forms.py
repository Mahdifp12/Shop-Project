from django import forms

from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            'full_name',
            'email',
            'title',
            'message'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام شما"}),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "ایمیل شما"}),
            'title': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "عنوان پیفام شما"
            }),
            'message': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "پیغام شما",
                "rows": "10",
                "cols": "60",
                "id": "message"})
        }

        labels = {
            'full_name': "نام شما",
            'email': "ایمیل شما",
            'title': "عنوان پیغام شما",
            'message': "پیغام شما",

        }
        error_messages = {
            'full_name': {
                'required': 'لطفا نام خود را وارد کنید',
                'max_length': 'تعداد حروف نام شما بیشتر از حد مجاز است'
            },
            'email': {
                'required': 'لطفا ایمیل خود را وارد کنید',
            },
            'title': {
                'required': 'لطفا عنوان پیغام خود را وارد کنید',
                'max_length': 'تعداد حروف عنوان پیغام شما بیشتر از حد مجاز است'
            },
            'message': {
                'required': 'لطفا پیغام خود را وارد کنید',
            }
        }
