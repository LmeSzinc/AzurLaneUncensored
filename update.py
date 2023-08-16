import os
import requests, requests_cache
import shutil

def update():
    if os.path.exists('./files'):
        shutil.rmtree('./files')
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
    res = []
    session = requests_cache.CachedSession(cache_control=True, backend='memory')
    data = session.get('https://api.github.com/repos/taofan233/azurlane_uncensored/releases').json()
    for item in data:
        if item['author']['login'] == 'taofan233':
            res.append(item['tag_name'])
    res = res[0]
    assets =  requests.get(f'https://github.com/taofan233/azurlane_uncensored/releases/download/{res}/uncensored.plus.{res}.zip')
    open(f"./tmp/uncensored.plus.{res}.zip", "wb+").write(assets.content)
    import zipfile
    with zipfile.ZipFile(f'./tmp/uncensored.plus.{res}.zip', 'r') as zf:
        zf.extractall('./tmp/')
    shutil.copytree('./tmp/files', './files')
    if os.path.exists('./files/AssetBundles/char'):
        shutil.rmtree('./files/AssetBundles/char')

    shutil.rmtree('./tmp')

if __name__ == '__main__':
    update()