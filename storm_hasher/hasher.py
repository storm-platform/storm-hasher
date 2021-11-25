#
# This file is part of Checksum helper library for Storm platform.
# Copyright (C) 2021 INPE.
#
# Checksum helper library for Storm platform is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Checksum module."""

import hashlib
from pathlib import Path
from typing import Union, List

from typeguard import typechecked

SUPPORTED_ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
}


@typechecked
class StormHasher:
    def __init__(self, algorithm: str = "sha256", chunk_size: int = 4096):
        algorithm_fnc = SUPPORTED_ALGORITHMS.get(algorithm)

        if not algorithm_fnc:
            raise NotImplementedError(f"The {algorithm} algorithm is not supported!")

        self._chunk_size = chunk_size
        self._algorithm_fnc = algorithm_fnc

        self._algorithm_name = algorithm

    @property
    def algorithm(self) -> str:
        return self._algorithm_name

    @property
    def chunk_size(self) -> int:
        return self._chunk_size

    def hash_command(self, command: Union[str, List]) -> str:
        """Calculate the command checksum.

        Args:
            command (Union[str, List]): Command definition, in list or string format.

        Returns:
            str: String with hexdigest value.
        """

        if isinstance(command, str):
            command = command.split()

        # sorting to avoid problems with command parameters order
        command = sorted(command)
        command = " ".join(command)

        return self._algorithm_fnc(command.encode("utf-8")).hexdigest()

    def hash_file(self, file_path: Union[str, Path]) -> str:
        """Calculate file checksum.

        Args:
            file_path (Union[str, Path]): Path to the file

        Returns:
            str: String with hexdigest value.

        Raises:
            IOError when could not open given file.

        Note:
            This code is adapted from: https://github.com/brazil-data-cube/bdc-catalog
        """
        algorithm_obj = self._algorithm_fnc()

        def _read(stream):
            for chunk in iter(lambda: stream.read(self._chunk_size), b""):
                algorithm_obj.update(chunk)

        with open(str(file_path), "rb") as f:
            _read(f)

        return algorithm_obj.hexdigest()


__all__ = "StormHasher"
