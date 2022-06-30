from dundie.cli import main

def load(filepath):
    """ Loads data from filepath to the database """
    try:
        with open(filepath) as file:
            for line in file:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found {e}")


if __name__ == "__main__":
    main()
