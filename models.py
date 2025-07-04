from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    senha: Mapped[str] = mapped_column(String(50))

class Pessoa2(Base):
    __tablename__ = 'pessoa2'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    senha: Mapped[str] = mapped_column(String(50))
