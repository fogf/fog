from django.db import models


class Celebrity(models.Model):
    name = models.CharField(max_length=64, verbose_name="姓名")
    en_name = models.CharField(max_length=64, verbose_name="英文名（可选）", defualt="", blank=True)
    sex = models.SmallIntegerField(verbose_name="性别", choices=((0, "男"), (1, "女"), (3, "其他")))
    birthday = models.DateField(verbose_name="出生日期", null=True)
    #other_en_name = models.CharField(max_length=255, verbose_name="更多外文名", null=True)
    birth_area = models.CharField(max_length=128, verbose_name="出生地", defualt="", blank=True)
    profession = models.CharField(max_length=16, verbose_name="职业", defualt="", blank=True)

    class Meta:
        verbose_name = "人物"


class CelebrityPic(models.Model):
    celebrity = models.ForeignKey(Celebrity, verbose_name="人")
    image_url = models.URLField(verbose_name="URL")
    width = models.IntegerField(verbose_name="宽度", default=0)
    height = models.IntegerField(verbose_name="高度", default=0)

    class Meta:
        verbose_name = "人物图片"


class Movie(models.Model):
    title = models.CharField(max_length=1024, verbose_name="电影标题")
    initial_release_date = models.DateField(verbose_name="上映日期", null=True)
    runtime = models.IntegerField(verbose_name="片长(分钟)", null=True)
    directors = models.ManyToManyField(Celebrity, related_name="directors", verbose_name="导演")
    scriptwriters = models.ManyToManyField(Celebrity, related_name="scriptwriters", verbose_name="编剧")
    languages = models.CharField(max_length=255, verbose_name="语言")
    other_title = models.CharField(max_length=255, verbose_name="又名")
    country = models.CharField(max_length=16, verbose_name="制片国家/地区")

    class Meta:
        verbose_name = "电影"


class MoviePic(models.Model):
    celebrity = models.ForeignKey(Movie, verbose_name="电影")
    image_url = models.URLField(verbose_name="URL")
    width = models.IntegerField(verbose_name="宽度", default=0)
    height = models.IntegerField(verbose_name="高度", default=0)

    class Meta:
        verbose_name = "剧照"

class MovieBrief(models.Model):

    movie = models.ForeignKey(Movie)
    intro = models.TextField(verbose_name="简介")

    class Meta:
        verbose_name = "电影简介"

class MovieReview(models.Model):

    movie = models.ForeignKey(Movie, verbose_name="电影")
    publisher = models.ForeignKey('auth.User', verbose_name="用户")
    context = models.TextField(verbose_name="正文")

    class Meta:
        verbose_name = "影评"