from django.core.management.base import BaseCommand

from AppTwo.management.ModelsFactory import UserFactory


class Command(BaseCommand):
    help = 'Seed the database with fake users.'

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
        for _ in range(options['users']):
            UserFactory()
