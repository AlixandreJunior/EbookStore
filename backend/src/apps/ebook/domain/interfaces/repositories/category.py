from apps.ebook.domain.entities.category import CategoryEntity


class CategoryRepositoryInterface:
    def save_category(self, category: CategoryEntity) -> CategoryEntity:
        raise NotImplementedError
    
    def get_by_id(self, category_id: int) -> CategoryEntity:
        raise NotImplementedError

    def get_all(self) -> list[CategoryEntity]:
        raise NotImplementedError

    def delete(self, category_id: int):
        raise NotImplementedError