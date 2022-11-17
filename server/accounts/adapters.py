from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field

class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        data = form.cleaned_data
        user.nickname = data.get('nickname')
        user.image = data.get('image')
        user.save()

        return user