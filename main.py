# idle_shell.py (This will be embedded, so no need for a separate file)
import code

def main():
    # Starting the interactive shell
    print(code.interact(local=locals()))

if __name__ == "__main__":
    main()