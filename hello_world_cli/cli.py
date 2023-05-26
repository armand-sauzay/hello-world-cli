"""CLI for the hello_world_cli package."""
import argparse

import requests


def main(argv=None) -> int:
    """
    Parse name and print greeting.

    Args:
        argv: The arguments to parse. Expects a name to greet.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name", help="The name to greet and count repos for", default="world"
    )
    args = parser.parse_args(argv)
    if args.name == "":
        print("Username cannot be empty")
        return 1

    print(f"Hello {args.name}!")

    repos = requests.get(f"https://api.github.com/users/{args.name}/repos")
    if repos.status_code != 200:
        print(f"Failed to fetch repos for {args.name}")
        return 1
    repos = repos.json()
    print(f"You have {len(repos)} repos.")  # type: ignore
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
