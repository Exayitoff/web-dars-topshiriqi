# Web Lib Deployment

## Render orqali deploy

### Variant 1: render.yaml bilan
1. Loyihani GitHub'ga push qiling.
2. Render dashboard'da `New +` > `Blueprint` ni tanlang.
3. Repository'ni ulang.
4. `render.yaml` avtomatik o'qiladi va web service + PostgreSQL yaratiladi.
5. Deploy tugagach Render Shell ichida admin user yarating:
   `python manage.py createsuperuser`

### Variant 2: Manual deploy
1. GitHub repository'ni Render'ga ulang.
2. Avval `New +` > `PostgreSQL` yarating.
3. Keyin `New +` > `Web Service` yarating.
4. Quyidagilarni kiriting:
   Build Command: `bash build.sh`
   Start Command: `gunicorn config.wsgi:application`
5. Environment variables qo'shing:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=your-service-name.onrender.com`
   - `DJANGO_CSRF_TRUSTED_ORIGINS=https://your-service-name.onrender.com`
   - `DATABASE_URL` = Render PostgreSQL connection string
6. Deploy bo'lgach Render Shell ichida:
   `python manage.py createsuperuser`

## Tekshiruv
- Admin: `https://your-service-name.onrender.com/admin/`
- Site: `https://your-service-name.onrender.com/`

## Eslatma
- Render avtomatik `RENDER_EXTERNAL_HOSTNAME` beradi, settings uni ham qabul qiladi.
- Static fayllar WhiteNoise orqali servis qilinadi.
- Migrations va collectstatic `build.sh` ichida bajariladi.
