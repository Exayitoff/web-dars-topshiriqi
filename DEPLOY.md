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
2. `Static Site` emas, `Web Service` tanlang.
3. Avval `New +` > `PostgreSQL` yarating.
4. Keyin `New +` > `Web Service` yarating.
5. Quyidagilarni kiriting:
   Build Command: `bash build.sh`
   Start Command: `gunicorn config.wsgi:application`
6. Environment variables qo'shing:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=your-service-name.onrender.com`
   - `DJANGO_CSRF_TRUSTED_ORIGINS=https://your-service-name.onrender.com`
   - `DATABASE_URL` = Render PostgreSQL connection string
7. Deploy bo'lgach Render Shell ichida:
   `python manage.py createsuperuser`

## Muhim
- `.python-version` bilan Python `3.12.9` ga pin qilingan.
- `psycopg[binary]` Render uchun mos versiyaga yangilangan.
- Render avtomatik `RENDER_EXTERNAL_HOSTNAME` beradi, settings uni ham qabul qiladi.
- Static fayllar WhiteNoise orqali servis qilinadi.
- Migrations va collectstatic `build.sh` ichida bajariladi.

## Tekshiruv
- Admin: `https://your-service-name.onrender.com/admin/`
- Site: `https://your-service-name.onrender.com/`
