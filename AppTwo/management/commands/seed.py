from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from AppTwo.management.ModelsFactory import UserFactory


class Command(BaseCommand):
    help = 'Seeds the database with fake users.'

    def add_arguments(self, parser):
        # Positional arguments (disabled)
        # parser.add_argument('users', default=50, nargs='+', type=int)

        # **kwargs: Named (optional) arguments
        parser.add_argument(
            '--users',
            default=50,
            type=int,
            help='The number of fake users to seed'
        )

    def handle(self, *args, **options):
        count = options['users']
        while count:
            try:
                UserFactory()
            except IntegrityError:
                continue
            else:
                count -= 1
