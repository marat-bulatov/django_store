from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': "Store",
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': "Store - Продукты",
    }

    return render(request, 'products/products.html', context)

def test_context(request):
    context = {
        'title': 'store',
        'header': 'Добро пожаловать!',
        'username': 'Иван Иванов',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090.00,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'name': 'Синяя куртка The North Face',
                'price': 23725.00,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390.00,
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий. '
            },
        ],
        'promotion': True,
        'products_of_promotion': [
            {
                'name': '12345 Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 11111.00,
                'description': '12345 Материал с плюшевой текстурой. Удобный и мягкий. '
            },
        ]
    }

    return render(request, 'products/test_context.html', context)