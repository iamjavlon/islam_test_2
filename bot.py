import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()
from bot.main import main

if __name__ == '__main__':
    main()