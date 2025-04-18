import shutil
import tempfile
from pathlib import Path

import patoolib
import requests_cache


def update():
    session = requests_cache.CachedSession(
        cache_control=True, backend='memory')
    data = session.get(
        'https://api.github.com/repos/taofan233/azurlane_uncensored/releases/latest').json()
    assert data['author']['login'] == 'taofan233', 'Wrong author'
    tag_name = data['tag_name']
    latest_asset = next(asset for asset in data['assets']
                        if asset['name'].startswith(f'uncensored.plus.{tag_name}'))
    tmp_dir = Path(tempfile.mkdtemp())
    asset_file = tmp_dir / latest_asset['name']
    asset_file.write_bytes(session.get(
        latest_asset['browser_download_url']).content)
    patoolib.extract_archive(str(asset_file), outdir=str(tmp_dir))
    latest_files = next((p for p in tmp_dir.rglob('files') if p.is_dir()), None)
    local_files = Path('./files').resolve()
    if latest_files.exists() and local_files.exists():
        shutil.rmtree(local_files)
        shutil.copytree(latest_files, local_files)
    char_files = local_files / 'AssetBundles' / 'char'
    if char_files.exists():
        shutil.rmtree(char_files)
    shutil.rmtree(tmp_dir)


if __name__ == '__main__':
    update()
