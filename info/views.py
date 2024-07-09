from django.http import HttpResponse,JsonResponse,HttpRequest
from . models import Fruit,Basket,Owner
from django.db.models import F


# Create your views here.

def handleFruit(request, id=None):
    if request.method=='GET':
        manager=Fruit.objects.filter(expired_date=False).values()
        return JsonResponse({'fruits':list(manager)})
    if request.method=='POST':
        name = request.POST.get('name')
        expired_date = request .POST.get('expired_date')
        price = request.POST.get('price')
        owner = request.POST.get('owner')
        basket = request.POST.get('basket')

        if name is not None and expired_date is not None and price is not None:
            if id is not None:
                fruit = Fruit.objects.filter(id=id).first()

                if fruit is None:
                    return JsonResponse({
                        'message':'fruit is does not exist with id'
                    })
                
                fruit.name=name
                fruit.expired_date=expired_date
                fruit.price=price

                if owner is not None:
                    owner_manager = Owner.objects.filter(id=owner).first()
                    if owner_manager is not None:
                        fruit.owner = owner_manager
                    
                if basket is not None:
                    basket_manager = Basket.objects.filter(id=basket).first()
                    if basket_manager is not None:
                        fruit.basket = basket_manager

                fruit.save()

                return JsonResponse({
                    'message':'fruit is updated successfully'
                })
            
            fruit=Fruit()
            fruit.name=name
            fruit.expired_date=expired_date
            fruit.price=price
            if owner is not None:
                owner_manager = Owner.objects.filter(id=owner).first()
                if owner_manager is not None:
                    fruit.owner = owner_manager
                    
            if basket is not None:
                basket_manager = Basket.objects.filter(id=basket).first()
                if basket_manager is not None:
                    fruit.basket = basket_manager
            fruit.save()
            
            return JsonResponse({
                'message':'New fruit add successfully !!'
            })
        
        return JsonResponse({
            'message':'name,price,expired_date,owner or basket are required !'
        })



def handleBasket(request,id=None):
    if request.method=='GET':
        basket=Basket.objects.select_related('fruit').values()
        return JsonResponse({
            'baskets':list(basket)
        })
    
    if request.method=='POST':
        id = request.POST.get('id')
        name = request.POST.get('name') # GET from params and POST from body
        rating = request.POST.get('rating')
        items = request.POST.get('items')

        if name is not None and rating is not None and items is not None:
            if id is not None:
                basket = Basket.objects.filter(deleted=True).filter(pk=id).first()
                if basket is None:
                    return JsonResponse({
                        'message':f'basket is does exist with id{id}'
                    })
                basket.name = name
                basket.rating = rating
                basket.items = items
                basket.save()

            basket=Basket()
            basket.name=name
            basket.rating=rating
            basket.items=items
            basket.save()
            return JsonResponse({
                'message':'basket is add successful !!'
            })
            
        return JsonResponse ({
            'message':'name,rating and iteams are required !!'
        })
    
def handleOwner(request, id=None):
    if request.method=='GET':
        owner=Owner.objects.values()
        # Fruit.objects.filter(owner=1)
        return JsonResponse({
            'owner':list(owner)
        })
    if request.method=='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        shop_name = request.POST.get('shop_name')

        if name is not None and shop_name is not None:
            if id is not None:
                owner=Owner.objects.filter(id=id).values()

                if owner is None:
                    return JsonResponse({
                        'message':'owner is does not exist'
                    })
                owner.name=name
                owner.shop_name=shop_name
                owner.save()

            owner=Owner()
            owner.name=name
            owner.shop_name=shop_name
            owner.save()
            return JsonResponse({
                'message':'Owner is added successfully !!'
            })    
        
        return JsonResponse({
            'message':'name or shop name is required !'
        })


