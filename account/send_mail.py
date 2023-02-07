from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f"http://localhost:8000/api/v1/accounts/activate/{code}/"
    full_link_server = f"http://35.246.223.100/api/v1/accounts/activate/{code}/"
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: \n{full_link}\n{full_link_server}',
        'doolat.daiyrkulov@gmail.com',
        [user],
        fail_silently=False
    )

def send_reset_email(user):
    code = user.activation_code
    email = user.email
    send_mail('Letter with password reset code!', f"Your reset code {code}", 'odecik30@gmail.com', [email, ],
              fail_silently=False)


def send_notification(user_email, order_id, price):
    send_mail(
        'Уведомление о создании заказа!',
        f"""Вы создали заказ №{order_id}, \n полная стоимость вашего заказа: {price}. \nспасибо за то что выбрали нас!""",
        'from@example.com',
        [user_email],
        fail_silently=False
    )
