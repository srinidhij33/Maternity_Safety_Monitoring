import yagmail
user = 'diabetesprognosis1@gmail.com'
app_password = 'wemgztxdbtijmhhh' # a token for gmail
to = 'akbarpasha0696@gmail.com'
subject = 'Heart Disease Prediction'
content = 'hello'
with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, content)
    print('Sent email successfully')