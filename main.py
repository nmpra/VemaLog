# Vehicle Maintenance Log Project

import cli
from models import Garage


def main():
    my_garage = Garage()
    cli.run_cli(my_garage)


if __name__ == "__main__":
    main()
