from django.db import models

# Create your models here.

class Pro_customers (models.Model):

    """
        客户类：
        客户代码、客户名称、联系人员
    """

    cus_code = models.CharField("代码",max_length = 20)
    cus_name = models.CharField("客户名称",max_length = 30)
    cus_memb = models.TextField(verbose_name='联系人员')

    def __str__(self):
        return self.cus_name

class Pro_stages (models.Model):
    
    """
        项目阶段类：
        客户代码、客户名称、联系人员、类型
    """

    Sta_code = models.CharField("代码",max_length = 20)
    Sta_name = models.CharField("阶段名称",max_length = 30)
    sta_choices = (
        ('1','大屏项目'),
        ('2','分析项目'),
    )
    Sta_type = models.CharField('类型',max_length = 50,choices = sta_choices)

    def __str__(self):
        return self.Sta_name

class Pro_members (models.Model):
    
    """
        员工类：
        员工名称、员工角色、是否在职、人天成本
    """

    mem_name = models.CharField("员工名称",max_length = 30)
    role_choice = (
        ('1',u'项目经理'),
        ('2',u'销售'),
        ('3',u'产品经理'),
        ('4',u'UI'),
        ('5',u'UE'),
        ('6',u'总监'),
        ('7',u'前端技术'),
        ('8',u'后端技术')
    )
    Mem_role = models.CharField('角色',max_length = 30,choices = role_choice)
    sta_choice = (
        ('1',u'在职'),
        ('2',u'离职')
    )
    Mem_statu = models.CharField('是否在职',max_length = 10, choices = sta_choice )
    Mem_cost = models.IntegerField(verbose_name = '人天成本')

    def __str__(self):
        return self.mem_name

class Projects (models.Model):
    
    """
        项目类：
        代码、项目名称、客户、所处阶段、项目状态、项目成员
    """

    pro_code = models.CharField("代码",max_length = 20)
    pro_name = models.CharField("项目名称",max_length = 30)
    pro_customer = models.ForeignKey(Pro_customers,verbose_name = '客户')
    pro_stage = models.ForeignKey(Pro_stages,verbose_name = '所处阶段')
    statu_choices = (
        ('1',u'洽谈中'),
        ('2',u'实施中'),
        ('3',u'暂停'),
        ('9',u'失败') 
    )
    pro_statu = models.CharField('项目状态',max_length = 20,choices = statu_choices)
    pro_member = models.ForeignKey(Pro_members,verbose_name = '项目成员')

    def __str__(self):
        return self.pro_name



class Pro_diarys (models.Model):
    
    """
        日报类：
        日期、项目、项目阶段、工作事项、工作产出、问题、备注
    """

    dia_data = models.DateField('日期',auto_now=True)

    #这里必须定义related_name属性。 
    dia_project = models.OneToOneField(Projects,verbose_name = '所属项目')
    #dia_statu = models.ManyToManyField(Projects,related_name= 'pro_stage',to_field='pro_name', verbose_name = '项目阶段')
    dia_statu = models.ForeignKey(Projects,related_name='pro_name', verbose_name = '项目阶段')
    dia_task = models.TextField(verbose_name='工作事项')
    dia_result = models.CharField('工作产出',max_length =100)
    dia_trouble = models.CharField('问题',max_length = 100)
    dia_text = models.TextField(verbose_name='备注')

    def __str__(self):
        return self.dia_data

"""
class Projects (models.Model):
    """
    人员类
    """
    pass

class Projects (models.Model):
    pass
class Projects (models.Model):
    pass

class Projects (models.Model):
    pass

class Projects (models.Model):
    pass

class Projects (models.Model):
    pass
class Projects (models.Model):
    pass

class Projects (models.Model):
    pass
    """
