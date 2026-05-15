import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

# 1. بناء المسارات
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. تحميل متغيرات البيئة من .env
load_dotenv()

# 3. إعدادات الأمان
SECRET_KEY = os.getenv('SECRET_KEY')

# تأكد أن DEBUG تكون False في السيرفر و True في جهازك عبر ملف .env
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# السماح لجميع النطاقات في المرحلة الحالية
ALLOWED_HOSTS = ['*']

# أضف رابط موقعك هنا مع https://
CSRF_TRUSTED_ORIGINS = [
    'https://satisfied-curiosity-production-f8a2.up.railway.app',
]

# 4. تعريف التطبيقات
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App', # تطبيقك الخاص
]

# 5. الميدل وير (ترتيب WhiteNoise هنا ضروري جداً)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # تم التثبيت للتعامل مع الملفات الثابتة في الإنتاج
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AstroCode2026.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # مجلد القوالب العام
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AstroCode2026.wsgi.application'

# 6. قاعدة البيانات (الربط مع Neon باستخدام متغير البيئة DATABASE_URL)
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# 7. التحقق من كلمة المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 8. اللغة والوقت
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 9. الملفات الثابتة والوسائط (Production Ready)
STATIC_URL = 'static/'

# المجلد الرئيسي الذي يبحث فيه Django عن ملفات الـ CSS/JS الخاصة بتطبيقك أثناء التطوير
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# المجلد الذي ستجتمع فيه كل ملفات المشروع (بما فيها الـ Admin) عند عمل collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles' 

# إعدادات WhiteNoise لضغط وتخزين الملفات الثابتة بكفاءة
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ملفات الميديا (الرفع)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 10. إعدادات أخرى
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'App.Team'