from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command creates facility"

    """     def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="time"
        )
        """

    def handle(self, *args, **options):
        faciliteis = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in faciliteis:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Facility created!"))
