import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conectaif.settings")
django.setup()

from django.core.management import call_command

def run_migrations():
    try:
        call_command('makemigrations')
        call_command('migrate')
        print("Migrações concluídas com sucesso!")
    except Exception as e:
        print("Ocorreu um erro durante as migrações:", str(e))

if __name__ == "__main__":
    run_migrations()
