from sqlalchemy import DateTime, Float, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    # default=func.now() - будет создано автоматически текущее время при создании записи в таблице
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    # onupdate, который указывает, что при обновлении записи значение в этом столбце будет автоматически обновляться на текущее время с помощью func.now()
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    


class Product(Base):
    __tablename__='product'
    # autoincrement=True означает, что значения этого столбца будут автоматически увеличиваться при добавлении новой записи
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # nullable - он не может быть пустым
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text) #Большой объем текста
    # asdecimal=True означает, что значения будут храниться как десятичные числа, а не двоичные числа с плавающей точкой. 
    price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    image: Mapped[str] = mapped_column(String(150))
    
    def __repr__(self) -> str:
        pass