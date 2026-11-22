#!/usr/bin/env python3
"""Prepare a repository-local environment, rebuild, then launch the reading server."""
import argparse
import fcntl
import hashlib
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]

def run(args, **kwargs):
    return subprocess.run([str(x) for x in args], cwd=str(ROOT), **kwargs)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only', action='store_true', help='Prepare and rebuild without opening a browser or starting a server.')
    args = parser.parse_args()
    environment = os.environ.copy()
    environment.pop('PYTHONHOME', None)
    environment.pop('PYTHONPATH', None)
    environment['PIP_DISABLE_PIP_VERSION_CHECK'] = '1'
    environment['PYTHONUNBUFFERED'] = '1'
    venv = ROOT/'.venv'
    python = venv/'bin/python'
    requirements = ROOT/'requirements-reader.txt'
    try:
        # Prevent two Finder launches racing to prepare the same environment.
        with (ROOT/'.reader-launch.lock').open('a') as lock:
            print('Preparing '+ROOT.name+'…', flush=True)
            fcntl.flock(lock, fcntl.LOCK_EX)
            if not python.exists():
                if venv.exists():
                    raise RuntimeError('The existing .venv environment is incomplete. It was left unchanged; repair it before launching again.')
                print('First launch: creating a private Python environment.', flush=True)
                run([sys.executable, '-m', 'venv', venv], env=environment, check=True)
            probe = run([python, '-c', 'import markdown_it, pygments'], env=environment, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            fingerprint = hashlib.sha256(requirements.read_bytes()).hexdigest()
            stamp = venv/'.reader-requirements'
            prepared = stamp.read_text().strip() if stamp.exists() else ''
            if probe.returncode or prepared != fingerprint:
                print('Checking reader dependencies. Internet is needed only if packages must be downloaded.', flush=True)
                run([python, '-m', 'pip', 'install', '--disable-pip-version-check', '-r', requirements], env=environment, check=True)
                run([python, '-c', 'import markdown_it, pygments'], env=environment, check=True)
                stamp.write_text(fingerprint+'\n')
            print('Refreshing articles and PDF index…', flush=True)
            run([python, ROOT/'build_reader.py'], env=environment, check=True)
        if args.prepare_only:
            print('Library is ready. Launcher checks passed.', flush=True)
            return 0
        print('Opening the library. Keep this window open while reading.', flush=True)
        os.execve(str(python), [str(python), str(ROOT/'tools/reader/serve_library.py')], environment)
    except KeyboardInterrupt:
        print('\nStartup cancelled.')
        return 130
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print('\nCould not start the library: '+str(error), file=sys.stderr)
        print('If package installation failed, check your connection and double-click Start Library.command again.', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
