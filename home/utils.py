from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

def send_verification_email(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    verification_url = request.build_absolute_uri(f'/verify/{uid}/{token}/')

    send_mail(
        'Verifica tu cuenta',
        f'Haz clic en el siguiente enlace para verificar tu cuenta:\n\n{verification_url}',
        'noreply@oceanworld.com',
        [user.email],
        fail_silently=False,
    )

    return verification_url