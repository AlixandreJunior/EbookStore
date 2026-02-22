class EbookRepositoryInterface:
    def save_ebook(self, ebook_data):
        raise NotImplementedError

    def get_ebook_by_id(self, ebook_id):
        raise NotImplementedError

    def delete_ebook(self, ebook_id):
        raise NotImplementedError