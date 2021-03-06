from django.db import models

# Create your models here.

class UserGroup(models.Model):
    """
        用户组
    """
    title = models.CharField(max_length=32,verbose_name="分组名")

    def __str__(self):
        return self.title

class Role(models.Model):
    """
    角色
    """
    name = models.CharField(max_length=32,verbose_name="角色")

    def __str__(self):
        return self.name


class Users(models.Model):
    """
    个人信息
    """
    name = models.CharField(max_length=32,verbose_name="用户名")
    email = models.EmailField(max_length=32,verbose_name="邮箱")
    age = models.IntegerField(verbose_name="年龄")

    ug = models.ForeignKey(to=UserGroup,null=True,blank=True,verbose_name="用户组")
    rm = models.ManyToManyField(to=Role,verbose_name="角色")

    def text_username(self):
        return self.name

    def value_username(self):
        return self.name

    def text_email(self):
        return self.email

    def value_email(self):
        return self.email

    def text_age(self):
        return self.age

    def value_age(self):
        return self.age

    def __str__(self):
        return self.name
