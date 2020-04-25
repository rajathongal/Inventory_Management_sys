from django.db import models
from sales.models import *
# Create your models here.
class Device(models.Model):
    choices = (('Available','item ready to be prushase'),('Sold','item has been sold'),('restoking','item is restoking in few days'))
    type = models.CharField(max_length=120,blank=False)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    status = models.CharField(max_length=15,blank=False,choices=choices,default = 'Available')
    issue = models.CharField(max_length = 100,default='No Issues')

    class Meta:
        abstract = True
    
    def __str__(self):
        return ' type : {}'.format(self.type)

class Laptop(Device):
    image = models.ImageField(upload_to='Laptops_pic')
    name_of_class = models.CharField(max_length=20,default='Laptop',blank=True,null=True)

    def __str__(self):
        return ' laptop type : {}'.format(self.type)


class Mobile(Device):
    HuaweiP20 = 'HuaweiP'
    HuaweiY9Prime2019 = 'Huawei'
    STATUS_CHOICES = (
        (HuaweiP20, 'HuaweiP'),
        (HuaweiY9Prime2019, 'Huawei')
    )
    SIZE_CHOICES = (
        ('T', 'T'),
        ('K', 'K'),
        ('S', 'S'),
        ('D', 'D'),
        ('Q', 'Q'),
        ('R', 'R'),
        ('50', '50'),
        ('40', '40'),
        ('20', '20'),
        ('15', '15'),
        ('10', '10'),
        ('5', '5'),
        ('2.5', '2.5'),
    )
    FILL_CHOICES = (
        (HuaweiP20, 'HuaweiP20'),
        (HuaweiY9Prime2019, 'HuaweiY9Prime2019'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=HuaweiP20)
    fill = models.CharField(max_length=10, choices=FILL_CHOICES, default='HuaweiP20')
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default='T')
    #barcode = models.CharField(max_length=15,default='HuaweiP20')
    #serial_number = models.CharField(max_length=15, unique=True, primary_key=True,default='00')
    emp_init = models.CharField(max_length=3,null=True, blank=True)
    order = models.ForeignKey(Order, null=True, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mobiles_pic')
    name_of_class = models.CharField(max_length=20,default='Desktop',blank=True,null=True)

    def __str__(self):
        return ' mobile type : {}'.format(self.type)
      # This controls where the user gets taken when a new object is created
    @staticmethod
    def get_absolute_url():
        return reverse('warehouse:bottles')

    def __str__(self):
        return "{} {}-{}-{}-{} by {}".format(self.fill, self.size, self.status, self.barcode, self.serial_number, self.emp_init)
   



class Desktop(Device):
    image = models.ImageField(upload_to='desktop_pic')
    name_of_class = models.CharField(max_length=20,default='Desktop',blank=True,null=True)
    def __str__(self):
        return ' desktop type : {}'.format(self.type)
    HP = 'HP'
    asus = 'asus'
    STATUS_CHOICES = (
        (HP, 'HP'),
        (asus, 'asus'),

    )

    FILL_CHOICES = (
        (HP, 'HP'),
        (asus, 'asus'),

    )
    image = models.ImageField(upload_to='desktop_pic')
    name_of_class = models.CharField(max_length=20,default='Desktop',blank=True,null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=asus)
    fill = models.CharField(max_length=13, choices=FILL_CHOICES)
    #barcode = models.CharField(max_length=15,default='Desktop')
    #serial_number = models.CharField(max_length=15, unique=True, primary_key=True,default='00')
    emp_init = models.CharField(max_length=3,null=True, blank=True)
    order = models.ForeignKey(Order, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return ' desktop type : {}'.format(self.type)

    # This controls where the user gets taken when a new object is created
    @staticmethod
    def get_absolute_url():
        return reverse('warehouse:tubs')

    def __str__(self):
        return "{}-{}-{}, {} by {}".format(self.fill, self.barcode, self.serial_number, self.status, self.emp_init)
   

