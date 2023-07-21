from django.db import models


class AccountTest(models.Model):
    # USER_ID는 SERIAL로 자동 증가하는 기본 키로 사용됩니다.
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=355, unique=True, null=False)
    rdate = models.DateTimeField(null=False)
    last_login = models.DateTimeField(null=True)  # null=True로 설정하여 NULL 허용

    class Meta:
        db_table = 'account_test'  # 데이터베이스에 저장될 테이블의 이름을 지정
        managed = False  # 이미 존재하는 테이블과 연결하지만 Django가 해당 테이블을 관리하지 않도록 설정

    def __str__(self):
        return self.user_id
