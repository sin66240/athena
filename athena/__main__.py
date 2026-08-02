import sys

from athena.cli.selfplay_cli import SelfPlayCLI


def main():

    cli = SelfPlayCLI()

    if len(sys.argv) < 2:
        print("ATHENA CLI")
        print("commands:")
        print("  status")
        print("  champion")
        print("  matches")
        return


    command = sys.argv[1]


    if command == "status":

        print(cli.status())


    elif command == "champion":

        print(cli.champion())


    elif command == "matches":

        print(cli.matches())


    else:

        print("Unknown command")


if __name__ == "__main__":
    main()
