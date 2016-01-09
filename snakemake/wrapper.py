__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.script import script


def wrapper(path, input, output, params, wildcards, threads, resources, log, config):
    """
    Load a wrapper from https://bitbucket.org/snakemake/snakemake-wrappers under
    the given path + wrapper.py and execute it.
    """
    # TODO handle requirements.txt

    if not path.startswith("http") or not path.startswith("file:"):
        path = "https://bitbucket.org/snakemake/snakemake-wrappers/raw/" + path
    if not (path.endswith("wrapper.py") or path.endswith("wrapper.R")):
        path += "wrapper.py"

    script("", path, input, output, params, wildcards, threads, resources, log, config)