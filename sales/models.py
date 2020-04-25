from django.db import models
from django.shortcuts import reverse


# Create your models here.


class Customer(models.Model):
    company = models.CharField(max_length=100, unique=True)
    contact_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, unique=True)
    customer_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)

    @staticmethod
    def get_absolute_url():
        return reverse('sales:customers')

    def __str__(self):
        return ' '.join([self.company, str(self.customer_id)])


class Order(models.Model):
    STATUS_CHOICES = (
        ('QUEUED', 'Queued'),
        ('SHIPPED', 'Shipped'),
    )
    order_number = models.AutoField(primary_key=True, unique=True)
    date_ordered = models.DateField()
    ship_date = models.DateField()
    emp_init = models.CharField(max_length=3, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, null=True, blank=True)
    branch = models.IntegerField(default=1)
    ship_method = models.CharField(max_length=50, null=True, blank=True)
    courier = models.CharField(max_length=50, null=True, blank=True)
    order_type = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS_CHOICES, default='QUEUED')

    def __str__(self):
        return "{} - {} - {} id: {}".format(self.customer, self.ship_date, self.order_number, self.order_number)


class QueuedDesktop(models.Model):

    HP = 'HP'
    asus = 'asus'


    FILL_CHOICES = (
        (HP, 'HP'),
        (asus, 'asus'),

    )
    fill = models.CharField(max_length=13, choices=FILL_CHOICES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return "Desktop quantity: {}".format(self.fill)

class QueuedMobile(models.Model):
    HuaweiP20 = 'HuaweiP'
    HuaweiY9Prime2019 = 'Huawei'
    FILL_CHOICES = (
        (HuaweiP20, 'HuaweiP20'),
        (HuaweiY9Prime2019, 'HuaweiY9Prime2019'),
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
    fill = models.CharField(max_length=13, choices=FILL_CHOICES)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return " mobile quantity: {} {}".format(self.fill, self.size)



