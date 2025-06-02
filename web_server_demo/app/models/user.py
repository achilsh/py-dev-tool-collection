from tortoise.models import Model
from tortoise import fields

## asyncmy 使用，性能更加，  pip install tortoise-orm asyncmy
class UserModel(Model):
    # 自动递增
    id = fields.BigIntField(primary_key=True)
    ## null 说明该字段是否可以 nullable
    name = fields.CharField(max_length=100, null=True) 
    # 自动设置
    created_at=fields.DatetimeField(
        ## 字段名不用自动生成的，按指定名字来
        source_field="create_time",
        auto_now_add=True,
        description="创建时间",
    )
    # 自动更新
    updated_at = fields.DatetimeField(
        auto_now=True,
        description="更新时间"
    )
    score=fields.FloatField(
        default=0.0,
        description="分数"
    )
    active = fields.BooleanField(
        default=True, 
        description="是否激活"
    )
    
    email = fields.CharField(max_length=50, default="hwshtongxin@126.com")
    cardId = fields.CharField(max_length=22, unique=True, db_index=True, description="身份证id")
    address = fields.CharField(max_length=255)
    class Meta:
        ## 指定 表名，而非自动产生的表名
        table = "user_model"
        #  唯一索引
        unique_together = [("name", "email")]
        # 联合索引
        indexes =[("cardId", "address")]
        #指定排序字段
        ordering = ["cardId", "-address"] 
        table_description ="表的描述具体内容"