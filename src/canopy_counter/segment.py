"""Tile segmentation helpers."""

from dataclasses import dataclass
from typing import Sequence


@dataclass
class TileResult:
    tile_id: str
    canopy_fraction: float


def threshold_mask(values: Sequence[float], cutoff: float = 0.42) -> list[int]:
    return [1 if value >= cutoff else 0 for value in values]


def canopy_fraction(values: Sequence[float], cutoff: float = 0.42) -> float:
    mask = threshold_mask(values, cutoff)
    if not mask:
        return 0.0
    return sum(mask) / len(mask)


def score_tile(tile_id: str, values: Sequence[float]) -> TileResult:
    return TileResult(tile_id=tile_id, canopy_fraction=canopy_fraction(values))
