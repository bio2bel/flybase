from typing import Mapping, Optional

from bio2bel import AbstractManager
from bio2bel.manager.namespace_manager import BELNamespaceManagerMixin
from pybel.manager.models import Namespace, NamespaceEntry
from .constants import MODULE_NAME
from .models import Base, FlyGene
from .parser import get_mapping_df


class Manager(AbstractManager, BELNamespaceManagerMixin):
    """Manager for FlyBase."""

    _base = Base
    module_name = MODULE_NAME

    namespace_model = FlyGene
    identifiers_recommended = 'FlyBase'
    identifiers_pattern = '^FB\w{2}\d{7}$'
    identifiers_miriam = 'MIR:00000030'
    identifiers_namespace = 'fb'
    identifiers_url = 'http://identifiers.org/fb/'

    def count_fly_genes(self) -> int:
        """Count the fly genes in the database."""
        return self._count_model(FlyGene)

    def summarize(self) -> Mapping[str, int]:
        """Summarize the database."""
        return dict(fly_genes=self.count_fly_genes())

    def is_populated(self) -> bool:
        """Check if the database is populated."""
        return 0 < self.count_fly_genes()

    def populate(self, gene_mapping_url: Optional[str] = None):
        """Populate the database."""
        mapping_df = get_mapping_df(url=gene_mapping_url)
        mapping_df.to_sql(FlyGene.__tablename__, self.engine, if_exists='append', index=False)
        self.session.commit()

    def _create_namespace_entry_from_model(self, model: FlyGene, namespace: Namespace) -> NamespaceEntry:
        return NamespaceEntry(
            encoding='GRP',
            name=model.symbol,
            identifier=model.flybase_id,
            namespace=namespace,
        )

    @staticmethod
    def _get_identifier(model: FlyGene) -> str:
        return model.flybase_id
