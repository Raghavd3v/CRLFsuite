# -*- coding: utf-8 -*-

"""
This file contains all the command line arguments
"""
import argparse

parser = argparse.ArgumentParser()
Main_args = parser.add_argument_group('Main arguments')
Main_args.add_argument('-t', '--target', dest='target', help='Target URL')
Main_args.add_argument('-iT', '--import-targets', dest='targets', help='Multiple targets')
Main_args.add_argument('--pipe', dest='pipe', help='Read targets from stdin', action='store_true')
Request_args = parser.add_argument_group('Request arguments')
Request_args.add_argument('-m', '--method', dest='method', help='Request method (GET/POST), default: GET', default='GET')
Request_args.add_argument('-d', '--data', dest='data', help='HTTP POST data (ex: -d "akey=aval&bkey=bval")')
Request_args.add_argument('-c', '--cookies', dest='cookie', help='HTTP Cookies (ex: -c "KEY=Val;NEWKEY=NewVal")')
Request_args.add_argument('-tO', '--timeout', dest='timeout', help='Request timeout, default: 15', default=15)
Request_args.add_argument('--ssl', dest='ssl', help='Verify SSL cert.', action='store_true', default=False)
Request_args.add_argument('--delay', dest='delay', help='Delay between every request.', type=float, default=0)
Request_args.add_argument('--stable', dest='stable', help='Prioritize stability over speed.', action='store_true')
Request_args.add_argument('--headers', dest='headers', help='Add headers. Separate with newlines (if multiple).', nargs='?', const=True)
Output_args = parser.add_argument_group('Ouput arguments')
Output_args.add_argument('-oN', '--normal-output', dest='nout', help='Path for text output file')
Output_args.add_argument('-oJ', '--json-output', dest='jout', help='Path for json output file')
parser.add_argument('-cT', '--concurrent-threads', dest='threads', help='Number of concurrent threads, default: 10', default=10, type=int)
parser.add_argument('-v', '--verbose', dest='verbose', help='Verbosity level (1:3)',  default=1, type=int)
parser.add_argument('-r', '--resume', dest='resume', help='Resume scan using resume.cfg', action='store_true')
parser.add_argument('-sL', '--silent', dest='silent', help='Silent mode', action='store_true')
parser.add_argument('-sH', '--skip-heuristic', dest='heuristic', help='Skip heuristic scanning', action='store_true')
parser.add_argument('-cL', '--clean', dest='clean', help='Remove CRLFsuite generated files.', action='store_true')
args = parser.parse_args()
target = args.target
targets = args.targets
pipe = args.pipe
method = args.method
data = args.data
cookie = args.cookie
timeout = args.timeout
ssl = args.ssl
headers = args.headers
nout = args.nout
jout = args.jout
threads = args.threads
verbose = args.verbose
silent = args.silent
skipHeuristic = args.heuristic
resume = args.resume
clean = args.clean
stable = args.stable
delay = args.delay