from sqlalchemy.orm import Session
from app.models.loan_model import LoanModel
from app.repositories.base_repository import BaseRepository

class LoanRepository(BaseRepository[LoanModel]):
    def __init__(self, session: Session):
        super().__init__(session, LoanModel)

    def get_open_loans(self) -> list[LoanModel]:
        """Retorna empréstimos não devolvidos"""
        return self.session.query(LoanModel).filter(LoanModel.returned == False).all()

    def get_by_user(self, user_name: str) -> list[LoanModel]:
        """Busca empréstimos por usuário"""
        return self.session.query(LoanModel).filter(LoanModel.user_name.ilike(f"%{user_name}%")).all()

    def return_book(self, loan_id: int) -> LoanModel | None:
        """Marca um empréstimo como devolvido"""
        loan = self.session.query(LoanModel).get(loan_id)
        if loan:
            loan.returned = True
            self.session.commit()
        return loan