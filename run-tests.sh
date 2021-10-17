#!/usr/bin/env bash
#
# This file is part of Checksum helper library for Storm platform.
# Copyright (C) 2021 INPE.
#
# Checksum helper library for Storm platform is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle storm_hasher examples tests setup.py && \
isort storm_hasher examples tests setup.py --check-only --diff && \
check-manifest --ignore ".travis.yml,.drone.yml,.readthedocs.yml" && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest && \
pytest
