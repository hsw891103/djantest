from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password, make_password

class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required':'아이디를 입력해주세요.'}, max_length=64, label="사용자 이름")
    password = forms.CharField(error_messages={'required':'비밀번호를 입력해주세요.'},widget=forms.PasswordInput, label="비밀번호")
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password :
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else :
                self.user_id = fcuser.id
                
                
class RegisterForm(forms.Form):
    username = forms.CharField(error_messages={'required':'아이디를 입력해주세요.'}, max_length=64, label="사용자 이름")
    useremail = forms.EmailField(error_messages={'requeired' : '이메일을 입력해주세요.'}, widget=forms.EmailInput, label="사용자 이메일")
    password = forms.CharField(error_messages={'required':'비밀번호를 입력해주세요.'},widget=forms.PasswordInput, label="비밀번호")
    re_password = forms.CharField(error_messages={'required':'비밀번호를 확인해주세요.'},widget=forms.PasswordInput, label="비밀번호확인")
    
    def clean(self):
        print('ResigetrForm 시작')
        cleand_data = super().clean()
        username = cleand_data.get('username')
        useremail = cleand_data.get('useremail')
        password = cleand_data.get('password')
        re_password = cleand_data.get('re_password')
        
        if username and useremail and password and re_password :
            # print('ResigetrForm에 모든 정보가 들어있음. 중복검사 시작 - ')            
            if Fcuser.objects.filter(username=username).exists():
                # print(user,'의 타입 : ', type(user))
                # if str(user) == username :
                #     print( '뿅, 맞았습니다.')
                # print(username,'의 타입 : ', type(username))
                # username은 str, user는 class라 타입이 달라 계속 중복검사가 안됐음.
                # print(username, '--ID중복!')
                self.add_error('username', '아이디가 중복됩니다.')
            else :    
                if password == re_password :
                    fcuser = Fcuser(username=username, useremail=useremail, password=make_password(password))
                    fcuser.save()
                    # print('form.py의 RegisterForm에서 ',username, ' 회원가입완료!')
                else:
                    self.add_error('password', '비밀번호가 일치하지 않습니다.')
                                  
            
                    
    