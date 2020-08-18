from django.db import models


class TimeStampedModel(models.Model):
    """ Define Time Stamped Model Class """

    created = models.DateTimeField(auto_now_add=True)  # 모델이 생성된 날짜, 시간
    updated = models.DateTimeField(auto_now=True)  # 새로운 날짜로 업데이트

    class Meta:

        abstract = True  # 추상 모델 -> 확장만 가능
