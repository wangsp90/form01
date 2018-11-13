#encoding utf-8
from django import forms

class message(forms.Form):
	title=forms.CharField(max_length=255,min_length=4,label='标题')
	content=forms.CharField(widget=forms.Textarea,label='内容')
	email=forms.EmailField(required=True,label='邮箱')
	reply=forms.BooleanField(required=False,label='回复')

		