#!/usr/bin/env python3

 _     ____  ____ __ ___  ____  _____ ____  ____  _   _
/ \   /  _ \/_   \\\  \///  __\/  __//   _\/ _ \/ \ / |
| |   | / \| /   / \  / |  \/||  \  |  /  | / \|| |\ | |
| |_/\| |-||/   /_ / /  |    /|  /_ |  \__| \_/|| | \| |
\____/\_/ \|\____//_/   \_/\_\\\____\\\___/\___/\_/  \\|
########################################
# ///                                        \\\
#  		You can edit your configuration here
#
#
########################################
# global variables
auquatoneThreads = "5"
subdomainThreads = "10"
dirsearchThreads = "50"
dirsearchWordlist = "~/tools/dirsearch/db/dicc.txt"
massdnsWordlist = "~/tools/SecLists/Discovery/DNS/clean-jhaddix-dns.txt"
chromiumPath = "/snap/bin/chromium"
SECONDS = "0"

domain = ""
subreport= ""

########################################
# Happy Hunting
########################################

import sys, os, argparse
import subprocess



def main():
    # arguments parser set up
    parser = argparse.ArgumentParser(description='automate some tedious tasks of reconnaissance and information gathering', add_help=False)
    # create mutually exclusive groups for files or domains
    mutually_exclusive = parser.add_mutually_exclusive_group()
    mutually_exclusive.add_argument("-f", "--file", action='store', dest='file', type=argparse.FileType('r'), help="file filled with domains, each seperated by a newline")
    mutually_exclusive.add_argument("-d", "--domain", action='store', dest='domain', help="a single domain name to search")
    parser.add_argument("-e", "--exclude", action='store', dest='excluded', help="specify excluded subdomains")
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit.")
    args = parser.parse_args()
    print(args.domain)

if __name__ == '__main__':
    SystemExit(main())
