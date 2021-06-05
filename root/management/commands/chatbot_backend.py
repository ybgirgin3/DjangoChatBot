from django.core.management.base import BaseCommand, CommandError
from pprint import pprint


# veriler veritabanına ekleyecek olan kısım
from root.models import ArizaKaydi, Item

class Command(BaseCommand):
    help = 'Saves items from terminal chatbot'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="name of the ArizaKaydi")
        parser.add_argument('user_id', type=int, help="identity of the user in the db")

    def handle(self, *args, **kwargs):
        a1 = ArizaKaydi(
            name=kwargs['name'],
            user_id=kwargs['user_id']
        )
        
        a1.save()
        self.stdout.write("Ariza kaydi başarı ile eklendi")



