from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.bot.api.serializers import ProductSerializer
from src.bot.models import Product


@api_view(['GET'])
def get_products(request) -> Response:
	"""
	Return all of products for Telegram Bot
	:param request:
	:return:
	"""

	products = Product.objects.all()
	serializer = ProductSerializer(products, many=True)

	return Response(serializer.data)

# def registration(request):
# 	"""Метод регистрации"""
#
# 	context = {}
# 	if request.method == 'POST':
# 		username = request.POST.get('username', None)
# 		password = request.POST.get('password', None)
# 		email = request.POST.get('email', None)
# 		user = CustomUser.objects.create(username=username, email=email)
# 		user.set_password(password)
# 		user.save()
# 	return redirect(settings.LOGIN_URL)
#
#
# @login_required
# def account(request):
# 	context = {}
# 	customer_form = CustomerForm()
# 	context['customer_form'] = customer_form
# 	user_form = CustomUserForm()
# 	context['user_form'] = user_form
# 	return render(request, 'registration/my-account.html', context)
