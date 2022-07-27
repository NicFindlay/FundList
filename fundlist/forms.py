from crispy_forms.helper import FormHelper
from allauth.account.forms import (
    LoginForm,
    SignupForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    ChangePasswordForm,
    SetPasswordForm,
)
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields["login"].widget = forms.TextInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Username",
                "id": "username",
            }
        )
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Password",
                "id": "password",
            }
        )


class UserSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Email",
                "id": "email",
            }
        )
        self.fields["username"].widget = forms.TextInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Username",
                "id": "username1",
            }
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Password",
                "id": "password1",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Password Again",
                "id": "password2",
            }
        )


class UserResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields["email"].label = "Email"

        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Email address",
                "id": "email1",
            }
        )


class UserResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(UserResetPasswordKeyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields["password1"].label = "New Password"
        self.fields["password2"].label = "Confirm New Password"

        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "new password",
                "id": "password3",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "confirm new password",
                "id": "password4",
            }
        )


class UserChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserChangePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields["oldpassword"].label = "Old Password"
        self.fields["password1"].label = "New Password"
        self.fields["password2"].label = "Confirm New Password"

        self.fields["oldpassword"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Old Password",
                "id": "password5",
            }
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "New Password",
                "id": "password6",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Confirm New Password",
                "id": "password7",
            }
        )


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields["password1"].label = "New Password"
        self.fields["password2"].label = "Confirm New Password"

        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "New Password",
                "id": "password8",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-floating form-floating-custom mb-3",
                "placeholder": "Confirm New Password",
                "id": "password9",
            }
        )
