from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = "date"

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

        widgets = {
            "Booking_date": DateInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "Name": "Nama",
            "Phone": "Telepon",
            "Email": "Surel",
            "Model": "Model",
        }

        # Tambahkan kelas Bootstrap untuk gaya yang lebih baik
        error_css_class = 'text-danger'
        required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # Tambahkan kelas Bootstrap untuk gaya yang lebih baik
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

        # Anda dapat menyesuaikan gaya lebih lanjut jika diperlukan
        self.fields['Name'].widget.attrs['placeholder'] = 'Masukkan nama Anda'
        self.fields['Phone'].widget.attrs['placeholder'] = 'Masukkan nomor telepon Anda'
        self.fields['Email'].widget.attrs['placeholder'] = 'Masukkan surel Anda'
        self.fields['Model'].widget.attrs['placeholder'] = 'Masukkan model'

        # Tambahkan kelas kustom untuk gaya
        self.fields['Name'].widget.attrs['class'] += ' kelas-kustom'
        self.fields['Phone'].widget.attrs['class'] += ' kelas-kustom'
        self.fields['Email'].widget.attrs['class'] += ' kelas-kustom'
        self.fields['Model'].widget.attrs['class'] += ' kelas-kustom'
