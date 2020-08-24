from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):  # AbstractUser -> 장고의 기본 유저 모델
    """custom user model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    # 상수 설정

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),  # (DATABASE로 보내지는 값, ADMIN FORM에서 보여지는 값)
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    # 선택지 (튜플)

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(upload_to="avatar",blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
    # null = True -> 비어있는거 허락 한다
    # default = "" -> string 값을 기본값으로 할당
    # blank = True -> db 생성시 꼭 값을 안넣어도 되게 함
