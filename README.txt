isotoma.recipe.distros
======================

This is a fork of ``plone.recipe.distros`` that uses the zc.buildout Download
API so that the lovely.buildouthttp monkey patches work on it. You probably
don't want to use this fork!!!!

Options
-------

urls
    The URLs of the archives to download. The archives specified in the same
    part will be extracted into the same parts folder named after the part.
    The full path to that folder will be available as 'location' from the
    parts option dictionary.

nested-packages
    The file names of one or more of the archives in the urls list.
    This will cause only the Python packages (identified by a __init__.py) in
    the top folder in the archive to be extracted into the destination.

version-suffix-packages
    The file names of one or more of the archives in the urls list.
    This will cause the part after the last dash to be omitted from the created
    destination folder.

