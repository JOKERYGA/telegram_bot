from sqlalchemy import BigInteger, DateTime, Float, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    # default=func.now() - будет создано автоматически текущее время при создании записи в таблице
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    # onupdate, который указывает, что при обновлении записи значение в этом столбце будет автоматически обновляться на текущее время с помощью func.now()
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Banner(Base):
    __tablename__ = 'banner'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # unique=True: Этот аргумент указывает, что значения этого столбца должны быть уникальными.
    name: Mapped[str] = mapped_column(String(150), unique=True)
    image: Mapped[str] = mapped_column(String(150), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)

class Category(Base):
    __tablename__ = 'category'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)


class Product(Base):
    __tablename__='product'
    # autoincrement=True означает, что значения этого столбца будут автоматически увеличиваться при добавлении новой записи
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # nullable - он не может быть пустым -Fasle
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text) #Большой объем текста
    # asdecimal=True означает, что значения будут храниться как десятичные числа, а не двоичные числа с плавающей точкой. 
    # Numeric(5,2) - 5 знаков может быть, 2 после запятой (предпочтительнее для PostgreSQL
    price: Mapped[float] = mapped_column(Numeric(5,2), nullable=False)
    image: Mapped[str] = mapped_column(String(150))
    # ondelete=CASCADE - Опасная штука, не лучшее решение для данного случая
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete='CASCADE'),  nullable=False)
    
    # backref='product' - обратная связь для удобной выборки из баззы данных
    category: Mapped['Category'] = relationship(backref='product')
    

class User(Base):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # Значение в столбце уникальное - True
    user_id: Mapped[int] = mapped_column(unique=True)
    first_name: Mapped[str] = mapped_column(String(150), nullable=True)
    last_name: Mapped[str] = mapped_column(String(150), nullable=True)
    phone: Mapped[str] = mapped_column(String(13), nullable=True)


class Cart(Base):
    """Корзина пользователя для тех товаров, которые он хочет купить"""
    __tablename__ = 'cart'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', ondelete="CASCADE"), nullable=False)
    quantity: Mapped[int]
    
    # Чтобы в будущем можно было подтягивать информацию о связанных товарах и пользователях
    user: Mapped['User'] = relationship(backref='cart')
    product: Mapped['Product'] = relationship(backref='cart')