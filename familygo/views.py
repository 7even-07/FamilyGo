from django.shortcuts import get_object_or_404, render,redirect
from.models import Order, OrderItem, Product,Category,Cart,Trending_product,Shirts_product,Shirts_category,Kudta_product,Oversize_product,Sweatshirt_product,Hoodies_product,Shervani_product,Jacket_product,Jeans_product,Shorts_product,Cargos_product,Chinos_product,Joggers_product,Cordouary_product,Sweatpants_product,Tshirts_product,Hoodiesg_product,Tank_product,Peplum_product,Croptops_product,Cardigan_product,Tubetops_product,Jeansg_product,Shortsg_product,Trouser_product,Skirts_product,Joggerg_product,Chinosg_product,Flarepants_product,Phones_product,Swatch_product,Airpods_product,Mwave_product,Camera_product,TV_product,Light_product,Fans_product,Charger_product,VC_product,Dumbell_product,Bars_product,Hgrip_product,Creatine_product,Protien_product,Gbag_product,Towels_product,Shoes_product,Matts_product,Wmachine_product,Pens_product,Pencils_product,Pouch_product,Lbox_product,Sanitizer_product,Sbags_product,Wallets_product,Umbrella_product,Note_product,Wbottle_product,Novel_product,Sstories_product,Thriller_product,Romance_product,Fantasy_product,Historical_product,Cook_product,Drama_product,Self_product,Travel_product,Eauf_product,Eaud_product,Oil_product,Solid_product,Splash_product,Neutral_product,Seasonal_product,Gourmand_product,Wood_product,Niche_product,Skincare_product,Makeup_product,Haircare_product,Nailcare_product,Fragnance_product,Organic_product,Mature_product,Suncare_product,Lipcare_product,Hairdye_product,Handgun_product,Sniper_product,Shotgun_product,Dagger_product,Bows_product,Nunchaku_product,Katana_product,Warhammer_product,Stungun_product,Whips_product,Jewelery_product,Watch_product,Hats_product,Eyewear_product,Scarves_product,Handbag_product,Belts_product,Mittens_product,HairAccessories_product,Socks_product,UserProfile,UserForm

# Create your views here.

def home(request):
    pl = Product.objects.all()
    cl = Trending_product.objects.all()
    context = {"pl": pl, "cl": cl}
    return render(request, 'home.html', context)

def mens_collection(request):
    return render(request, 'mens.html')

def women_collection(request):
    return render(request, 'womens.html')

def electronic_collection(request):
    return render(request, 'electronics.html')

def gym_view(request):
    return render(request,'gym.html')

def school_view(request):
    return render(request,'school.html')

def book_view(request):
    return render(request,'books.html')

def perfume_view(request):
    return render(request,'perfumes.html')

def cosmetic_view(request):
    return render(request,'cosmetics.html')

def weapon_view(request):
    return render(request,'weapons.html')

def accessories_view(request):
    return render(request,'accessories.html')

def shirt_view(request):
    pl=Shirts_product.objects.all()
    context={'pl':pl}
    return render(request,'shirt.html',context)

def kudta_view(request):
    pl=Kudta_product.objects.all()
    context={"pl":pl}
    return render(request,'kudta.html',context)

def oversize_view(request):
    pl=Oversize_product.objects.all()
    context={'pl':pl}
    return render(request,'oversize.html',context)

def sweatb_views(request):
    pl=Sweatshirt_product.objects.all()
    context={'pl':pl}
    return render(request,'sweatb.html',context)

def hoodiesb_view(request):
    pl=Hoodies_product.objects.all()
    context={'pl':pl}
    return render(request,'hoodiesb.html',context)

def shervani_view(request):
    pl=Shervani_product.objects.all()
    context={'pl':pl}
    return render(request,'shervani.html',context)

def jackets_view(request):
    pl=Jacket_product.objects.all()
    context={'pl':pl}
    return render(request,'jackets.html',context)

def jeans_view(request):
    pl=Jeans_product.objects.all()
    context={'pl':pl}
    return render(request,'jeans.html',context)

def shorts_view(request):
    pl=Shorts_product.objects.all()
    context={'pl':pl}
    return render(request,'shorts.html',context)

def cargo_view(request):
    pl=Cargos_product.objects.all()
    context={'pl':pl}
    return render(request,'cargo.html',context)

def chinos_view(request):
    pl=Chinos_product.objects.all()
    context={'pl':pl}
    return render(request,'chinos.html',context)

def joggers_view(request):
    pl=Joggers_product.objects.all()
    context={'pl':pl}
    return render(request,'joggers.html',context)

def cordouary_view(Request):
    pl=Cordouary_product.objects.all()
    context={'pl':pl}
    return render(Request,'cordouary.html',context)

def sweatp_views(request):
    pl=Sweatpants_product.objects.all()
    context={'pl':pl}
    return render(request,'sweatp.html',context)

def tshirts_view(request):
    pl=Tshirts_product.objects.all()
    context={'pl':pl}
    return render(request,'tshirts.html',context)

def hoodiesg_view(request):
    pl=Hoodiesg_product.objects.all()
    context={'pl':pl}
    return render(request,'hoodiesg.html',context)

def tank_view(request):
    pl=Tank_product.objects.all()
    context={'pl':pl}
    return render(request,'tank.html',context)

def peplum_view(request):
    pl=Peplum_product.objects.all()
    context={'pl':pl}
    return render(request,'peplum.html',context)

def crop_view(request):
    pl=Croptops_product.objects.all()
    context={'pl':pl}
    return render(request,'crop.html',context)

def cardigans_view(request):
    pl=Cardigan_product.objects.all()
    context={'pl':pl}
    return render(request,'cardigans.html',context)

def tube_view(request):
    pl=Tubetops_product.objects.all()
    context={'pl':pl}
    return render(request,'tube.html',context)

def jeansg_view(request):
    pl=Jeansg_product.objects.all()
    context={'pl':pl}
    return render(request,'jeansg.html',context)

def shortsg_view(request):
    pl=Shortsg_product.objects.all()
    context={'pl':pl}
    return render(request,'shortsg.html',context)

def trouser_view(request):
    pl=Trouser_product.objects.all()
    context={'pl':pl}
    return render(request,'trouser.html',context)

def skirts_view(request):
    pl=Skirts_product.objects.all()
    context={'pl':pl}
    return render(request,'skirts.html',context)

def jogger_view(request):
    pl=Joggerg_product.objects.all()
    context={'pl':pl}
    return render(request,'jogger.html',context)

def chinosg_view(request):
    pl=Chinosg_product.objects.all()
    context={'pl':pl}
    return render(request,'chinosg.html',context)

def flare_view(request):
    pl=Flarepants_product.objects.all()
    context={'pl':pl}
    return render(request,'flare.html',context)

def phone_view(request):
    pl=Phones_product.objects.all()
    context={'pl':pl}
    return render(request,'phone.html',context)  


def swatch_view(request):
    pl=Swatch_product.objects.all()
    context={'pl':pl}
    return render(request,'swatch.html',context)

def airpods_view(request):
    pl=Airpods_product.objects.all()
    context={'pl':pl}
    return render(request,'airpods.html',context)

def mvave_view(request):
    pl=Mwave_product.objects.all()
    context={'pl':pl}
    return render(request,'mvave.html',context)

def camera_view(request):
    pl=Camera_product.objects.all()
    context={'pl':pl}
    return render(request,'camera.html',context)

def tv_view(request):
    pl=TV_product.objects.all()
    context={'pl':pl}
    return render(request,'tv.html',context)

def light_view(request):
    pl=Light_product.objects.all()
    context={'pl':pl}
    return render(request,'light.html',context)

def fans_view(request):
    pl=Fans_product.objects.all()
    context={'pl':pl}
    return render(request,'fans.html',context)

def charger_view(request):
    pl=Charger_product.objects.all()
    context={'pl':pl}
    return render(request,'charger.html',context)

def vc_view(request):
    pl=VC_product.objects.all()
    context={'pl':pl}
    return render(request,'vc.html',context)

def dumbell_view(request):
    pl=Dumbell_product.objects.all()
    context={'pl':pl}
    return render(request,'dumbell.html',context)

def bars_view(request):
    pl=Bars_product.objects.all()
    context={'pl':pl}
    return render(request,'bars.html',context)

def hgrip_view(request):
    pl=Hgrip_product.objects.all()
    context={'pl':pl}
    return render(request,'hgrip.html',context)

def creatine_view(request):
    pl=Creatine_product.objects.all()
    context={'pl':pl}
    return render(request,'creatine.html',context)

def protien_view(request):
    pl=Protien_product.objects.all()
    context={'pl':pl}
    return render(request,'protien.html',context)

def gbag_view(request):
    pl=Gbag_product.objects.all()
    context={'pl':pl}
    return render(request,'gbag.html',context)

def towels_view(request):
    pl=Towels_product.objects.all()
    context={'pl':pl}
    return render(request,'towels.html',context)

def shoes_view(request):
    pl=Shoes_product.objects.all()
    context={'pl':pl}
    return render(request,'shoes.html',context)

def matt_view(request):
    pl=Matts_product.objects.all()
    context={'pl':pl}
    return render(request,'matt.html',context)

def wm_view(request):
    pl=Wmachine_product.objects.all()
    context={'pl':pl}
    return render(request,'wm.html',context)

def pens_view(request):
    pl=Pens_product.objects.all()
    context={'pl':pl}
    return render(request,'pens.html',context)

def pencil_view(request):
    pl=Pencils_product.objects.all()
    context={'pl':pl}
    return render(request,'pencil.html',context)

def pouch_view(request):
    pl=Pouch_product.objects.all()
    context={'pl':pl}
    return render(request,'pouch.html',context)

def lbox_view(request):
    pl=Lbox_product.objects.all()
    context={'pl':pl}
    return render(request,'lbox.html',context)

def sanitizer_view(request):
    pl=Sanitizer_product.objects.all()
    context={'pl':pl}
    return render(request,'sanitizer.html',context)

def sbags_view(request):
    pl=Sbags_product.objects.all()
    context={'pl':pl}
    return render(request,'sbags.html',context)

def wallets_view(request):
    pl=Wallets_product.objects.all()
    context={'pl':pl}
    return render(request,'wallets.html',context)

def umb_view(request):
    pl=Umbrella_product.objects.all()
    context={'pl':pl}
    return render(request,'umb.html',context)

def note_view(request):
    pl=Note_product.objects.all()
    context={'pl':pl}
    return render(request,'note.html',context)

def wbottles_view(request):
    pl=Wbottle_product.objects.all()
    context={'pl':pl}
    return render(request,'wbottles.html',context)

def novel_view(request):
    pl=Novel_product.objects.all()
    context={'pl':pl}
    return render(request,'novel.html',context)

def sstories_view(request):
    pl=Sstories_product.objects.all()
    context={'pl':pl}
    return render(request,'sstories.html',context)

def thriller_view(request):
    pl=Thriller_product.objects.all()
    context={'pl':pl}
    return render(request,'thriller.html',context)

def romance_view(request):
    pl=Romance_product.objects.all()
    context={'pl':pl}
    return render(request,'romance.html',context)

def fantasy_view(request):
    pl=Fantasy_product.objects.all()
    context={'pl':pl}
    return render(request,'fantasy.html',context)

def historical_view(request):
    pl=Historical_product.objects.all()
    context={'pl':pl}
    return render(request,'historical.html',context)

def cook_view(request):
    pl=Cook_product.objects.all()
    context={'pl':pl}
    return render(request,'cook.html',context)

def drama_view(request):
    pl=Drama_product.objects.all()
    context={'pl':pl}
    return render(request,'drama.html',context)

def self_view(request):
    pl=Self_product.objects.all()
    context={'pl':pl}
    return render(request,'self.html',context)

def travel_view(request):
    pl=Travel_product.objects.all()
    context={'pl':pl}
    return render(request,'travel.html',context)

def eau_view(request):
    pl=Eauf_product.objects.all()
    context={'pl':pl}
    return render(request,'eau.html',context)

def de_view(request):
    pl=Eaud_product.objects.all()
    context={'pl':pl}
    return render(request,'de.html',context)

def oil_view(request):
    pl=Oil_product.objects.all()
    context={'pl':pl}
    return render(request,'oil.html',context)

def solid_view(request):
    pl=Solid_product.objects.all()
    context={'pl':pl}
    return render(request,'solid.html',context)

def splash_view(request):
    pl=Splash_product.objects.all()
    context={'pl':pl}
    return render(request,'splash.html',context)

def neutral_view(request):
    pl=Neutral_product.objects.all()
    context={'pl':pl}
    return render(request,'neutral.html',context)

def seasonal_view(request):
    pl=Seasonal_product.objects.all()
    context={'pl':pl}
    return render(request,'seasonal.html',context)

def gourmand_view(request):
    pl=Gourmand_product.objects.all()
    context={'pl':pl}
    return render(request,'gourmand.html',context)

def wood_view(request):
    pl=Wood_product.objects.all()
    context={'pl':pl}
    return render(request,'wood.html',context)

def niche_view(request):
    pl=Niche_product.objects.all()
    context={'pl':pl}
    return render(request,'niche.html',context)

def skincare_view(request):
    pl=Skincare_product.objects.all()
    context={'pl':pl}
    return render(request,'skincare.html',context)

def makeup_view(request):
    pl=Makeup_product.objects.all()
    context={'pl':pl}
    return render(request,'makeup.html',context)

def haircare_view(request):
    pl=Haircare_product.objects.all()
    context={'pl':pl}
    return render(request,'haircare.html',context)

def nailcare_view(request):
    pl=Nailcare_product.objects.all()
    context={'pl':pl}
    return render(request,'nailcare.html',context)

def fragnance_view(request):
    pl=Fragnance_product.objects.all()
    context={'pl':pl}
    return render(request,'fragnance.html',context)

def organic_view(request):
    pl=Organic_product.objects.all()
    context={'pl':pl}
    return render(request,'organic.html',context)

def mature_view(request):
    pl=Mature_product.objects.all()
    context={'pl':pl}
    return render(request,'mature.html',context)

def suncare_view(request):
    pl=Suncare_product.objects.all()
    context={'pl':pl}
    return render(request,'suncare.html',context)

def lip_view(request):
    pl=Lipcare_product.objects.all()
    context={'pl':pl}
    return render(request,'lip.html',context)

def hair_view(request):
    pl=Hairdye_product.objects.all()
    context={'pl':pl}
    return render(request,'hair.html',context)

def handgun_view(request):
    pl=Handgun_product.objects.all()
    context={'pl':pl}
    return render(request,'handgun.html',context)

def sniper_view(request):
    pl=Sniper_product.objects.all()
    context={'pl':pl}
    return render(request,'sniper.html',context)

def shotgun_view(request):
    pl=Shotgun_product.objects.all()
    context={'pl':pl}
    return render(request,'shotgun.html',context)

def dagger_view(request):
    pl=Dagger_product.objects.all()
    context={'pl':pl}
    return render(request,'daggers.html',context)

def bows_view(request):
    pl=Bows_product.objects.all()
    context={'pl':pl}
    return render(request,'bows.html',context)

def nunchaku_view(request):
    pl=Nunchaku_product.objects.all()
    context={'pl':pl}
    return render(request,'nunchaku.html',context)

def katana_view(request):
    pl=Katana_product.objects.all()
    context={'pl':pl}
    return render(request,'katana.html',context)

def war_view(request):
    pl=Warhammer_product.objects.all()
    context={'pl':pl}
    return render(request,'war.html',context)

def stun_view(request):
    pl=Stungun_product.objects.all()
    context={'pl':pl}
    return render(request,'stun.html',context)

def whips_view(request):
    pl=Whips_product.objects.all()
    context={'pl':pl}
    return render(request,'whips.html',context)

def jewelery_view(request):
    pl=Jewelery_product.objects.all()
    context={'pl':pl}
    return render(request,'jewelery.html',context)

def watch_view(request):
    pl=Watch_product.objects.all()
    context={'pl':pl}
    return render(request,'watch.html',context)

def hats_view(request):
    pl=Hats_product.objects.all()
    context={'pl':pl}
    return render(request,'hats.html',context)

def eyewear_view(request):
    pl=Eyewear_product.objects.all()
    context={'pl':pl}
    return render(request,'eyewear.html',context)

def scarves_view(request):
    pl=Scarves_product.objects.all()
    context={'pl':pl}
    return render(request,'scarves.html',context)

def handbags_view(request):
    pl=Handbag_product.objects.all()
    context={'pl':pl}
    return render(request,'handbags.html',context)

def belts_view(request):
    pl=Belts_product.objects.all()
    context={'pl':pl}
    return render(request,'belts.html',context)

def mittens_view(request):
    pl=Mittens_product.objects.all()
    context={'pl':pl}
    return render(request,'mittens.html',context)

def haira_view(request):
    pl=HairAccessories_product.objects.all()
    context={'pl':pl}
    return render(request,'haira.html',context)

def socks_view(request):
    pl=Socks_product.objects.all()
    context={'pl':pl}
    return render(request,'socks.html',context)



from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'userform.html', context)

    
    

from django.contrib.auth import authenticate,login,logout

def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request, username=uname, password=passw)

        if user is not None:
            request.session["uid"] = user.id
            login(request, user)
            return redirect("/")

    else:
        return render(request, "login.html")




def logout_view(request):
    logout(request)
    return redirect("/")
    


from django.contrib.auth.models import User



def shirt_cart(request,p_name):
    shirt=Shirts_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,shirt=shirt).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.shirt=shirt
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


















def kudta_cart(request,p_name):
    kudta=Kudta_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,kudta=kudta).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.kudta=kudta
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def oversize_cart(request,p_name):
    oversize=Oversize_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,oversize=oversize).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.oversize=oversize
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def sweatb_cart(request,p_name):
    sweatb=Sweatshirt_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,sweatb=sweatb)

    if existing_cart_item:
        existing_cart_item.quantity +=1
        existing_cart_item.save()
    else:
        c=Cart()
        c.sweatb=sweatb
        c.user=user
        c.quantity=1
        c.save()
    return redirect('/cartlist')



def hoodiesb_cart(request,p_name):
    hoodiesb=Hoodies_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,hoodiesb=hoodiesb).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.hoodiesb=hoodiesb
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def shervani_cart(request,p_name):
    shervani=Shervani_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,shervani=shervani).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.shervani=shervani
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def jacket_cart(request,p_name):
    jacket=Jacket_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,jacket=jacket).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.jacket=jacket
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def jeans_cart(request,p_name):
    jeans=Jeans_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,jeans=jeans).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.jeans=jeans
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def shortsb_cart(request,p_name):
    shortsb=Shorts_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,shortsb=shortsb).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.shortsb=shortsb
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def chinos_cart(request,p_name):
    chinosb=Chinos_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,chinosb=chinosb).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.chinosb=chinosb
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')







def joggerb_cart(request,p_name):
    joggerb=Joggers_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,joggerb=joggerb).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.joggerb=joggerb
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def cordouary_cart(request,p_name):
    cordouary=Cordouary_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,cordouary=cordouary).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.cordouary=cordouary
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def cargo_cart(request,p_name):
    cargo=Cargos_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,cargo=cargo).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.cargo=cargo
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def sweatpants_cart(request,p_name):
    sweatp=Sweatpants_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,sweatp=sweatp).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.sweatp=sweatp
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def tshirt_cart(request,p_name):
    tshirt=Tshirts_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,tshirt=tshirt).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.tshirt=tshirt
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def hoodiesg_cart(request,p_name):
    hoodiesg=Hoodiesg_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,hoodiesg=hoodiesg).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.hoodiesg=hoodiesg
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def tank_cart(request,p_name):
    tank=Tank_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,tank=tank).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.tank=tank
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def peplum_cart(request,p_name):
    peplum=Peplum_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,peplum=peplum).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.peplum=peplum
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')







def crop_cart(request,p_name):
    crop=Croptops_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,crop=crop).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.crop=crop
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def cardigan_cart(request,p_name):
    cardigan=Cardigan_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,cardigan=cardigan).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.cardigan=cardigan
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def tube_cart(request,p_name):
    tube=Tubetops_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,tube=tube).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.tube=tube
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def jeansg_cart(request,p_name):
    jeansg=Jeansg_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,jeansg=jeansg).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.jeansg=jeansg
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def shortsg_cart(request,p_name):
    shortsg=Shortsg_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,shortsg=shortsg).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.shortsg=shortsg
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def trouser_cart(request,p_name):
    trouser=Trouser_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,trouser=trouser).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.trouser=trouser
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def skirt_cart(request,p_name):
    skirt=Skirts_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,skirt=skirt).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.skirt=skirt
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def joggerg_cart(request,p_name):
    joggerg=Joggerg_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,joggerg=joggerg).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.joggerg=joggerg
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def chinosg_cart(request,p_name):
    chinosg=Chinosg_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,chinosg=chinosg).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.chinosg=chinosg
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def flarepants_cart(request,p_name):
    flarepants=Flarepants_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,flarepants=flarepants).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.flarepants=flarepants
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def phone_cart(request,p_name):
    phone=Phones_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,phone=phone).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.phone=phone
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def swatch_cart(request,p_name):
    swatch=Swatch_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,swatch=swatch).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.swatch=swatch
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def airpods_cart(request,p_name):
    airpod=Airpods_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,airpod=airpod).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.airpod=airpod
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def mwave_cart(request,p_name):
    mwave=Mwave_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,mwave=mwave).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.mwave=mwave
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def camera_cart(request,p_name):
    camera=Camera_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,camera=camera).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.camera=camera
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def tv_cart(request,p_name):
    tv=TV_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,tv=tv).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.tv=tv
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def light_cart(request,p_name):
    light=Light_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,light=light).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.light=light
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def fans_cart(request,p_name):
    fan=Fans_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,fan=fan).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.fan=fan
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def charger_cart(request,p_name):
    charger=Charger_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,charger=charger).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.charger=charger
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')


def vc_cart(request,p_name):
    vc=VC_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,vc=vc).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.vc=vc
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def dumbell_cart(request,p_name):
    dumbell=Dumbell_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,dumbell=dumbell).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.dumbell=dumbell
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def bar_cart(request,p_name):
    bar=Bars_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,bar=bar).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.bar=bar
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def hgrip_cart(request,p_name):
    hgrip=Hgrip_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,hgrip=hgrip).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.hgrip=hgrip
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def creatine_cart(request,p_name):
    creatine=Creatine_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,creatine=creatine).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.creatine=creatine
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def protien_cart(request,p_name):
    protien=Protien_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,protien=protien).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.protien=protien
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def gbag_cart(request,p_name):
    gbag=Gbag_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,gbag=gbag).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.gbag=gbag
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def towel_cart(request,p_name):
    towel=Towels_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,towel=towel).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.towel=towel
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def shoes_cart(request,p_name):
    shoes=Shoes_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,shoes=shoes).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.shoes=shoes
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def matt_cart(request,p_name):
    matt=Matts_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,matt=matt).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.matt=matt
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def wmachine_cart(request,p_name):
    wmachine=Wmachine_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,wmachine=wmachine).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.wmachine=wmachine
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def pen_cart(request,p_name):
    pen=Pens_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,pen=pen).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.pen=pen
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def pencil_cart(request,p_name):
    pencil=Pencils_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,pencil=pencil).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.pencil=pencil
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def pouch_cart(request,p_name):
    pouch=Pouch_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,pouch=pouch).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.pouch=pouch
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def lbox_cart(request,p_name):
    lbox=Lbox_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,lbox=lbox).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.lbox=lbox
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def sanitizer_cart(request,p_name):
    sanitizer=Sanitizer_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,sanitizer=sanitizer).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.sanitizer=sanitizer
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def sbag_cart(request,p_name):
    sbag=Sbags_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,sbag=sbag).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.sbag=sbag
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def wallet_cart(request,p_name):
    wallet=Wallets_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,wallet=wallet).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.wallet=wallet
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def umbrella_cart(request,p_name):
    umbrella=Umbrella_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,umbrella=umbrella).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.umbrella=umbrella
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def notebook_cart(request,p_name):
    note=Note_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,note=note).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.note=note
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def wbottle_cart(request,p_name):
    wbottle=Wbottle_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,wbottle=wbottle).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.wbottle=wbottle
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def novel_cart(request,p_name):
    novel=Novel_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,novel=novel).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.novel=novel
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def sstories_cart(request,p_name):
    sstories=Sstories_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,sstories=sstories).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.sstories=sstories
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def thriller_cart(request,p_name):
    thriller=Thriller_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,thriller=thriller).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.thriller=thriller
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def romance_cart(request,p_name):
    romance=Romance_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,romance=romance).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.romance=romance
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def fantasy_cart(request,p_name):
    fantasy=Fantasy_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,fantasy=fantasy).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.fantasy=fantasy
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def historical_cart(request,p_name):
    historical=Historical_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,historical=historical).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.historical=historical
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def cook_cart(request,p_name):
    cook=Cook_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,cook=cook).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.cook=cook
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def drama_cart(request,p_name):
    drama=Drama_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,drama=drama).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.drama=drama
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def self_cart(request,p_name):
    help=Self_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,help=help).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.help=help
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def travel_cart(request,p_name):
    travel=Travel_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,travel=travel).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.travel=travel
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def eauf_cart(request,p_name):
    eauf=Eauf_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,eauf=eauf).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.eauf=eauf
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def eaud_cart(request,p_name):
    eaud=Eaud_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,eaud=eaud).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.eaud=eaud
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def oil_cart(request,p_name):
    oil=Oil_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,oil=oil).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.oil=oil
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def solid_cart(request,p_name):
    solid=Solid_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,solid=solid).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.solid=solid
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def splash_cart(request,p_name):
    splash=Splash_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,splash=splash).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.splash=splash
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def neutral_cart(request,p_name):
    neutral=Neutral_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,neutral=neutral).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.neutral=neutral
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def seasonal_cart(request,p_name):
    seasonal=Seasonal_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,seasonal=seasonal).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.seasonal=seasonal
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def gourmand_cart(request,p_name):
    gourmand=Gourmand_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,gourmand=gourmand).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.gourmand=gourmand
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def wood_cart(request,p_name):
    wood=Wood_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,wood=wood).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.wood=wood
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')



def niche_cart(request,p_name):
    niche=Niche_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,niche=niche).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.niche=niche
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def skincare_cart(request,p_name):
    skincare=Skincare_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,skincare=skincare).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.skincare=skincare
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def makeup_cart(request,p_name):
    makeup=Makeup_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,makeup=makeup).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.makeup=makeup
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def haircare_cart(request,p_name):
    haircare=Haircare_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,haircare=haircare).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.haircare=haircare
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def nailcare_cart(request,p_name):
    nailcare=Nailcare_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,nailcare=nailcare).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.nailcare=nailcare
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def fragnance_cart(request,p_name):
    fragnance=Fragnance_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,fragnance=fragnance).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.fragnance=fragnance
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def organic_cart(request,p_name):
    organic=Organic_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,organic=organic).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.organic=organic
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def mature_cart(request,p_name):
    mature=Mature_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,mature=mature).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.mature=mature
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def suncare_cart(request,p_name):
    suncare=Suncare_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,suncare=suncare).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.suncare=suncare
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')




def lipcare_cart(request,p_name):
    lipcare=Lipcare_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,lipcare=lipcare).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.lipcare=lipcare
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def hairdye_cart(request,p_name):
    hairdye=Hairdye_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,hairdye=hairdye).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.hairdye=hairdye
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def handgun_cart(request,p_name):
    handgun=Handgun_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,handgun=handgun).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.handgun=handgun
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def sniper_cart(request,p_name):
    sniper=Sniper_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,sniper=sniper).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.sniper=sniper
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def shotgun_cart(request,p_name):
    shotgun=Shotgun_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,shotgun=shotgun).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.shotgun=shotgun
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def dagger_cart(request,p_name):
    dagger=Dagger_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,dagger=dagger).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.dagger=dagger
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def bows_cart(request,p_name):
    bow=Bows_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,bow=bow).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.bow=bow
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def nunchaku_cart(request,p_name):
    nunchaku=Nunchaku_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,nunchaku=nunchaku).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.nunchaku=nunchaku
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def katana_cart(request,p_name):
    katana=Katana_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,katana=katana).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.katana=katana
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def warhammer_cart(request,p_name):
    warhammer=Warhammer_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,warhammer=warhammer).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.warhammer=warhammer
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def stungun_cart(request,p_name):
    stungun=Stungun_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,stungun=stungun).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.stungun=stungun
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')






def whips_cart(request,p_name):
    whips=Whips_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,whips=whips).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.whips=whips
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def jewelery_cart(request,p_name):
    jewelery=Jewelery_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,jewelery=jewelery).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.jewelery=jewelery
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def watch_cart(request,p_name):
    watch=Watch_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,watch=watch).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.watch=watch
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def hats_cart(request,p_name):
    hats=Hats_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,hats=hats).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.hats=hats
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def eyewear_cart(request,p_name):
    eyewear=Eyewear_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,eyewear=eyewear).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.eyewear=eyewear
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def scarves_cart(request,p_name):
    scarves=Scarves_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,scarves=scarves).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.scarves=scarves
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def handbag_cart(request,p_name):
    handbag=Handbag_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,handbag=handbag).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.handbag=handbag
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def belts_cart(request,p_name):
    belts=Belts_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,belts=belts).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.belts=belts
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def mittens_cart(request,p_name):
    mittens=Mittens_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,mittens=mittens).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.mittens=mittens
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def haira_cart(request,p_name):
    haira=HairAccessories_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,haira=haira).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.haira=haira
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')





def socks_cart(request,p_name):
    socks=Socks_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,socks=socks).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        c=Cart()
        c.socks=socks
        c.user=user
        c.quantity = 1
        c.save()
    return redirect('/cartlist')

def most_cart(request,p_name):
    product=Product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,product=product).first()

    if existing_cart_item:
        existing_cart_item.quantity +=1
        existing_cart_item.save()
    else:
        c=Cart()
        c.product=product
        c.user=user
        c.quantity =1
        c.save()
    return redirect('/cartlist')


def trending_cart(request,p_name):
    tcart=Trending_product.objects.get(p_name=p_name)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    existing_cart_item=Cart.objects.filter(user=user,tcart=tcart).first()

    if existing_cart_item:
        existing_cart_item.quantity +=1
        existing_cart_item.save()
    else:
        c=Cart()
        c.tcart=tcart
        c.user=user
        c.quantity =1
        c.save()
    return redirect('/cartlist')

























def cartlist_view(request):
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    clist = Cart.objects.filter(user=user)

    total_cart_price = 0 
    
    selected_product=clist.first()


    for item in clist:
        shirt=item.shirt
        kudta = item.kudta
        oversize = item.oversize
        sweatb = item.sweatb
        hoodiesb = item.hoodiesb
        shervani = item.shervani
        jacket=item.jacket
        jeans=item.jeans
        shortsb=item.shortsb
        cargo=item.cargo
        chinosb=item.chinosb
        joggerb=item.joggerb
        cordouary=item.cordouary
        sweatp=item.sweatp
        tshirt=item.tshirt
        hoodiesg=item.hoodiesg
        tank=item.tank
        peplum=item.peplum
        crop=item.crop
        cardigan=item.cardigan
        tube=item.tube
        jeansg=item.jeansg
        shortsg=item.shortsg
        trouser=item.trouser
        skirt=item.skirt
        joggerg=item.joggerg
        chinosg=item.chinosg
        flarepants=item.flarepants
        phone=item.phone
        swatch=item.swatch
        airpod=item.airpod
        mwave=item.mwave
        camera=item.camera
        tv=item.tv
        light=item.light
        fan=item.fan
        charger=item.charger
        vc=item.vc
        dumbell=item.dumbell
        bar=item.bar
        hgrip=item.hgrip
        creatine=item.creatine
        protien=item.protien
        gbag=item.gbag
        towel=item.towel
        shoes=item.shoes
        matt=item.matt
        wmachine=item.wmachine
        pen=item.pen
        pencil=item.pencil
        pouch=item.pouch
        lbox=item.lbox
        sanitizer=item.sanitizer
        sbag=item.sbag
        wallet=item.wallet
        umbrella=item.umbrella
        note=item.note
        wbottle=item.wbottle
        novel=item.novel
        sstories=item.sstories
        thriller=item.thriller
        romance=item.romance
        fantasy=item.fantasy
        historical=item.historical
        cook=item.cook
        drama=item.drama
        help=item.help
        travel=item.travel
        eauf=item.eauf
        eaud=item.eaud
        oil=item.oil
        solid=item.solid
        splash=item.splash
        neutral=item.neutral
        seasonal=item.seasonal
        gourmand=item.gourmand
        wood=item.wood
        niche=item.niche
        skincare=item.skincare
        makeup=item.makeup
        haircare=item.haircare
        nailcare=item.nailcare
        fragnance=item.fragnance
        organic=item.organic
        mature=item.mature
        suncare=item.suncare
        lipcare=item.lipcare
        hairdye=item.hairdye
        handgun=item.handgun
        sniper=item.sniper
        shotgun=item.shotgun
        dagger=item.dagger
        bow=item.bow
        nunchaku=item.nunchaku
        katana=item.katana
        warhammer=item.warhammer
        stungun=item.stungun
        whips=item.whips
        jewelery=item.jewelery
        watch=item.watch
        hats=item.hats
        eyewear=item.eyewear
        scarves=item.scarves
        handbag=item.handbag
        belts=item.belts
        mittens=item.mittens
        haira=item.haira
        socks=item.socks
        product=item.product
        tcart=item.tcart
        
        
        if shirt:
            price=item.shirt.price
        elif kudta:
            price = item.kudta.price
        elif oversize:
            price = item.oversize.price
        elif sweatb:
            price = item.sweatb.price
        elif hoodiesb:
            price = item.hoodiesb.price
        elif shervani:
            price = item.shervani.price
        elif jacket:
            price=item.jacket.price
        elif jeans:
            price=item.jeans.price
        elif shortsb:
            price=item.shortsb.price
        elif cargo:
            price=item.cargo.price
        elif chinosb:
            price=item.chinosb.price
        elif joggerb:
            price=item.joggerb.price
        elif cordouary:
            price=item.cordouary.price
        elif sweatp:
            price=item.sweatp.price
        elif tshirt:
            price=item.tshirt.price
        elif hoodiesg:
            price=item.hoodiesg.price
        elif tank:
            price=item.tank.price
        elif peplum:
            price=item.peplum.price
        elif crop:
            price=item.crop.price
        elif cardigan:
            price=item.cardigan.price
        elif tube:
            price=item.tube.price
        elif jeansg:
            price=item.jeansg.price
        elif shortsg:
            price=item.shortsg.price
        elif trouser:
            price=item.trouser.price
        elif skirt:
            price=item.skirt.price
        elif joggerg:
            price=item.joggerg.price
        elif chinosg:
            price=item.chinosg.price
        elif flarepants:
            price=item.flarepants.price
        elif phone:
            price=item.phone.price
        elif swatch:
            price=item.swatch.price
        elif airpod:
            price=item.airpod.price
        elif mwave:
            price=item.mwave.price
        elif camera:
            price=item.camera.price
        elif tv:
            price=item.tv.price
        elif light:
            price=item.light.price
        elif fan:
            price=item.fan.price
        elif charger:
            price=item.charger.price
        elif vc:
            price=item.vc.price
        elif dumbell:
            price=item.dumbell.price
        elif bar:
            price=item.bar.price
        elif hgrip:
            price=item.hgrip.price
        elif creatine:
            price=item.creatine.price
        elif protien:
            price=item.protien.price
        elif gbag:
            price=item.gbag.price
        elif towel:
            price=item.towel.price
        elif shoes:
            price=item.shoes.price
        elif matt:
            price=item.matt.price
        elif wmachine:
            price=item.wmachine.price
        elif pen:
            price=item.pen.price
        elif pencil:
            price=item.pencil.price
        elif pouch:
            price=item.pouch.price
        elif lbox:
            price=item.lbox.price
        elif sanitizer:
            price=item.sanitizer.price
        elif sbag:
            price=item.sbag.price
        elif wallet:
            price=item.wallet.price
        elif umbrella:
            price=item.umbrella.price
        elif note:
            price=item.note.price
        elif wbottle:
            price=item.wbottle.price
        elif novel:
            price=item.novel.price
        elif sstories:
            price=item.sstories.price
        elif thriller:
            price=item.thriller.price
        elif romance:
            price=item.romance.price
        elif fantasy:
            price=item.fantasy.price
        elif historical:
            price=item.historical.price
        elif cook:
            price=item.cook.price
        elif drama:
            price=item.drama.price
        elif help:
            price=item.help.price
        elif travel:
            price=item.travel.price
        elif eauf:
            price=item.eauf.price
        elif eaud:
            price=item.eaud.price
        elif oil:
            price=item.oil.price
        elif solid:
            price=item.solid.price
        elif splash:
            price=item.splash.price
        elif neutral:
            price=item.neutral.price
        elif seasonal:
            price=item.seasonal.price
        elif gourmand:
            price=item.gourmand.price
        elif wood:
            price=item.wood.price
        elif niche:
            price=item.niche.price
        elif skincare:
            price=item.skincare.price
        elif makeup:
            price=item.makeup.price
        elif haircare:
            price=item.haircare.price
        elif nailcare:
            price=item.nailcare.price
        elif fragnance:
            price=item.fragnance.price
        elif organic:
            price=item.organic.price
        elif mature:
            price=item.mature.price
        elif suncare:
            price=item.suncare.price
        elif lipcare:
            price=item.lipcare.price
        elif hairdye:
            price=item.hairdye.price
        elif handgun:
            price=item.handgun.price
        elif sniper:
            price=item.sniper.price
        elif shotgun:
            price=item.shotgun.price
        elif dagger:
            price=item.daagger.price
        elif bow:
            price=item.bow.price
        elif nunchaku:
            price=item.nunchaku.price
        elif katana:
            price=item.katana.price
        elif warhammer:
            price=item.warhammer.price
        elif stungun:
            price=item.stungun.price
        elif whips:
            price=item.whips.price
        elif jewelery:
            price=item.jewelery.price
        elif watch:
            price=item.watch.price
        elif hats:
            price=item.hats.price
        elif eyewear:
            price=item.eyewear.price
        elif scarves:
            price=item.scarves.price
        elif handbag:
            price=item.handbag.price
        elif belts:
            price=item.belts.price
        elif mittens:
            price=item.mittens.price
        elif haira:
            price=item.haira.price
        elif socks:
            price=item.socks.price
        elif product:
            price=item.product.price
        elif tcart:
            price=item.tcart.price
        


        
        
        
        
        
        

            
        item.individual_price = item.quantity * price
        item.save()

        total_cart_price += item.individual_price

    context = {'clist': clist, 'total_price': total_cart_price,'selected_product': selected_product,'user':user}
    return render(request, 'cart-list.html', context)



def update_quantity(request, cid, action):
    item = Cart.objects.get(id=cid)
    
    if action == 'plus':
        item.quantity += 1
        item.save()
    elif action == 'minus' and item.quantity > 0:
        item.quantity -= 1
        if item.quantity == 0:
            item.delete()
        else:
            item.save()

    return redirect('/cartlist')     

# from .models import Buy
# from django.views.decorators.csrf import csrf_exempt
# import razorpay


# def payment_page(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         amount=int(request.POST.get('amount'))
#         client=razorpay.Client(auth=('rzp_test_uA6HF2ESxryOb6','pMHUyp9nbFIf68yEKqcnCPYy'))
#         payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})

#         print(payment)

#         buy=Buy(name=name,amount=amount,payment_id=payment['id'])
#         buy.save()

#         return render(request,'payment_page.html')
#     else:
#         return render(request,'payment_page.html')

        


# @csrf_exempt
# def success_view(request):
#     if request.method=="POST":
#         a=request.POST
#         print(a)
#         order_id=''
#         for key,val in a.items():
#             if key=='razorpay_order_id':
#                 order_id=val
#                 break
#         user=Buy.objects.filter(payment_id=order_id).first()
#         user.paid=True
#         user.save()
#         return render(request,'success.html')
#     else:
#         return render(request,'success.html')

def payment_page(request):
    return render(request,'payment_page.html')

def success_view(request):
    return render(request, 'success_template.html')




# views.py


# from django.shortcuts import render


# def search_view(request):
#     query = request.GET.get('q', '')

#     # List of models to include in the search
#     search_models = [Product, Trending_product, Airpods_product,Shirts_product,Kudta_product,Oversize_product,Sweatshirt_product,Hoodies_product,Shervani_product,Jacket_product,Jeans_product,Shorts_product,Cargos_product,Chinos_product,Joggers_product,Cordouary_product,Sweatpants_product,Tshirts_product,Hoodiesg_product,Tank_product,Peplum_product,Croptops_product,Cardigan_product,Tubetops_product,Jeansg_product,Shortsg_product,Trouser_product,Skirts_product,Joggerg_product,Chinosg_product,Flarepants_product,Phones_product,Swatch_product,Airpods_product,Mwave_product,Camera_product,TV_product,Light_product,Fans_product,Charger_product,VC_product,Dumbell_product,Bars_product,Hgrip_product,Creatine_product,Protien_product,Gbag_product,Towels_product,Shoes_product,Matts_product,Wmachine_product,Pens_product,Pencils_product,Pouch_product,Lbox_product,Sanitizer_product,Sbags_product,Wallets_product,Umbrella_product,Note_product,Wbottle_product,Novel_product,Sstories_product,Thriller_product,Romance_product,Fantasy_product,Historical_product,Cook_product,Drama_product,Self_product,Travel_product,Eauf_product,Eaud_product,Oil_product,Solid_product,Splash_product,Neutral_product,Seasonal_product,Gourmand_product,Wood_product,Niche_product,Skincare_product,Makeup_product,Haircare_product,Nailcare_product,Fragnance_product,Organic_product,Mature_product,Suncare_product,Lipcare_product,Hairdye_product,Handgun_product,Sniper_product,Shotgun_product,Dagger_product,Bows_product,Nunchaku_product,Katana_product,Warhammer_product,Stungun_product,Whips_product,Jewelery_product,Watch_product,Hats_product,Eyewear_product,Scarves_product,Handbag_product,Belts_product,Mittens_product,HairAccessories_product,Socks_product]

#     # Perform a query that spans multiple models using Q objects
#     results = []
#     for model in search_models:
#         results.extend(model.objects.filter(p_name__icontains=query))

#     context = {'results': results, 'query': query}
#     return render(request, 'search_results.html', context)



from django.db.models import Q
def search_view(request):
    query = request.GET.get('q')

    # Search across multiple models using Q objects
    all_products_list = []
    if query:
        all_products_list += Product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Trending_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Airpods_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Shirts_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Kudta_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Oversize_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Sweatshirt_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Hoodies_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Shervani_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Jacket_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Jeans_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Shorts_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Cargos_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Tank_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Peplum_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Croptops_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Cardigan_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Tubetops_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Jeansg_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Shortsg_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Trouser_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Skirts_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Joggerg_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Joggerg_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Flarepants_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Phones_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Swatch_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Airpods_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Mwave_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Camera_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Camera_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += TV_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Light_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Fans_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Charger_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += VC_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Dumbell_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Bars_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Hgrip_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Creatine_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Protien_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Gbag_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Towels_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Shoes_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Matts_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Wmachine_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Pens_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Pencils_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Pouch_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Lbox_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Sanitizer_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Sbags_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Wallets_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Umbrella_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Note_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Wbottle_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Novel_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Sstories_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Thriller_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Romance_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Fantasy_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Historical_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Cook_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Drama_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Self_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Travel_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Eauf_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Eaud_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Oil_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Solid_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Splash_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Neutral_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Seasonal_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Gourmand_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Wood_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Niche_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Skincare_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Makeup_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Haircare_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Nailcare_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Fragnance_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Organic_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Mature_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Suncare_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Lipcare_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Hairdye_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Handgun_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Sniper_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Shotgun_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Dagger_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Bows_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Nunchaku_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Katana_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Warhammer_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Stungun_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Whips_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Jewelery_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Watch_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Hats_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Eyewear_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Scarves_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Handbag_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Belts_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Mittens_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += HairAccessories_product.objects.filter(Q(p_name__icontains=query))
        all_products_list += Socks_product.objects.filter(Q(p_name__icontains=query))

    context = {'all_products_list': all_products_list, 'query': query}
    return render(request, 'all/search_results.html', context)






def buy_all(request):
    # Retrieve all products in the user's cart
    user_cart = Cart.objects.filter(user=request.user)
    # Create an order for all products in the cart
    order = Order.objects.create(user=request.user)
    total_price = 0
    
    for item in user_cart:
        # Determine the type of product in the cart and get the respective product name and price
        shirt=item.shirt
        kudta = item.kudta
        oversize = item.oversize
        sweatb = item.sweatb
        hoodiesb = item.hoodiesb
        shervani = item.shervani
        jacket=item.jacket
        jeans=item.jeans
        shortsb=item.shortsb
        cargo=item.cargo
        chinosb=item.chinosb
        joggerb=item.joggerb
        cordouary=item.cordouary
        sweatp=item.sweatp
        tshirt=item.tshirt
        hoodiesg=item.hoodiesg
        tank=item.tank
        peplum=item.peplum
        crop=item.crop
        cardigan=item.cardigan
        tube=item.tube
        jeansg=item.jeansg
        shortsg=item.shortsg
        trouser=item.trouser
        skirt=item.skirt
        joggerg=item.joggerg
        chinosg=item.chinosg
        flarepants=item.flarepants
        phone=item.phone
        swatch=item.swatch
        airpod=item.airpod
        mwave=item.mwave
        camera=item.camera
        tv=item.tv
        light=item.light
        fan=item.fan
        charger=item.charger
        vc=item.vc
        dumbell=item.dumbell
        bar=item.bar
        hgrip=item.hgrip
        creatine=item.creatine
        protien=item.protien
        gbag=item.gbag
        towel=item.towel
        shoes=item.shoes
        matt=item.matt
        wmachine=item.wmachine
        pen=item.pen
        pencil=item.pencil
        pouch=item.pouch
        lbox=item.lbox
        sanitizer=item.sanitizer
        sbag=item.sbag
        wallet=item.wallet
        umbrella=item.umbrella
        note=item.note
        wbottle=item.wbottle
        novel=item.novel
        sstories=item.sstories
        thriller=item.thriller
        romance=item.romance
        fantasy=item.fantasy
        historical=item.historical
        cook=item.cook
        drama=item.drama
        help=item.help
        travel=item.travel
        eauf=item.eauf
        eaud=item.eaud
        oil=item.oil
        solid=item.solid
        splash=item.splash
        neutral=item.neutral
        seasonal=item.seasonal
        gourmand=item.gourmand
        wood=item.wood
        niche=item.niche
        skincare=item.skincare
        makeup=item.makeup
        haircare=item.haircare
        nailcare=item.nailcare
        fragnance=item.fragnance
        organic=item.organic
        mature=item.mature
        suncare=item.suncare
        lipcare=item.lipcare
        hairdye=item.hairdye
        handgun=item.handgun
        sniper=item.sniper
        shotgun=item.shotgun
        dagger=item.dagger
        bow=item.bow
        nunchaku=item.nunchaku
        katana=item.katana
        warhammer=item.warhammer
        stungun=item.stungun
        whips=item.whips
        jewelery=item.jewelery
        watch=item.watch
        hats=item.hats
        eyewear=item.eyewear
        scarves=item.scarves
        handbag=item.handbag
        belts=item.belts
        mittens=item.mittens
        haira=item.haira
        socks=item.socks
        product=item.product
        tcart=item.tcart
        if shirt:
            price=item.shirt.price
            p_name=item.shirt.p_name
        elif kudta:
            price = item.kudta.price
            p_name=item.kudta.p_name
        elif oversize:
            price = item.oversize.price
            p_name=item.oversize.p_name
        elif sweatb:
            price = item.sweatb.price
            p_name= item.sweatb.p_name
        elif hoodiesb:
            price = item.hoodiesb.price
            p_name= item.hoodiesb.p_name
        elif shervani:
            price = item.shervani.price
            p_name= item.shervani.p_name
        elif jacket:
            price=item.jacket.price
            p_name= item.jacket.p_name
        elif jeans:
            price=item.jeans.price
            p_name=item.jeans.p_name
        elif shortsb:
            price=item.shortsb.price
            p_name=item.shortsb.p_name
        elif cargo:
            price=item.cargo.price
            p_name=item.cargo.p_name
        elif chinosb:
            price=item.chinosb.price
            p_name=item.chinosb.p_name
        elif joggerb:
            price=item.joggerb.price
            p_name=item.joggerb.p_name
        elif cordouary:
            price=item.cordouary.price
            p_name=item.cordouary.p_name
        elif sweatp:
            price=item.sweatp.price
            p_name=item.sweatp.p_name
        elif tshirt:
            price=item.tshirt.price
            p_name=item.tshirt.p_name
        elif hoodiesg:
            price=item.hoodiesg.price
            p_name=item.hoodiesg.p_name
        elif tank:
            price=item.tank.price
            p_name=item.tank.p_name
        elif peplum:
            price=item.peplum.price
            p_name=item.peplum.p_name
        elif crop:
            price=item.crop.price
            p_name=item.crop.p_name
        elif cardigan:
            price=item.cardigan.price
            p_name=item.cardigan.p_name
        elif tube:
            price=item.tube.price
            p_name=item.tube.p_name
        elif jeansg:
            price=item.jeansg.price
            p_name=item.jeansg.p_name
        elif shortsg:
            price=item.shortsg.price
            p_name=shortsg.p_name
        elif trouser:
            price=item.trouser.price
            p_name=item.trouser.p_name
        elif skirt:
            price=item.skirt.price
            p_name=item.skirt.p_name
        elif joggerg:
            price=item.joggerg.price
            p_name=item.joggerg.p_name
        elif chinosg:
            price=item.chinosg.price
            p_name=item.chinosg.p_name
        elif flarepants:
            price=item.flarepants.price
            p_name=item.flarepants.p_name
        elif phone:
            price=item.phone.price
            p_name=item.phone.p_name
        elif swatch:
            price=item.swatch.price
            p_name=item.swatch.p_name
        elif airpod:
            price=item.airpod.price
            p_name=item.airpod.p_name
        elif mwave:
            price=item.mwave.price
            p_name=item.mwave.p_name
        elif camera:
            price=item.camera.price
            p_name=item.camera.p_name
        elif tv:
            price=item.tv.price
            p_name=item.tv.p_name
        elif light:
            price=item.light.price
            p_name=item.light.p_name
        elif fan:
            price=item.fan.price
            p_name=item.fan.p_name
        elif charger:
            price=item.charger.price
            p_name=item.charger.p_name
        elif vc:
            price=item.vc.price
            p_name=item.vc.p_name
        elif dumbell:
            price=item.dumbell.price
            p_name=item.dumbell.p_name
        elif bar:
            price=item.bar.price
            p_name=item.bar.p_name
        elif hgrip:
            price=item.hgrip.price
            p_name=item.hgrip.p_name
        elif creatine:
            price=item.creatine.price
            p_name=item.creatine.p_name
        elif protien:
            price=item.protien.price
            p_name=item.protien.p_name
        elif gbag:
            price=item.gbag.price
            p_name=item.gbag.p_name
        elif towel:
            price=item.towel.price
            p_name=item.towel.p_name
        elif shoes:
            price=item.shoes.price
            p_name=item.shoes.p_name
        elif matt:
            price=item.matt.price
            p_name=item.matt.p_name
        elif wmachine:
            price=item.wmachine.price
            p_name=item.wmachine.p_name
        elif pen:
            price=item.pen.price
            p_name=item.pen.p_name
        elif pencil:
            price=item.pencil.price
            p_name=item.pencil.p_name
        elif pouch:
            price=item.pouch.price
            p_name=item.pouch.p_name
        elif lbox:
            price=item.lbox.price
            p_name=item.lbox.p_name
        elif sanitizer:
            price=item.sanitizer.price
            p_name=item.sanitizer.p_name
        elif sbag:
            price=item.sbag.price
            p_name=item.sbag.p_name
        elif wallet:
            price=item.wallet.price
            p_name=item.wallet.p_name
        elif umbrella:
            price=item.umbrella.price
            p_name=item.umbrella.p_name
        elif note:
            price=item.note.price
            p_name=item.note.p_name
        elif wbottle:
            price=item.wbottle.price
            p_name=item.wbottle.p_name
        elif novel:
            price=item.novel.price
            p_name=item.novel.p_name
        elif sstories:
            price=item.sstories.price
            p_name=item.sstories.p_name
        elif thriller:
            price=item.thriller.price
            p_name=item.thriller.p_name
        elif romance:
            price=item.romance.price
            p_name=item.romance.p_name
        elif fantasy:
            price=item.fantasy.price
            p_name=item.fantasy.p_name
        elif historical:
            price=item.historical.price
            p_name=item.historical.p_name
        elif cook:
            price=item.cook.price
            p_name=item.cook.p_name
        elif drama:
            price=item.drama.price
            p_name=item.drama.p_name
        elif help:
            price=item.help.price
            p_name=item.help.p_name
        elif travel:
            price=item.travel.price
            p_name=item.travel.p_name
        elif eauf:
            price=item.eauf.price
            p_name=item.eauf.p_name
        elif eaud:
            price=item.eaud.price
            p_name=item.eaud.p_name
        elif oil:
            price=item.oil.price
            p_name=item.oil.p_name
        elif solid:
            price=item.solid.price
            p_name=item.solid.p_name
        elif splash:
            price=item.splash.price
            p_name=item.splash.p_name
        elif neutral:
            price=item.neutral.price
            p_name=item.neutral.p_name
        elif seasonal:
            price=item.seasonal.price
            p_name=item.seasonal.p_name
        elif gourmand:
            price=item.gourmand.price
            p_name=item.gourmand.p_name
        elif wood:
            price=item.wood.price
            p_name=item.wood.p_name
        elif niche:
            price=item.niche.price
            p_name=item.niche.p_name
        elif skincare:
            price=item.skincare.price
            p_name=item.skincare.p_name
        elif makeup:
            price=item.makeup.price
            p_name=item.makeup.p_name
        elif haircare:
            price=item.haircare.price
            p_name=item.haircare.p_name
        elif nailcare:
            price=item.nailcare.price
            p_name=item.nailcare.p_name
        elif fragnance:
            price=item.fragnance.price
            p_name=item.fragnance.p_name
        elif organic:
            price=item.organic.price
            p_name=item.organic.p_name
        elif mature:
            price=item.mature.price
            p_name=item.mature.p_name
        elif suncare:
            price=item.suncare.price
            p_name=item.suncare.p_name
        elif lipcare:
            price=item.lipcare.price
            p_name=item.lipcare.p_name
        elif hairdye:
            price=item.hairdye.price
            p_name=item.hairdye.p_name
        elif handgun:
            price=item.handgun.price
            p_name=item.handgun.p_name
        elif sniper:
            price=item.sniper.price
            p_name=item.sniper.p_name
        elif shotgun:
            price=item.shotgun.price
            p_name=item.shotgun.p_name
        elif dagger:
            price=item.daagger.price
            p_name=item.dagger.p_name
        elif bow:
            price=item.bow.price
            p_name=item.bow.p_name
        elif nunchaku:
            price=item.nunchaku.price
            p_name=item.nunchaku.p_name
        elif katana:
            price=item.katana.price
            p_name=item.katana.p_name
        elif warhammer:
            price=item.warhammer.price
            p_name=item.warhammer.p_name
        elif stungun:
            price=item.stungun.price
            p_name=item.stungun.p_name
        elif whips:
            price=item.whips.price
            p_name=item.whips.p_name
        elif jewelery:
            price=item.jewelery.price
            p_name=item.jewelery.p_name
        elif watch:
            price=item.watch.price
            p_name=item.watch.p_name
        elif hats:
            price=item.hats.price
            p_name=item.hats.p_name
        elif eyewear:
            price=item.eyewear.price
            p_name=item.eyewear.p_name
        elif scarves:
            price=item.scarves.price
            p_name=item.scarves.p_name
        elif handbag:
            price=item.handbag.price
            p_name=item.handbag.p_name
        elif belts:
            price=item.belts.price
            p_name=item.belts.p_name
        elif mittens:
            price=item.mittens.price
            p_name=item.mittens.p_name
        elif haira:
            price=item.haira.price
            p_name=item.haira.p_name
        elif socks:
            price=item.socks.price
            p_name=item.socks.p_name
        elif product:
            price=item.product.price
            p_name=item.product.p_name
        elif tcart:
            price=item.tcart.price
            p_name=item.tcart.p_name
        else:
            # Handle the case when none of the product types are found
            p_name = "Unknown Product"
            price = 0  # Set a default price or handle accordingly

        item.delete()
    for cart_item in user_cart:
        # Create an order item for each product in the cart
        order_item = OrderItem.objects.create(
            order=order,
            product_name=p_name,  # Replace with appropriate field from Cart
            quantity=cart_item.quantity,
            price=price  # Replace with appropriate field from Cart
        )

        # Update the total price for the order
        total_price += order_item.price * order_item.quantity
        
    # Save the total price to the order
    order.total_price = total_price
    order.save()

    # Redirect to the checkout page with the order ID or display a confirmation
    order_items = OrderItem.objects.filter(order=order)  # Assuming 'order' is the specific Order object
    return render(request, 'checkout.html', {'order_id': order.id, 'order_total': order.total_price, 'order_items': order_items})





def checkout_confirm(request, order_id):
    # Make sure the user is authenticated
    if not request.user.is_authenticated:
        # Redirect to login or handle unauthenticated user as needed
        # Example: return HttpResponseRedirect('/login/')
        pass

    # Use get_object_or_404 to handle the case where the order doesn't exist
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip')

        order.billing_name = name
        order.billing_address = address
        order.billing_city = city
        order.billing_zip = zip_code
        order.save()

        # Additional order confirmation logic here

    context = {'order': order.items.all,'tp':order.total_price,'oi':order.id}
    return render(request, 'checkout_confirm.html', context)











