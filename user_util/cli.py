# -*- coding: utf-8 -*-

"""Console script for user_util."""
import json
import sys
import click
from . import user_util


@click.command()
@click.option('--username', '-u',
              help='Original username to convert to retired username. Multiple usernames can be specified.',
              multiple=True
              )
@click.option('--email', '-e',
              help='Original email address to convert to retired email address. '
                   'Multiple email addresses can be specified.',
              multiple=True
              )
@click.option('--salt', '-s',
              help='JSON-formatted list of salt strings ordered from oldest to current. '
                   'All double-quotes must be escaped.'
              )
def retire_user(username, email, salt):
    """
    Console script for user_util to convert usernames/email addresses to retired usernames/email addresses.
    """
    try:
        salt_list = json.loads(salt)
    except (TypeError, ValueError):
        click.echo("Salt value \"{}\" is invalid JSON.".format(salt))
        raise
    results = {}
    for name in username:
        results[name] = user_util.get_retired_username(name, salt_list)
    for email_addr in email:
        results[email_addr] = user_util.get_retired_email(email_addr, salt_list)

    click.echo("{}".format(json.dumps(results)))
    return 0


if __name__ == "__main__":
    sys.exit(retire_user())  # pragma: no cover
