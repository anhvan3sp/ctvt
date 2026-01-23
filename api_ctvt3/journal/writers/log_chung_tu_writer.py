class LogChungTuWriter:
    def __init__(self, repo):
        self.repo = repo

    def write(self, log_chung_tu):
        self.repo.save(log_chung_tu)
