from django.db import models

# Create your models here.
class Series (models.Model):
	id = models.AutoField(primary_key=True)
	series_name = models.CharField(max_length=25)
	slug = models.SlugField(max_length=200)
	starting_from = models.IntegerField()
	logo_serie  = models.ImageField(upload_to='serie/images/', )
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering =['-created_at']

	def __str__(self):
		return self.series_name


class iPhone_Name(models.Model):
	id = models.AutoField(primary_key=True)
	of_series = models.ForeignKey(Series, on_delete=models.CASCADE)
	iPhone_name = models.CharField(max_length=25)
	slug = models.SlugField(max_length=200)
	processor = models.CharField(max_length=110)
	camera = models.CharField(max_length=100)
	display = models.CharField(max_length=100)
	display_panel_type = models.CharField(max_length=100 )
	ratings_ips = models.CharField(max_length=100,)


	def __str__(self):
		return self.iPhone_name



class Product (models.Model):
	CONDITION_CHOICES = ( ('new', 'New'), ('best', ' Best'), ('good', ' Good'), )
	id = models.AutoField(primary_key=True)
	name = models.ForeignKey(iPhone_Name, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=200)
	new_price = models.IntegerField()
	older_price = models.IntegerField()
	battery_health = models.IntegerField()
	condition = models.CharField(max_length=100, choices=CONDITION_CHOICES, default='best')
	color= models.CharField(max_length=40)
	storage = models.CharField(max_length=100)
	face_id = models.BooleanField(default=True, )
	special_note = models.CharField(max_length=1000 )
	main_image = models.ImageField(upload_to='main_images/', )
	status = models.BooleanField(default="True")
	created_at = models.DateTimeField(auto_now=True,)
	uploaded_at = models.DateField(auto_now_add=True)
	warranty  = models.IntegerField()

	@property
	def discount(self):
		discount_per = self.new_price / self.older_price
		discount_per = str(100 -  int(discount_per*100)) + str('%')
		return discount_per

	@property
	def you_save(self):
		amount_saving = self.older_price - self.new_price
		amount_saving = str(amount_saving)
		return amount_saving
	class Meta:
		ordering = ['-created_at']



class other_product_images(models.Model):
	proudct_name = models.ForeignKey(Product, on_delete=models.CASCADE, )
	product_image = models.ImageField(upload_to='product/images/')

class Produts_Offers(models.Model):
	i_product = models.IntegerField()
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated_at']
