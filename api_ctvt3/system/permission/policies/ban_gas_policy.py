class BanGasPolicy:
    def can_ban(self, permissions: list[str]) -> bool:
        return "BAN_GAS" in permissions
