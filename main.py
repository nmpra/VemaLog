# Vehicle Maintenance Log Project

import cli
from models import Garasi


def main():
    my_garage = Garasi()
    cli.run_cli(my_garage)


if __name__ == "__main__":
    main()
