import code
import sys


def main():
    # Create namespace dictionary
    namespace = {
        '__name__': '__main__',
        '__doc__': None,
        '__package__': None
    }

    # Add current namespace items
    namespace.update(globals())

    # Create interactive shell banner
    banner = """
    Python Interactive Shell
    Python Version: {}
    Type 'exit()' or Ctrl-D to exit
    """.format(sys.version.split('\n')[0])

    # Start the interactive shell with custom banner and namespace
    code.interact(banner=banner, local=namespace)


if __name__ == "__main__":
    main()