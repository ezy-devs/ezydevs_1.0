from .models import *
from django import forms

class TestimoniesForm(forms.ModelForm):
    class Meta:
        model = Testimonies
        fields = ['name', 'designation', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'mt-2 p-4 border-2 border-gray-300 rounded-lg w-full focus:outline-none focus:ring-2 focus:ring-brand', 'rows': 4, 'placeholder': 'Share your experience'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file p-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand'}),
        }
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            MAX_SIZE = 5 * 1024 * 1024  # 5MB in bytes
            if image.size > MAX_SIZE:
                raise forms.ValidationError("Image size cannot be larger than 5MB.")
        return image
class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'description', 'icon']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'mt-2 p-4 border-2 border-gray-300 rounded-lg w-full focus:outline-none focus:ring-2 focus:ring-brand', 'rows': 4, 'placeholder': 'Describe the service'}),
            'icon': forms.TextInput(attrs={'class': 'mt-2 p-4 border-2 border-gray-300 rounded-lg w-full focus:outline-none focus:ring-2 focus:ring-brand', 'placeholder': 'FontAwesome icon class'}),
        }

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'image', 'link']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'mt-2 p-4 border-2 border-gray-300 rounded-lg w-full focus:outline-none focus:ring-2 focus:ring-brand', 'rows': 4, 'placeholder': 'Describe the project'}),
            'link': forms.URLInput(attrs={'class': 'mt-2 p-4 border-2 border-gray-300 rounded-lg w-full focus:outline-none focus:ring-2 focus:ring-brand', 'placeholder': 'Project link'}),
        }
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            MAX_SIZE = 5 * 1024 * 1024  # 5MB in bytes
            if image.size > MAX_SIZE:
                raise forms.ValidationError("Image size cannot be larger than 5MB.")
        return image

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'designation', 'image', 'bio', 'social_links']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'mt-2 p-4 border-2 border-gray-300 rounded-lg w-full focus:outline-none focus:ring-2 focus:ring-brand', 'rows': 4, 'placeholder': 'Describe the team member'}),
            'social_links': forms.TextInput(attrs={'class': 'mt-2 p-4 border-2 border-gray-300 rounded-lg w-full focus:outline-none focus:ring-2 focus:ring-brand', 'placeholder': 'JSON format for social links'}),
        }
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            MAX_SIZE = 5 * 1024 * 1024  # 5MB in bytes
            if image.size > MAX_SIZE:
                raise forms.ValidationError("Image size cannot be larger than 5MB.")
        return image