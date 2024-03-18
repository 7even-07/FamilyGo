from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table="Category"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Product"

from django.contrib.auth.models import User

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,default=None)

    class Meta:
        db_table="Cart"


class Trending_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table="Trending_category"
    
    def __str__(self):
        return self.name
    
class Trending_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Trending_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Trending_product"
        

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Trending_product,on_delete=models.CASCADE)

    class Meta:
        db_table="Cart"

class Shirts_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Shirts_category'

    def __str__(self):
        return self.name

class Shirts_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Trending_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Shirts_product"

class Cart:
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Shirts_product,on_delete=models.CASCADE)

    class Meta:
        db_table='Cart' 



class Kudta_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Kudta_category'

    def __str__(self):
        return self.name
    
class Kudta_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Kudta_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Kudta_product"

class KudtaCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Kudta_product,on_delete=models.CASCADE)

    class Meta:
        db_table='KudtaCart'


class Oversize_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Oversize_category'

    def __str__(self):
        return self.name
    
class Oversize_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Oversize_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Oversize_product"


class OversizeCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Oversize_product,on_delete=models.CASCADE)

    class Meta:
        db_table='Oversizecart'


class Sweatshirt_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Sweatshirt_category'

    def __str__(self):
        return self.name
    
class Sweatshirt_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Sweatshirt_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Sweatshirt_product"


class SweatshirtCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Sweatshirt_product,on_delete=models.CASCADE)

    class Meta:
        db_table='Sweatshirtcart'


class Hoodies_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Hoodies_category'

    def __str__(self):
        return self.name
    
class Hoodies_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Hoodies_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Hoodies_product"


class HoodiesCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Hoodies_product,on_delete=models.CASCADE)

    class Meta:
        db_table='Hoodiescart'

class Shervani_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Shervani_category'

    def __str__(self):
        return self.name
    
class Shervani_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Shervani_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Shervani_product"


class ShervaniCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Shervani_product,on_delete=models.CASCADE)

    class Meta:
        db_table='ShervaniCart'





class Jacket_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Jacket_category'

    def __str__(self):
        return self.name
    
class Jacket_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Jacket_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Jacket_product"


class JacketCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Jacket_product,on_delete=models.CASCADE)

    class Meta:
        db_table='JacketCart'


class Jeans_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Jeans_category'

    def __str__(self):
        return self.name
    
class Jeans_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Jeans_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Jeans_product"


class JeansCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Jeans_product,on_delete=models.CASCADE)

    class Meta:
        db_table='JeansCart'


class Shorts_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Shorts_category'

    def __str__(self):
        return self.name
    
class Shorts_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Shorts_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Shorts_product"


class ShortsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Shorts_product,on_delete=models.CASCADE)

    class Meta:
        db_table='ShortsCart'

class Cargos_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Cargos_category'

    def __str__(self):
        return self.name
    
class Cargos_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Cargos_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Cargos_product"


class CargosCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Cargos_product,on_delete=models.CASCADE)

    class Meta:
        db_table='CargosCart'


class Chinos_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Chinos_category'

    def __str__(self):
        return self.name
    
class Chinos_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Chinos_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Chinos_product"


class ChinosCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Chinos_product,on_delete=models.CASCADE)

    class Meta:
        db_table='ChinosCart'


class Joggers_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Joggers_category'

    def __str__(self):
        return self.name
    
class Joggers_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Joggers_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Joggers_product"


class JoggersCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Joggers_product,on_delete=models.CASCADE)

    class Meta:
        db_table='JoggersCart'


class Cordouary_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Cordouary_category'

    def __str__(self):
        return self.name
    
class Cordouary_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Cordouary_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Cordouary_product"


class CordouaryCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Cordouary_product,on_delete=models.CASCADE)

    class Meta:
        db_table='CordouaryCart'


class Sweatpants_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Sweatpants_category'

    def __str__(self):
        return self.name
    
class Sweatpants_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Sweatpants_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Sweatpants_product"


class SweatpantsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Sweatpants_product,on_delete=models.CASCADE)

    class Meta:
        db_table='SweatpantsCart'

class Tshirts_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Tshirts_category'

    def __str__(self):
        return self.name
    
class Tshirts_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Tshirts_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Tshirts_product"


class TshirtsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Tshirts_product,on_delete=models.CASCADE)

    class Meta:
        db_table='TshirtsCart'



class Hoodiesg_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Hoodiesg_category'

    def __str__(self):
        return self.name
    
class Hoodiesg_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Hoodiesg_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Hoodiesg_product"


class HoodiesgCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Hoodiesg_product,on_delete=models.CASCADE)

    class Meta:
        db_table='HoodiesgCart'


class Tank_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Tank_category'

    def __str__(self):
        return self.name
    
class Tank_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Tank_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Tank_product"


class TankCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Tank_product,on_delete=models.CASCADE)

    class Meta:
        db_table='TanksCart'


class Peplum_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Peplum_category'

    def __str__(self):
        return self.name
    
class Peplum_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Peplum_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Peplum_product"


class PeplumCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Peplum_product,on_delete=models.CASCADE)

    class Meta:
        db_table='PeplumCart'



class Croptops_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Croptops_category'

    def __str__(self):
        return self.name
    
class Croptops_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Croptops_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Croptops_product"


class CroptopsCar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Croptops_product,on_delete=models.CASCADE)

    class Meta:
        db_table='CroptopsCart'



class Cardigan_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Cardigan_category'

    def __str__(self):
        return self.name
    
class Cardigan_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Cardigan_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Cardigan_product"


class CardiganCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Cardigan_product,on_delete=models.CASCADE)

    class Meta:
        db_table='CardiganCart'



class Tubetops_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Tubetops_category'

    def __str__(self):
        return self.name
    
class Tubetops_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Tubetops_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Tubetops_product"


class TubetopsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Tubetops_product,on_delete=models.CASCADE)

    class Meta:
        db_table='TubetopsCart'


class Jeansg_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Jeansg_category'

    def __str__(self):
        return self.name
    
class Jeansg_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Jeansg_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Jeansg_product"


class JeansgCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Jeansg_product,on_delete=models.CASCADE)

    class Meta:
        db_table='JeansgCart'

    



class Shortsg_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Shortsg_category'

    def __str__(self):
        return self.name
    
class Shortsg_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Shortsg_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Shortsg_product"


class ShortsgCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Shortsg_product,on_delete=models.CASCADE)

    class Meta:
        db_table='ShortsgCart'



class Trouser_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Trouser_category'

    def __str__(self):
        return self.name
    
class Trouser_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Trouser_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Trouser_product"


class TrouserCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Trouser_product,on_delete=models.CASCADE)

    class Meta:
        db_table='TrouserCart'




class Skirts_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Skirts_category'

    def __str__(self):
        return self.name
    
class Skirts_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Skirts_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Skirts_product"


class SkirtsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Skirts_product,on_delete=models.CASCADE)

    class Meta:
        db_table='SkirtsCart'





class Joggerg_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Joggerg_category'

    def __str__(self):
        return self.name
    
class Joggerg_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Joggerg_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Joggerg_product"


class JoggergCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Joggerg_product,on_delete=models.CASCADE)

    class Meta:
        db_table='JoggerCart'



class Chinosg_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Chinosg_category'

    def __str__(self):
        return self.name
    
class Chinosg_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Chinosg_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Chinosg_product"


class ChinosgCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Chinosg_product,on_delete=models.CASCADE)

    class Meta:
        db_table='ChinosgCart'



class Flarepants_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Flarepants_category'

    def __str__(self):
        return self.name
    
class Flarepants_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Flarepants_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Flarepants_product"


class FlarepantsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Flarepants_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='FlarepantsCart'





class Phones_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Phones_category'

    def __str__(self):
        return self.name
    
class Phones_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Phones_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Phones_product"


class PhonesCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Phones_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='PhonesCart'






class Swatch_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Swatch_category'

    def __str__(self):
        return self.name
    
class Swatch_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Swatch_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Swatch_product"


class SwatchCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Swatch_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SwatchCart'






class Airpods_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Airpods_category'

    def __str__(self):
        return self.name
    
class Airpods_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Airpods_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Airpods_product"


class AirpodsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Airpods_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='AirpodsCart'






class Mwave_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Mwave_category'

    def __str__(self):
        return self.name
    
class Mwave_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Mwave_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Mwave_product"


class MwaveCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mwave_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='MwaveCart'









class Camera_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Camera_category'

    def __str__(self):
        return self.name
    
class Camera_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Camera_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Camera_product"


class CameraCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Camera_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='CameraCart'





class TV_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='TV_category'

    def __str__(self):
        return self.name
    
class TV_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(TV_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="TV_product"


class TVCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(TV_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='TVCart'






class Light_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Light_category'

    def __str__(self):
        return self.name
    
class Light_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Light_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Light_product"


class LightCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Light_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='LightCart'







class Fans_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Fans_category'

    def __str__(self):
        return self.name
    
class Fans_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Fans_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Fans_product"


class FansCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Fans_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='FanssCart'






class Charger_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Charger_category'

    def __str__(self):
        return self.name
    
class Charger_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Charger_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Charger_product"


class ChargerCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Charger_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='ChargerCart'








class VC_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='VC_category'

    def __str__(self):
        return self.name
    
class VC_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(VC_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="VC_product"


class VCCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(VC_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='VCCart'

class FlarepantsCart:
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Flarepants_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='VCCart'






class Dumbell_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Dumbell_category'

    def __str__(self):
        return self.name
    
class Dumbell_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Dumbell_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Dumbell_product"


class DumbellCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Dumbell_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='DumbellCart'








class Bars_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Bars_category'

    def __str__(self):
        return self.name
    
class Bars_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Bars_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Bars_product"


class BarsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Bars_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='BarsCart'









class Hgrip_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Hgrip_category'

    def __str__(self):
        return self.name
    
class Hgrip_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Hgrip_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Hgrip_product"


class HgripCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Hgrip_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HgripCart'








class Creatine_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Creatine_category'

    def __str__(self):
        return self.name
    
class Creatine_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Creatine_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Creatine_product"


class CreatineCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Creatine_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='CreatineCart'









class Protien_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Protien_category'

    def __str__(self):
        return self.name
    
class Protien_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Protien_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Protien_product"


class ProtienCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Hgrip_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='ProtienCart'









class Gbag_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Gbag_category'

    def __str__(self):
        return self.name
    
class Gbag_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Gbag_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Gbag_product"


class GbagCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Gbag_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='GbagCart'









class Towels_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Towels_category'

    def __str__(self):
        return self.name
    
class Towels_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Towels_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Towels_product"


class TowelsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Towels_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='TowelsCart'









class Shoes_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Shoes_category'

    def __str__(self):
        return self.name
    
class Shoes_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Shoes_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Shoes_product"


class ShoesCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Shoes_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='ShoesCart'









class Matts_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Matts_category'

    def __str__(self):
        return self.name
    
class Matts_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Matts_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Matts_product"


class MattsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Matts_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='MattsCart'









class Wmachine_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='HWmachine_category'

    def __str__(self):
        return self.name
    
class Wmachine_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Wmachine_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Wmachine_product"


class WmachineCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Wmachine_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='WmachineCart'









class Pens_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Pens_category'

    def __str__(self):
        return self.name
    
class Pens_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Pens_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Pens_product"


class PensCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Pens_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='PensCart'











class Pencils_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Pencils_category'

    def __str__(self):
        return self.name
    
class Pencils_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Pencils_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Pencils_product"


class PencilsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Pencils_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='PencilsCart'











class Pouch_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Pouch_category'

    def __str__(self):
        return self.name
    
class Pouch_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Pouch_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Pouch_product"


class PouchCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Pouch_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='PouchCart'











class Lbox_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Lbox_category'

    def __str__(self):
        return self.name
    
class Lbox_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Lbox_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Lbox_product"


class LboxCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Lbox_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='LboxCart'











class Sanitizer_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Sanitizer_category'

    def __str__(self):
        return self.name
    
class Sanitizer_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Sanitizer_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Sanitizer_product"


class SanitizerCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Sanitizer_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SanitizerCart'











class Sbags_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Sbags_category'

    def __str__(self):
        return self.name
    
class Sbags_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Sbags_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Sbags_product"


class SbagsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Sbags_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SbagsCart'











class Wallets_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Wallets_category'

    def __str__(self):
        return self.name
    
class Wallets_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Wallets_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Wallets_product"


class WalletsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Wallets_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='WalletsCart'











class Umbrella_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Umbrella_category'

    def __str__(self):
        return self.name
    
class Umbrella_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Umbrella_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Umbrella_product"


class UmbrellaCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Umbrella_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='UmbrellaCart'











class Note_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Note_category'

    def __str__(self):
        return self.name
    
class Note_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Note_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Note_product"


class NoteCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Note_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='NoteCart'











class Wbottle_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Wbottle_category'

    def __str__(self):
        return self.name
    
class Wbottle_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Wbottle_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Wbottle_product"


class WbottleCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Wbottle_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='WbottleCart'









class Novel_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Novel_category'

    def __str__(self):
        return self.name
    
class Novel_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Novel_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Novel_product"


class NovelCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Wbottle_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='NovelCart'









class Sstories_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Sstories_category'

    def __str__(self):
        return self.name
    
class Sstories_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Sstories_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Sstories_product"


class SstoriesCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Sstories_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SstoriesCart'









class Thriller_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Thriller_category'

    def __str__(self):
        return self.name
    
class Thriller_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Thriller_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Thriller_product"


class ThrillerCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Thriller_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='ThrillerCart'









class Romance_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Romance_category'

    def __str__(self):
        return self.name
    
class Romance_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Romance_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Romance_product"


class RomanceCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Romance_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='RomanceCart'









class Fantasy_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Fantasy_category'

    def __str__(self):
        return self.name
    
class Fantasy_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Fantasy_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Fantasy_product"


class FantasyCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Fantasy_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='FantasyCart'









class Historical_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Historical_category'

    def __str__(self):
        return self.name
    
class Historical_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Historical_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Historical_product"


class HistoricalCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Historical_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HistoricalCart'









class Cook_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Cook_category'

    def __str__(self):
        return self.name
    
class Cook_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Cook_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Cook_product"


class CookCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Cook_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='CookCart'









class Drama_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Drama_category'

    def __str__(self):
        return self.name
    
class Drama_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Drama_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Drama_product"


class DramaCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Drama_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='DramaCart'









class Self_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Self_category'

    def __str__(self):
        return self.name
    
class Self_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Self_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Self_product"


class SelfCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Self_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SelfCart'









class Travel_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Travel_category'

    def __str__(self):
        return self.name
    
class Travel_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Travel_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Travel_product"


class TravelCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Travel_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='TravelCart'








class Eauf_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Eauf_category'

    def __str__(self):
        return self.name
    
class Eauf_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Eauf_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Eauf_product"


class EaufCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Eauf_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='EaufCart'







class Eaud_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Eaud_category'

    def __str__(self):
        return self.name
    
class Eaud_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Eaud_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Eaud_product"


class EaudCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Eaud_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='EaudCart'







class Oil_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Oil_category'

    def __str__(self):
        return self.name
    
class Oil_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Oil_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Oil_product"


class OilCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Oil_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='OilCart'







class Solid_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Solid_category'

    def __str__(self):
        return self.name
    
class Solid_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Solid_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Solid_product"


class SolidCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Solid_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SolidCart'







class Splash_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Splash_category'

    def __str__(self):
        return self.name
    
class Splash_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Splash_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Splash_product"


class SplashCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Splash_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SplashCart'







class Neutral_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Neutral_category'

    def __str__(self):
        return self.name
    
class Neutral_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Neutral_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Neutral_product"


class NeutralCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Neutral_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='NeutralCart'







class Seasonal_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Seasonal_category'

    def __str__(self):
        return self.name
    
class Seasonal_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Seasonal_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Seasonal_product"


class SeasonalCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Seasonal_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SeasonalCart'







class Gourmand_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Gourmand_category'

    def __str__(self):
        return self.name
    
class Gourmand_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Gourmand_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Gourmand_product"


class GourmandCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Gourmand_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='GourmandCart'







class Wood_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Wood_category'

    def __str__(self):
        return self.name
    
class Wood_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Wood_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Wood_product"


class WoodCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Wood_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='WoodCart'







class Niche_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Niche_category'

    def __str__(self):
        return self.name
    
class Niche_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Niche_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Niche_product"


class NicheCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Niche_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='NicheCart'









class Skincare_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Skincare_category'

    def __str__(self):
        return self.name
    
class Skincare_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Skincare_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Skincare_product"


class SkincareCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Skincare_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SkincareCart'








class Makeup_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Makeup_category'

    def __str__(self):
        return self.name
    
class Makeup_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Makeup_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Makeup_product"


class MakeupCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Makeup_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='MakeupCart'








class Haircare_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Haircare_category'

    def __str__(self):
        return self.name
    
class Haircare_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Haircare_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Haircare_product"


class HaircareCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Haircare_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HaircareCart'








class Nailcare_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Nailcare_category'

    def __str__(self):
        return self.name
    
class Nailcare_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Nailcare_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Nailcare_product"


class NailcareCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Nailcare_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='NailcareCart'








class Fragnance_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Fragnance_category'

    def __str__(self):
        return self.name
    
class Fragnance_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Fragnance_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Fragnance_product"


class FragnanceCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Fragnance_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='FragnanceCart'








class Organic_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Organic_category'

    def __str__(self):
        return self.name
    
class Organic_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Organic_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Organic_product"


class OrganicCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Organic_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='OrganicCart'








class Mature_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Mature_category'

    def __str__(self):
        return self.name
    
class Mature_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Mature_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Mature_product"


class MatureCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mature_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='MatureCart'








class Suncare_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Suncare_category'

    def __str__(self):
        return self.name
    
class Suncare_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Suncare_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Suncare_product"


class SuncareCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Suncare_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SuncareCart'








class Lipcare_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Lipcare_category'

    def __str__(self):
        return self.name
    
class Lipcare_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Lipcare_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Lipcare_product"


class LipcareCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Lipcare_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='LipcareCart'








class Hairdye_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Hairdye_category'

    def __str__(self):
        return self.name
    
class Hairdye_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Hairdye_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Hairdye_product"


class HairdyeCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Hairdye_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HairdyeCart'









class Handgun_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Handgun_category'

    def __str__(self):
        return self.name
    
class Handgun_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Handgun_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Handgun_product"


class HandgunCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Handgun_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HandgunCart'









class Sniper_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='HSniper_category'

    def __str__(self):
        return self.name
    
class Sniper_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Sniper_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Sniper_product"


class SniperCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Sniper_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SniperCart'









class Shotgun_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Shotgun_category'

    def __str__(self):
        return self.name
    
class Shotgun_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Shotgun_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Shotgun_product"


class ShotgunCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Shotgun_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='ShotgunCart'









class Dagger_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Dagger_category'

    def __str__(self):
        return self.name
    
class Dagger_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Dagger_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Dagger_product"


class DaggerCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Dagger_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='DaggerCart'









class Bows_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Bows_category'

    def __str__(self):
        return self.name
    
class Bows_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Bows_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Bows_product"


class BowsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Bows_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='BowsCart'









class Nunchaku_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Nunchaku_category'

    def __str__(self):
        return self.name
    
class Nunchaku_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Nunchaku_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Nunchaku_product"


class NunchakuCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Nunchaku_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='NunchakuCart'









class Katana_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Katana_category'

    def __str__(self):
        return self.name
    
class Katana_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Katana_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Katana_product"


class KatanaCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Katana_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='KatanaCart'









class Warhammer_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Warhammer_category'

    def __str__(self):
        return self.name
    
class Warhammer_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Warhammer_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Warhammer_product"


class WarhammerCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Warhammer_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='WarhammerCart'









class Stungun_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Stungun_category'

    def __str__(self):
        return self.name
    
class Stungun_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Stungun_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Stungun_product"


class StungunCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Stungun_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='StungunCart'









class Whips_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Whips_category'

    def __str__(self):
        return self.name
    
class Whips_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Whips_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Whips_product"


class WhipsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Whips_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='WhipsCart'








class Jewelery_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Jewelery_category'

    def __str__(self):
        return self.name
    
class Jewelery_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Jewelery_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Jewelery_product"


class JeweleryCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Jewelery_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='JeweleryCart'















class Watch_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Watch_category'

    def __str__(self):
        return self.name
    
class Watch_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Watch_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Watch_product"


class WatchCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Watch_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='WatchCart'







class Hats_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Hats_category'

    def __str__(self):
        return self.name
    
class Hats_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Hats_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Hats_product"


class HatsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Hats_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HatsCart'







class Eyewear_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Eyewear_category'

    def __str__(self):
        return self.name
    
class Eyewear_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Eyewear_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Eyewear_product"


class EyewearCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Eyewear_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='EyewearCart'







class Scarves_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Scarves_category'

    def __str__(self):
        return self.name
    
class Scarves_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Scarves_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Scarves_product"


class ScarvesCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Scarves_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='ScarvesCart'







class Handbag_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Handbag_category'

    def __str__(self):
        return self.name
    
class Handbag_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Handbag_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Handbag_product"


class HandbagCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Whips_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HandbagCart'







class Handbag_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Handbag_category'

    def __str__(self):
        return self.name
    
class Handbag_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Handbag_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Handbag_product"


class HandbagCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Handbag_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HandbagCart'







class Belts_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Belts_category'

    def __str__(self):
        return self.name
    
class Belts_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Belts_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Belts_product"


class BeltsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Belts_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='BeltsCart'







class Mittens_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Mittens_category'

    def __str__(self):
        return self.name
    
class Mittens_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Mittens_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Mittens_product"


class MittensCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mittens_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='MittensCart'






class HairAccessories_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='HairAccessories_category'

    def __str__(self):
        return self.name
    
class HairAccessories_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(HairAccessories_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="HairAccessories_product"


class HairAccessoriesCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(HairAccessories_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='HairAccessoriesCart'









class Socks_category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='Socks_category'

    def __str__(self):
        return self.name
    
class Socks_product(models.Model):
    p_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Socks_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='familygo/images')

    class Meta:
        db_table="Socks_product"


class SocksCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Socks_product,on_delete=models.CASCADE)  

    class Meta:
        db_table='SocksCart'






class UserProfile(models.Model):
    MALE='M'
    FEMALE='F'
    OTHER='O'

    GENDER_CHOICES=[
        (MALE,'Male'),
        (FEMALE,'Female'),
        (OTHER,'Male'),
    ]

    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    age=models.IntegerField()
    mobile_number=models.CharField(max_length=30)
    address=models.TextField(max_length=300)

    class Meta:
        db_table="UserProfile"


from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields="__all__"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, default=None)
    shirt = models.ForeignKey(Shirts_product, on_delete=models.CASCADE, null=True, blank=True, default=None)
    kudta = models.ForeignKey(Kudta_product, on_delete=models.CASCADE, null=True, blank=True, default=None)
    oversize = models.ForeignKey(Oversize_product, on_delete=models.CASCADE, null=True, blank=True, default=None)
    sweatb = models.ForeignKey(Sweatshirt_product, on_delete=models.CASCADE, null=True, blank=True, default=None)
    hoodiesb = models.ForeignKey(Hoodies_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    shervani = models.ForeignKey(Shervani_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    jacket = models.ForeignKey(Jacket_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    jeans = models.ForeignKey(Jeans_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    shortsb = models.ForeignKey(Shorts_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    cargo = models.ForeignKey(Cargos_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    chinosb = models.ForeignKey(Chinos_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    joggerb = models.ForeignKey(Joggers_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    cordouary = models.ForeignKey(Cordouary_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    sweatp = models.ForeignKey(Sweatpants_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    tshirt = models.ForeignKey(Tshirts_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    hoodiesg = models.ForeignKey(Hoodiesg_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    tank = models.ForeignKey(Tank_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    peplum = models.ForeignKey(Peplum_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    crop = models.ForeignKey(Croptops_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    cardigan = models.ForeignKey(Cardigan_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    tube = models.ForeignKey(Tubetops_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    jeansg = models.ForeignKey(Jeansg_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    shortsg = models.ForeignKey(Shortsg_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    trouser = models.ForeignKey(Trouser_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    skirt = models.ForeignKey(Skirts_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    joggerg = models.ForeignKey(Joggerg_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    chinosg = models.ForeignKey(Chinosg_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    flarepants = models.ForeignKey(Flarepants_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    phone = models.ForeignKey(Phones_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    swatch = models.ForeignKey(Swatch_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    airpod = models.ForeignKey(Airpods_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    mwave = models.ForeignKey(Mwave_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    camera = models.ForeignKey(Camera_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    tv = models.ForeignKey(TV_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    light = models.ForeignKey(Light_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    fan = models.ForeignKey(Fans_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    charger = models.ForeignKey(Charger_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    vc = models.ForeignKey(VC_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    dumbell = models.ForeignKey(Dumbell_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    bar = models.ForeignKey(Bars_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    hgrip = models.ForeignKey(Hgrip_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    creatine = models.ForeignKey(Creatine_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    protien = models.ForeignKey(Protien_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    gbag = models.ForeignKey(Gbag_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    towel = models.ForeignKey(Towels_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    shoes = models.ForeignKey(Shoes_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    matt = models.ForeignKey(Matts_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    wmachine = models.ForeignKey(Wmachine_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    pen = models.ForeignKey(Pens_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    pencil = models.ForeignKey(Pencils_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    pouch = models.ForeignKey(Pouch_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    lbox = models.ForeignKey(Lbox_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    sanitizer = models.ForeignKey(Sanitizer_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    sbag = models.ForeignKey(Sbags_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    wallet = models.ForeignKey(Wallets_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    umbrella = models.ForeignKey(Umbrella_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    note = models.ForeignKey(Note_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    wbottle = models.ForeignKey(Wbottle_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    novel = models.ForeignKey(Novel_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    sstories = models.ForeignKey(Sstories_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    thriller = models.ForeignKey(Thriller_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    romance = models.ForeignKey(Romance_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    fantasy = models.ForeignKey(Fantasy_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    historical = models.ForeignKey(Historical_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    cook = models.ForeignKey(Cook_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    drama = models.ForeignKey(Drama_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    help = models.ForeignKey(Self_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    travel = models.ForeignKey(Travel_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    eauf = models.ForeignKey(Eauf_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    eaud = models.ForeignKey(Eaud_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    oil = models.ForeignKey(Oil_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    solid = models.ForeignKey(Solid_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    splash = models.ForeignKey(Splash_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    neutral = models.ForeignKey(Neutral_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    seasonal = models.ForeignKey(Seasonal_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    gourmand = models.ForeignKey(Gourmand_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    wood = models.ForeignKey(Wood_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    niche = models.ForeignKey(Niche_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    skincare = models.ForeignKey(Skincare_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    makeup = models.ForeignKey(Makeup_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    haircare = models.ForeignKey(Haircare_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    haircare = models.ForeignKey(Haircare_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    nailcare = models.ForeignKey(Nailcare_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    fragnance = models.ForeignKey(Fragnance_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    organic = models.ForeignKey(Organic_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    mature = models.ForeignKey(Mature_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    suncare = models.ForeignKey(Suncare_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    lipcare = models.ForeignKey(Lipcare_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    hairdye = models.ForeignKey(Hairdye_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    handgun = models.ForeignKey(Handgun_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    sniper = models.ForeignKey(Sniper_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    shotgun = models.ForeignKey(Shotgun_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    dagger = models.ForeignKey(Dagger_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    bow= models.ForeignKey(Bows_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    nunchaku= models.ForeignKey(Nunchaku_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    katana= models.ForeignKey(Katana_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    warhammer= models.ForeignKey(Warhammer_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    stungun= models.ForeignKey(Stungun_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    whips= models.ForeignKey(Whips_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    jewelery= models.ForeignKey(Jewelery_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    watch= models.ForeignKey(Watch_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    hats= models.ForeignKey(Hats_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    eyewear= models.ForeignKey(Eyewear_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    scarves= models.ForeignKey(Scarves_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    handbag= models.ForeignKey(Handbag_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    belts= models.ForeignKey(Belts_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    mittens= models.ForeignKey(Mittens_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    haira= models.ForeignKey(HairAccessories_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    socks= models.ForeignKey(Socks_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    tcart= models.ForeignKey(Trending_product, on_delete=models.CASCADE,null=True,blank=True,default=None)
    
    quantity = models.PositiveIntegerField(default=1)
    def individual_price(self):
        return self.quantity * self.hoodiesb.price 

    class Meta:
        db_table = "Cart"







class Buy(models.Model):
    name=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    payment_id=models.CharField(max_length=30)
    paid=models.BooleanField(default=False)

    db_table='Buy'




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} - {self.quantity} units"
    