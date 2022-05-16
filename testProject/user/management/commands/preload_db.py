from django.core.management import BaseCommand

# from preload_da.refound_payment import CheckReFundCreatePayment
from preload_data import populate_db



class Command(BaseCommand):
    help = 'Populate Database'

    def handle(self, *args, **options):
        populate_db.populate(options)

    def add_arguments(self, parser):
        parser.add_argument("--tollStations",default="preload_data/tollStations.json",type=str)
        parser.add_argument("--all_nodes",default="preload_data/all_nodes.json",type=str)
        parser.add_argument("--owners",default="preload_data/owners.json",type=str)
        parser.add_argument("--roads",default="preload_data/roads.json",type=str)
        parser.add_argument("--verbose",default=False,type=bool)