class NhapGasPolicy:
    def can_nhap(self, permissions: list[str]) -> bool:
        return "NHAP_GAS" in permissions
