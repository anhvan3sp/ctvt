class KeToanPolicy:
    def can_xem_bao_cao(self, permissions: list[str]) -> bool:
        return "XEM_BAO_CAO" in permissions
