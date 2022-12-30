from django.core.management.base import BaseCommand, CommandError
from customer.models import User
import logging

logger = logging.getLogger(__file__)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('userphone')

    def handle(self, *args, **options):
        try:
            user = User.objects.get(phone=options['userphone'])
            if user.is_staff:
                user.is_staff = False
            else:
                user.is_staff = True
            user.save()
            self.stdout.write('successes')
            logger.info('infor')
            logger.warning('warning')
        except User.DoesNotExist:
            self.stdout.write('user not found')
