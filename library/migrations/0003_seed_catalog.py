from django.db import migrations


def seed_catalog(apps, schema_editor):
    Genre = apps.get_model('library', 'Genre')
    Book = apps.get_model('library', 'Book')

    genres = [
        {'title': 'Dasturlash', 'slug': 'dasturlash', 'description': 'Frontend, backend, algoritmlar va software engineering bo‘yicha amaliy nashrlar.', 'display_order': 1},
        {'title': 'Ilmiy', 'slug': 'ilmiy', 'description': 'AI, matematika, biologiya va fizika bo‘yicha o‘rganishga qulay kitoblar jamlanmasi.', 'display_order': 2},
        {'title': 'Badiiy', 'slug': 'badiiy', 'description': 'Roman, hikoya, esse va she’riy asarlarni o‘z ichiga olgan boy tanlov.', 'display_order': 3},
        {'title': 'Tarix', 'slug': 'tarix', 'description': 'Markaziy Osiyo, jahon sivilizatsiyasi va muhim davrlar bo‘yicha nashrlar.', 'display_order': 4},
    ]

    genre_map = {}
    for item in genres:
        genre = Genre.objects.create(**item)
        genre_map[item['slug']] = genre

    books = [
        {
            'title': 'JavaScript Asoslari',
            'slug': 'javascript-asoslari',
            'author': 'A. Karimov',
            'genre': 'dasturlash',
            'description': 'Boshlovchilar uchun DOM, event va amaliy mashqlar asosidagi izchil qo‘llanma.',
            'summary': 'Frontend dasturlashni boshlash uchun DOM, event loop va API tushunchalarini qamrab oladi.',
            'image': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=900&q=80',
            'pages': 320,
            'level': 'Beginner',
            'year': 2026,
            'is_featured': True,
        },
        {
            'title': 'Python Dasturlash',
            'slug': 'python-dasturlash',
            'author': 'J. Aliyev',
            'genre': 'dasturlash',
            'description': 'Script yozish, avtomatlashtirish va backend asoslari uchun sodda, amaliy manba.',
            'summary': 'Python tilida dasturlash, fayllar bilan ishlash va backendga kirish uchun qulay manba.',
            'image': 'https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&w=900&q=80',
            'pages': 280,
            'level': 'Beginner',
            'year': 2025,
            'is_featured': False,
        },
        {
            'title': 'Sun’iy intellekt',
            'slug': 'suniy-intellekt',
            'author': 'D. Xasanov',
            'genre': 'ilmiy',
            'description': 'AI, neyron tarmoqlar va ma’lumotlar tahlili bo‘yicha amaliy izohlar.',
            'summary': 'AI tizimlari, ma’lumotlar tayyorlash va model baholash jarayonlari haqida to‘liq kirish.',
            'image': 'https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=900&q=80',
            'pages': 360,
            'level': 'Intermediate',
            'year': 2026,
            'is_featured': True,
        },
        {
            'title': 'O‘zbekiston tarixi',
            'slug': 'ozbekiston-tarixi',
            'author': 'R. Jo‘rayev',
            'genre': 'tarix',
            'description': 'Qadimgi davrdan mustaqillik yillarigacha bo‘lgan tarixiy jarayonlarni yoritadi.',
            'summary': 'Tarixiy manbalar, davrlar almashinuvi va muhim siyosiy jarayonlar sharhi.',
            'image': 'https://images.unsplash.com/photo-1463320726281-696a485928c7?auto=format&fit=crop&w=900&q=80',
            'pages': 410,
            'level': 'All levels',
            'year': 2024,
            'is_featured': False,
        },
        {
            'title': 'Badiiy adabiyot olami',
            'slug': 'badiiy-adabiyot-olami',
            'author': 'S. Rahmatov',
            'genre': 'badiiy',
            'description': 'Qissa, roman va hikoyalarning estetik qatlamini ochib beruvchi to‘plam.',
            'summary': 'Jahon va o‘zbek adabiyotidagi uslub, syujet va obrazlar tizimini sharhlaydi.',
            'image': 'https://images.unsplash.com/photo-1495446815901-a7297e633e8d?auto=format&fit=crop&w=900&q=80',
            'pages': 295,
            'level': 'All levels',
            'year': 2023,
            'is_featured': True,
        },
        {
            'title': 'Biologiya va hayot',
            'slug': 'biologiya-va-hayot',
            'author': 'N. Sobirova',
            'genre': 'ilmiy',
            'description': 'Tabiiy jarayonlar, hujayra tuzilishi va ekologik muvozanat haqidagi ommabop qo‘llanma.',
            'summary': 'Biologiya asoslari, ekologiya va zamonaviy ilmiy kuzatuvlarni birlashtiradi.',
            'image': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=900&q=80',
            'pages': 250,
            'level': 'Beginner',
            'year': 2025,
            'is_featured': False,
        },
    ]

    for item in books:
        Book.objects.create(
            title=item['title'],
            slug=item['slug'],
            author=item['author'],
            genre=genre_map[item['genre']],
            description=item['description'],
            summary=item['summary'],
            image=item['image'],
            pages=item['pages'],
            level=item['level'],
            year=item['year'],
            is_featured=item['is_featured'],
        )


def unseed_catalog(apps, schema_editor):
    Genre = apps.get_model('library', 'Genre')
    Book = apps.get_model('library', 'Book')
    Book.objects.all().delete()
    Genre.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0002_genre_book'),
    ]

    operations = [
        migrations.RunPython(seed_catalog, unseed_catalog),
    ]
