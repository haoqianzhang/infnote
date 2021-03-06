from djongo import models
from django.utils import timezone

from users.models import User
from categories.models import Category


class PostManager(models.Manager):
    def create(self, user: User, **kwargs):
        if not isinstance(user, User):
            raise ValueError('User instance error.')

        post = self.model(
            public_address=user.public_address,
            **kwargs
        )

        category = Category.objects.get(name=post.category)
        if not category:
            raise ValueError('Category "' + post.category + '" is not allowed.')
        category.posts += 1

        reply_to = kwargs.get('reply_to')
        if reply_to and len(reply_to) > 0:
            master = self.get(transaction_id=reply_to)
            master.replies += 1
            master.last_reply = post.transaction_id
            user.replies += 1
            post.category = master.category

            post.save()
            master.save()
            user.save()
            category.save()
        else:
            user.topics += 1
            category.topics += 1

            post.save()
            user.save()
            category.save()

        return self.get(transaction_id=post.transaction_id)


class Post(models.Model):
    id = models.ObjectIdField(db_column='_id', default=None)
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=20000)

    # 使用 URI-liked 的形式，暂时仅允许第一级目录
    # TODO: 给 Post 的 category 字段添加 validator
    category = models.CharField(max_length=255)

    date_submitted = models.DateTimeField(default=timezone.now)
    date_confirmed = models.DateTimeField(null=True, default=None)
    transaction_id = models.CharField(max_length=128, unique=True)
    is_confirmed = models.BooleanField(default=False)
    block_height = models.IntegerField(default=0)

    # 对应另一个 Post 的 transaction_id
    # TODO: 暂时限制仅能回复 reply_to 字段为空的 post
    reply_to = models.CharField(max_length=128, null=True, db_index=True)
    replies = models.IntegerField(default=0)
    last_reply = models.CharField(max_length=128, null=True)

    # TODO: 用于编辑，对应原始 post 的 transaction_id
    base_to = models.CharField(max_length=128, null=True)

    # 发送者的 public address
    public_address = models.CharField(max_length=128)

    # TODO: 可能需要限制为 UV 而不是 PV
    views = models.BigIntegerField(default=0)

    # TODO: 需要新的接口，对登录用户可用
    likes = models.BigIntegerField(default=0)

    objects = PostManager()

    class Meta:
        db_table = 'infnote_posts'
