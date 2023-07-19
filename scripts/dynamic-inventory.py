#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date: 2023-07-19T15:10:49+08:00
# Author: liuliancao <liuliancao@gmail.com>
"""Description: Testing dynamic inventory py for awx."""

import argparse
import json

class AwxInventory:
    """Awx inventory test."""
    def get_hosts(self):
        hosts = {
            "_meta": {"hostvars": {}},
            "group-1": {
                "hosts": ["172.31.253.73"],
                "vars": {
                    "group_name": "group-1"
                }
            },
            "group-2": {
                "hosts": ["172.31.253.75"],
                "vars": {
                    "group_name": "group-2"
                }
            }
        }
        return json.dumps(hosts)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='get awx dynamic inventory')

    mandatory_options = arg_parser.add_mutually_exclusive_group()

    mandatory_options.add_argument('--list',
                                   action='store_true',
                                   help="show group servers")

    mandatory_options.add_argument('--host',
                                   help="show specific battle server info")

    try:
        ai = AwxInventory()
        args = arg_parser.parse_args()
        if args.host:
            print(ai.get_host(host=args.host))
        elif args.list:
            print(ai.get_hosts())
        else:
            raise ValueError("Expecting either --host $HOSTNAME or --list")
    except ValueError:
        raise

