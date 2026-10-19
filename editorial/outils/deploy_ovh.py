# -*- coding: utf-8 -*-
"""Deploiement FTP du dossier site/maquettes vers OVH.
Identifiants lus dans deploy.secrets.json (a la racine, gitignore) :
{
  "host": "ftp.cluster129.hosting.ovh.net",
  "user": "cvbusim",
  "password": "…",
  "protocole": "ftps",                    # ou "ftp"
  "remote_dirs": ["www/election2027", "www"]
}
"""
import json, os, ftplib, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOCAL = os.path.join(ROOT, 'site', 'maquettes')

def main():
    conf_path = os.path.join(ROOT, 'deploy.secrets.json')
    conf = json.load(open(conf_path, encoding='utf-8'))
    cls = ftplib.FTP_TLS if conf.get('protocole', 'ftps') == 'ftps' else ftplib.FTP
    ftp = cls()
    ftp.connect(conf['host'], 21, timeout=30)
    ftp.login(conf['user'], conf['password'])
    if cls is ftplib.FTP_TLS:
        ftp.prot_p()
    files = sorted(f for f in os.listdir(LOCAL) if os.path.isfile(os.path.join(LOCAL, f)))
    for remote in conf['remote_dirs']:
        ftp.cwd('/')
        for part in remote.split('/'):
            try:
                ftp.cwd(part)
            except ftplib.error_perm:
                ftp.mkd(part)
                ftp.cwd(part)
        for name in files:
            src = os.path.join(LOCAL, name)
            with open(src, 'rb') as fh:
                ftp.storbinary(f'STOR {name}', fh)
            print(f'[deploy] {remote}/{name}')
    ftp.quit()
    print('[deploy] termine :', len(files), 'fichiers x', len(conf['remote_dirs']), 'dossier(s)')

if __name__ == '__main__':
    main()
