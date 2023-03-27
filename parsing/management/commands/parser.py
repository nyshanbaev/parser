import requests
from bs4 import BeautifulSoup as BS
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll
from peewee import *
from decouple import config


db = PostgresqlDatabase(config('NAME'), user=config('USER'), password=config('PASSWORD'), host='localhost', port=5432)


class Rent(Model):
    img = CharField()
    date = CharField()
    price = CharField()
    currency = CharField()

    class Meta:
        database = db
        table_name = 'rent'


Rent.create_table()


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

for i in range(1, 101):
    url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273'


    def news():
        
        response = requests.get(url)
        soup = BS(response.text, 'lxml')
        items = soup.find_all('div', class_='search-item')
        for item in items:
            if item.find('img').get('data-src') != None:
                img = item.find('img').get('data-src')
            else:
                img = 'None'
            date = item.find('span', class_='date-posted').text
            if item.find('div', class_='price').text.strip().startswith('$'):
                price = item.find('div', class_='price').text.strip()[1:]
            else:
                price = 'None'

            if item.find('div', class_='price').text.strip().startswith('$'):
                currency = item.find('div', class_='price').text.strip()[:1]
            else:
                currency = 'None'

            room = Rent(img=img, date=date, price=price, currency=currency)
            room.save()

    news()