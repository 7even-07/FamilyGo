from django.contrib import admin
from .models import Category, Product, Trending_category, Trending_product,Shirts_category,Shirts_product,Kudta_product,Kudta_category,Sweatshirt_category,Sweatshirt_product,Oversize_category,Oversize_product,Hoodies_category,Hoodies_product,Shervani_category,Shervani_product,Jacket_category,Jacket_product,Jeans_category,Jeans_product,Shorts_category,Shorts_product,Cargos_category,Cargos_product,Chinos_category,Chinos_product,Joggers_category,Joggers_product,Cordouary_category,Cordouary_product,Sweatpants_category,Sweatpants_product,Tshirts_category,Tshirts_product,Hoodiesg_category,Hoodiesg_product,Tank_category,Tank_product,Peplum_category,Peplum_product,Croptops_category,Croptops_product,Cardigan_category,Cardigan_product,Tubetops_category,Tubetops_product,Jeansg_category,Jeansg_product,Shortsg_category,Shortsg_product,Trouser_category,Trouser_product,Skirts_category,Skirts_product,Joggerg_category,Joggerg_product,Chinosg_category,Chinosg_product,Flarepants_category,Flarepants_product, Phones_category,Phones_product,Swatch_category,Swatch_product,Airpods_category,Airpods_product,Mwave_category,Mwave_product,Camera_category,Camera_product,TV_category,TV_product,Light_category,Light_product,Fans_category,Fans_product,Charger_category,Charger_product,VC_category,VC_product,Dumbell_category,Dumbell_product,Bars_category,Bars_product,Hgrip_category,Hgrip_product,Creatine_category,Creatine_product,Protien_category,Protien_product,Gbag_category,Gbag_product,Towels_category,Towels_product,Shoes_category,Shoes_product,Matts_category,Matts_product,Wmachine_category,Wmachine_product,Pens_category,Pens_product,Pencils_category,Pencils_product,Pouch_category,Pouch_product,Lbox_category,Lbox_product,Sanitizer_category,Sanitizer_product,Sbags_category,Sbags_product,Wallets_category,Wallets_product,Umbrella_category,Umbrella_product,Note_category,Note_product,Wbottle_category,Wbottle_product,Novel_category,Novel_product,Sstories_category,Sstories_product,Thriller_category,Thriller_product,Romance_category,Romance_product,Fantasy_category,Fantasy_product,Historical_category,Historical_product,Cook_category,Cook_product,Drama_category,Drama_product,Self_category,Self_product,Travel_category,Travel_product,Eauf_category,Eauf_product,Eaud_category,Eaud_product,Oil_category,Oil_product,Solid_category,Solid_product,Splash_category,Splash_product,Neutral_category,Neutral_product,Seasonal_category,Seasonal_product,Gourmand_category,Gourmand_product,Wood_category,Wood_product,Niche_category,Niche_product,Skincare_category,Skincare_product,Makeup_category,Makeup_product,Haircare_category,Haircare_product,Nailcare_category,Nailcare_product,Fragnance_category,Fragnance_product,Organic_category,Organic_product,Mature_category,Mature_product,Suncare_category,Suncare_product,Lipcare_category,Lipcare_product,Hairdye_category,Hairdye_product,Jewelery_category,Jewelery_product,Watch_category,Watch_product,Hats_category,Hats_product,Eyewear_category,Eyewear_product,Scarves_category,Scarves_product,Handbag_category,Handbag_product,Belts_category,Belts_product,Mittens_category,Mittens_product,HairAccessories_category,HairAccessories_product,Socks_category,Socks_product,Handgun_category,Handgun_product,Sniper_category,Sniper_product,Shotgun_category, Shotgun_product,Dagger_category,Dagger_product,Bows_category,Bows_product,Nunchaku_category,Nunchaku_product,Katana_category,Katana_product,Warhammer_category,Warhammer_product, Stungun_category,Stungun_product,Whips_category,Whips_product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'Category', 'image']

admin.site.register(Product, ProductAdmin)

class TcategoryAdmin(admin.ModelAdmin):
    list_display=['name','description']

admin.site.register(Trending_category,TcategoryAdmin)

class TproductAdmin(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']

admin.site.register(Trending_product,TproductAdmin)

class ScategoryAdmin(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Shirts_category,ScategoryAdmin)

class SproductAdmin(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Shirts_product,SproductAdmin)






class KcategoryAdmin(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Kudta_category,KcategoryAdmin)

class KproductAdmin(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Kudta_product,KproductAdmin)


class OcategoryAdmin(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Oversize_category,OcategoryAdmin)

class OproductAdmin(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Oversize_product,OproductAdmin)



class SwcategoryAdmin(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Sweatshirt_category,SwcategoryAdmin)

class SwproductAdmin(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Sweatshirt_product,SwproductAdmin)


class HoodiescAdmin(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Hoodies_category,HoodiescAdmin)

class HoodiespAdmin(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Hoodies_product,HoodiespAdmin)

class Sher(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Shervani_category,Sher)

class Sherp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Shervani_product,Sherp)

class Jackets(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Jacket_category,Jackets)

class jacketsp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Jacket_product,jacketsp)

class Jeans(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Jeans_category,Jeans)

class JeansP(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Jeans_product,JeansP)

class Shorts(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Shorts_category,Shorts)

class Shortp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Shorts_product,Shortp)

class Cargos(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Cargos_category,Cargos)

class Cargop(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Cargos_product,Cargop)

class Chinos(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Chinos_category,Chinos)

class Chinosp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Chinos_product,Chinosp)

class Joggers(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Joggers_category,Joggers)

class Joggerp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Joggers_product,Joggerp)

class Cordouary(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Cordouary_category,Cordouary)

class Cordouaryp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Cordouary_product,Cordouaryp)

class Sweatpants(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Sweatpants_category,Sweatpants)

class Sweatpantsp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Sweatpants_product,Sweatpantsp)



class Tshirt(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Tshirts_category,Tshirt)

class TshirtP(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Tshirts_product,TshirtP)



class HoodiesgCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Hoodiesg_category, HoodiesgCategoryAdmin)

class HoodiesgProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Hoodiesg_product, HoodiesgProductAdmin)



class TankTop(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Tank_category,TankTop)

class TankTopp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Tank_product,TankTopp)



class Peplum(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Peplum_category,Peplum)

class Peplump(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Peplum_product,Peplump)




class Croptop(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Croptops_category,Croptop)

class Croptoppp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Croptops_product,Croptoppp)




class Cardigan(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Cardigan_category,Cardigan)

class Cardiganp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Cardigan_product,Cardiganp)



class Tubetops(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Tubetops_category,Tubetops)

class Tubetopp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Tubetops_product,Tubetopp)




class Jeansg(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Jeansg_category,Jeansg)

class Jeansgp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Jeansg_product,Jeansgp)




class Shortsg(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Shortsg_category,Shortsg)

class Shortsgp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Shortsg_product,Shortsgp)




class Trouser(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Trouser_category,Trouser)

class Trouserp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Trouser_product,Trouserp)



class Skirts(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Skirts_category,Skirts)

class Skirtsp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Skirts_product,Skirtsp)





class Joggerg(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Joggerg_category,Joggerg)

class Joggergp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Joggerg_product,Joggergp)




class Chinosg(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Chinosg_category,Chinosg)

class Chinosgp(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Chinosg_product,Chinosgp)






class FlarepantsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Flarepants_category, FlarepantsCategoryAdmin)

class FlarepantsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Flarepants_product, FlarepantsProductAdmin)








class PhonesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Phones_category, PhonesCategoryAdmin)

class PhonesProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Phones_product, PhonesProductAdmin)



class SwatchCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Swatch_category, SwatchCategoryAdmin)

class SwatchProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Swatch_product, SwatchProductAdmin)





class AirpodsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Airpods_category, AirpodsCategoryAdmin)

class AirpodsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Airpods_product, AirpodsProductAdmin)




class MwaveCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Mwave_category, MwaveCategoryAdmin)

class MwaveProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Mwave_product, MwaveProductAdmin)




class CameraCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Camera_category, CameraCategoryAdmin)

class CameraProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Camera_product, CameraProductAdmin)


class TVCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(TV_category, TVCategoryAdmin)

class TVProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(TV_product, TVProductAdmin)


class LightCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Light_category, LightCategoryAdmin)

class LightProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Light_product, LightProductAdmin)


class FansCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Fans_category, FansCategoryAdmin)

class FansProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Fans_product, FansProductAdmin)


class ChargerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Charger_category, ChargerCategoryAdmin)

class ChargerProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Charger_product, ChargerProductAdmin)


class VCCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(VC_category, VCCategoryAdmin)

class VCProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(VC_product, VCProductAdmin)


class DumbellCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Dumbell_category, DumbellCategoryAdmin)

class DumbellProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Dumbell_product, DumbellProductAdmin)


class BarsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Bars_category, BarsCategoryAdmin)

class BarsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Bars_product, BarsProductAdmin)


class HgripCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Hgrip_category, HgripCategoryAdmin)

class HgripProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Hgrip_product, HgripProductAdmin)


class CreatineCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Creatine_category, CreatineCategoryAdmin)

class CreatineProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Creatine_product, CreatineProductAdmin)


class ProtienCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Protien_category, ProtienCategoryAdmin)

class ProtienProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Protien_product, ProtienProductAdmin)


class GbagCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Gbag_category, GbagCategoryAdmin)

class GbagProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Gbag_product, GbagProductAdmin)


class TowelsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Towels_category, TowelsCategoryAdmin)

class TowelsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Towels_product, TowelsProductAdmin)


class ShoesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Shoes_category, ShoesCategoryAdmin)

class ShoesProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Shoes_product, ShoesProductAdmin)


class MattsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Matts_category, MattsCategoryAdmin)

class MattsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Matts_product, MattsProductAdmin)


class WmachineCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Wmachine_category, WmachineCategoryAdmin)

class WmachineProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Wmachine_product, WmachineProductAdmin)


class PensCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Pens_category, PensCategoryAdmin)

class PensProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Pens_product, PensProductAdmin)


class PencilsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Pencils_category, PencilsCategoryAdmin)

class PencilsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Pencils_product, PencilsProductAdmin)



class PouchCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Pouch_category, PouchCategoryAdmin)

class PouchProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Pouch_product, PouchProductAdmin)


class LboxCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Lbox_category, LboxCategoryAdmin)

class LboxProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Lbox_product, LboxProductAdmin)


class SanitizerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Sanitizer_category, SanitizerCategoryAdmin)

class SanitizerProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Sanitizer_product, SanitizerProductAdmin)


class SbagsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Sbags_category, SbagsCategoryAdmin)

class SbagsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Sbags_product, SbagsProductAdmin)


class WalletsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Wallets_category, FlarepantsCategoryAdmin)

class WalletsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Wallets_product, WalletsProductAdmin)


class UmbrellaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Umbrella_category, UmbrellaCategoryAdmin)

class UmbrellaProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Umbrella_product, UmbrellaProductAdmin)


class NoteCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Note_category, NoteCategoryAdmin)

class NoteProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Note_product, NoteProductAdmin)


class WbottleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Wbottle_category, WbottleCategoryAdmin)

class WbottleProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Wbottle_product, WbottleProductAdmin)


class NovelCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Novel_category, NovelCategoryAdmin)

class NovelProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Novel_product, NovelProductAdmin)


class SstoriesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Sstories_category, SstoriesCategoryAdmin)

class SstoriesProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Sstories_product, SstoriesProductAdmin)


class ThrillerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Thriller_category, ThrillerCategoryAdmin)

class ThrillerProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Thriller_product, ThrillerProductAdmin)


class RomanceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Romance_category, RomanceCategoryAdmin)

class RomanceProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Romance_product, RomanceProductAdmin)


class FantasyCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Fantasy_category, FantasyCategoryAdmin)

class FantasyProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Fantasy_product, FantasyProductAdmin)


class HistoricalCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Historical_category, HistoricalCategoryAdmin)

class HistoricalProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Historical_product, HistoricalProductAdmin)


class CookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Cook_category, CookCategoryAdmin)

class CookProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Cook_product, CookProductAdmin)


class DramaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Drama_category, DramaCategoryAdmin)

class DramaProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Drama_product, DramaProductAdmin)


class SelfCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Self_category, SelfCategoryAdmin)

class SelfProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Self_product, SelfProductAdmin)


class TravelCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Travel_category, TravelCategoryAdmin)

class TravelProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Travel_product, SelfProductAdmin)


class EaufCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Eauf_category, EaufCategoryAdmin)

class EaufProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Eauf_product, EaufProductAdmin)


class EaudCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Eaud_category, EaudCategoryAdmin)

class EaudProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Eaud_product, EaudProductAdmin)


class OilCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Oil_category, OilCategoryAdmin)

class OilProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Oil_product, OilProductAdmin)


class SolidCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Solid_category, SolidCategoryAdmin)

class SolidProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Solid_product, SolidProductAdmin)


class SplashCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Splash_category, SplashCategoryAdmin)

class SplashProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Splash_product, SplashProductAdmin)


class NeutralCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Neutral_category, FlarepantsCategoryAdmin)

class NeutralProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Neutral_product, NeutralProductAdmin)


class SeasonalCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Seasonal_category, SeasonalCategoryAdmin)

class SeasonalProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Seasonal_product, SeasonalProductAdmin)


class GourmandCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Gourmand_category, GourmandCategoryAdmin)

class GourmandProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Gourmand_product, GourmandProductAdmin)


class WoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Wood_category, WoodCategoryAdmin)

class WoodProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Wood_product, WoodProductAdmin)


class NicheCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Niche_category, NicheCategoryAdmin)

class NicheProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Niche_product, NicheProductAdmin)


class SkincareCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Skincare_category, SkincareCategoryAdmin)

class SkincareProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Skincare_product, SkincareProductAdmin)


class MakeupCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Makeup_category, MakeupCategoryAdmin)

class MakeupProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Makeup_product, MakeupProductAdmin)


class HaircareCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Haircare_category, HaircareCategoryAdmin)

class HaircareProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Haircare_product, HaircareProductAdmin)


class NailcareCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Nailcare_category, NailcareCategoryAdmin)

class NailcareProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Nailcare_product, NailcareProductAdmin)


class FragnanceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Fragnance_category, FragnanceCategoryAdmin)

class FragnanceProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Fragnance_product, FragnanceProductAdmin)


class OrganicCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Organic_category, OrganicCategoryAdmin)

class OrganicProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Organic_product, OrganicProductAdmin)


class MatureCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Mature_category, MatureCategoryAdmin)

class MatureProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Mature_product, MatureProductAdmin)


class SuncareCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Suncare_category, SuncareCategoryAdmin)

class SuncareProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Suncare_product, SuncareProductAdmin)


class LipcareCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Lipcare_category, LipcareCategoryAdmin)

class LipcareProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Lipcare_product, LipcareProductAdmin)


class HairdyeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Hairdye_category, HairdyeCategoryAdmin)

class HairdyeProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Hairdye_product, HairdyeProductAdmin)


class HandgunCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Handgun_category, HandgunCategoryAdmin)

class HandgunProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Handgun_product, HandgunProductAdmin)


class SniperCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Sniper_category, SniperCategoryAdmin)

class SniperProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Sniper_product, SniperProductAdmin)


class ShotgunCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Shotgun_category, ShotgunCategoryAdmin)

class ShotgunProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Shotgun_product, ShotgunProductAdmin)


class DaggerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Dagger_category, DaggerCategoryAdmin)

class DaggerProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Dagger_product, DaggerProductAdmin)


class BowsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Bows_category, BowsCategoryAdmin)

class BowsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Bows_product, BowsProductAdmin)



class NunchakuCategoryAdmin(admin.ModelAdmin):
    list_display=['name','description']
admin.site.register(Nunchaku_category,NunchakuCategoryAdmin)

class NunchakuProductAdmin(admin.ModelAdmin):
    list_display=['p_name','price','description','date','category','image']
admin.site.register(Nunchaku_product,NunchakuProductAdmin)


class KatanaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Katana_category, KatanaCategoryAdmin)

class KatanaProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Katana_product, KatanaProductAdmin)


class WarhammerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Warhammer_category, WarhammerCategoryAdmin)

class WarhammerProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Warhammer_product, WarhammerProductAdmin)



class StungunCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Stungun_category, StungunCategoryAdmin)

class StungunProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Stungun_product, StungunProductAdmin)


class WhipsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Whips_category, WhipsCategoryAdmin)

class WhipsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Whips_product, WhipsProductAdmin)


class JeweleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Jewelery_category, JeweleryCategoryAdmin)

class JeweleryProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Jewelery_product, JeweleryProductAdmin)


class WatchCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Watch_category, WatchCategoryAdmin)

class WatchProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Watch_product, WatchProductAdmin)


class HatsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Hats_category, HatsCategoryAdmin)

class HatsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Hats_product, HatsProductAdmin)


class EyewearCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Eyewear_category, EyewearCategoryAdmin)

class EyewearProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Eyewear_product, EyewearProductAdmin)


class ScarvesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Scarves_category, ScarvesCategoryAdmin)

class ScarvesProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Scarves_product, ScarvesProductAdmin)


class HandbagCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Handbag_category, HandbagCategoryAdmin)

class HandbagProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Handbag_product, HandbagProductAdmin)


class BeltsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Belts_category, BeltsCategoryAdmin)

class BeltsProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Belts_product, BeltsProductAdmin)


class MittensCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Mittens_category, MittensCategoryAdmin)

class MittensProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Mittens_product, MittensProductAdmin)

class HairAccessoriesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(HairAccessories_category, HairAccessoriesCategoryAdmin)

class HairAccessoriesProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(HairAccessories_product, HairAccessoriesProductAdmin)

class SocksCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Socks_category, SocksCategoryAdmin)

class SocksProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'price', 'description', 'date', 'category', 'image']

admin.site.register(Socks_product, SocksProductAdmin)



from.models import Buy

admin.site.register(Buy)
