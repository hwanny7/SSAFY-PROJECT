from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field

class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
         data = form.cleaned_data
         nickname = data.get('nickname')
         img_url = data.get('img_url')
         point = data.get('point')
         date_joined = data.get('date_joined')

         if nickname:
             user_field(user, 'nickname', nickname)
         if img_url:
             user_field(user, 'img_url', img_url)
         if point:
             user_field(user, 'point', point)
         if date_joined:
             user_field(user, 'date_joined', date_joined)
        
         return super().save_user(request, user, form, commit=commit)