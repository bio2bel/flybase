# -*- coding: utf-8 -*-

"""FlyBase database models."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import pybel.dsl
from .constants import MODULE_NAME

Base = declarative_base()

FLY_GENE_TABLE_NAME = f'{MODULE_NAME}_flyGene'


class FlyGene(Base):  # type: ignore
    """Gene table."""

    __tablename__ = FLY_GENE_TABLE_NAME

    id = Column(Integer, primary_key=True)

    flybase_id = Column(String(255), nullable=False, index=True)
    symbol = Column(String(255), nullable=False, index=True)

    def __repr__(self):
        """Return FlyBase symbol."""
        return str(self.flybase_id)

    def __str__(self):
        """Return FlyBase symbol."""
        return str(self.flybase_id)

    def serialize_to_protein_node(self) -> pybel.dsl.Gene:
        """Serialize to PyBEL node data dictionary."""
        return pybel.dsl.Gene(
            namespace='flybase',
            name=self.symbol,
            identifier=str(self.flybase_id)
        )
