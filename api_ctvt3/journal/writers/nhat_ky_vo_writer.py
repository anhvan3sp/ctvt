class NhatKyVoWriter:
    def __init__(self, repo):
        self.repo = repo

    def write(self, nhat_ky_vo):
        self.repo.save(nhat_ky_vo)
