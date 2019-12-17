#!/usr/bin/python3,3
# -*- coding: utf-8 -*-
"""pexe38 package
"""
__version__ = '1.3'

from .patch_distutils import patch_distutils

patch_distutils()
