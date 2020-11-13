from recipes.models import Purchases, Favorites


def counter(request):
    if request.user.is_authenticated:
        counter = Purchases.objects.filter(user=request.user).count()
    else:
        counter = 0
    return {
        'counter': counter
    }


def purchases_id(request):
    if request.user.is_authenticated:
        purchases = Purchases.objects.filter(
            user=request.user).select_related('recipe').all()
        purchases_id = [i.recipe.id for i in purchases]
    else:
        purchases_id = []
    return {
        'purchases_id': purchases_id
    }


def favorites_id(request):
    if request.user.is_authenticated:
        favorites = Favorites.objects.filter(
            user=request.user).select_related('recipe').all()
        favorites_id = [i.recipe.id for i in favorites]
    else:
        favorites_id = []
    return {
        'favorites_id': favorites_id
    }