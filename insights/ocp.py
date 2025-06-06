"""
Top level OpenShift 4 component
===============================
The :py:func:`conf` component recognizes insights-operator and must-gather
archives.
"""

import logging
import os
import yaml
import warnings

from fnmatch import fnmatch
from insights.core import SafeLoader as Loader
from insights.core.plugins import component, datasource
from insights.core.context import ExecutionContext, fs_root

from insights.core.archives import extract
from insights.parsr.query import from_dict, Result
from insights.util import content_type

log = logging.getLogger(__name__)


@fs_root
class InsightsOperatorContext(ExecutionContext):
    """Recognizes insights-operator archives"""

    marker = "config/featuregate"


@fs_root
class MustGatherContext(ExecutionContext):
    """Recognizes must-gather archives"""

    marker = "cluster-scoped-resources"


contexts = [InsightsOperatorContext, MustGatherContext]


def _get_files(path):
    for root, dirs, names in os.walk(path):
        for name in names:
            yield os.path.join(root, name)


def _load(path):
    with open(path) as f:
        for doc in yaml.load_all(f, Loader=Loader):
            yield from_dict(doc, src=path)


def _process(path, excludes=None):
    excludes = excludes if excludes is not None else []
    for f in _get_files(path):
        if excludes and any(fnmatch(f, e) for e in excludes):
            continue
        try:
            for d in _load(f):
                yield d
        except Exception:
            log.debug("Failed to load %s; skipping.", f)


def analyze(paths, excludes=None):
    warnings.warn(
        "This '{0}' is deprecated and will be removed in {1}.".format('ocp.analyze', '3.6.0'),
        DeprecationWarning,
        stacklevel=2,
    )
    if not isinstance(paths, list):
        paths = [paths]

    results = []
    for path in paths:
        if content_type.from_file(path) == "text/plain":
            results.extend(_load(path))
        elif os.path.isdir(path):
            results.extend(_process(path, excludes))
        else:
            with extract(path) as ex:
                results.extend(_process(ex.tmp_dir, excludes))

    return Result(children=results)


@datasource(contexts)
def conf_root(broker):
    for ctx in contexts:
        if ctx in broker:
            return broker[ctx].root


@component(conf_root)
def conf(root):
    """
    The ``conf`` component parses all configuration in an insights-operator or
    must-gather archive and returns an object that is part of the parsr common
    data model.  It can be navigated and queried in a standard way. See the
    `tutorial`_ for details.

    .. _tutorial: https://insights-core.readthedocs.io/en/latest/notebooks/Parsr%20Query%20Tutorial.html

    """
    return analyze(root, excludes=["*.log"])
