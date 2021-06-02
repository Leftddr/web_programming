import sys
import pymysql

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


# declarative_base() : Table 생성을 위한 부모 class인 Base 생성하는 함수
Base = declarative_base()


class Restaurant(Base):
    #테이블 이름을 지정한다.
    __tablename__ = 'restaurant'
    #id, name은 테이블의 특성을 지정한다. => primary_key => 주키, nullable 특성의 특성
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    #테이블 이름
    __tablename__ = 'menu_item'
    #특성들의 자료형과, 특징, 외래키 등을 지정한다.
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    #restaurant 테이블의 id를 외래키로 참조한다.
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    #이 클래스와 관련이 있다는 것을 알려준다.
    restaurant = relationship(Restaurant)


##### insert at end of file #####

engine = create_engine('mysql+pymysql://root:root@localhost/restaurant')

Base.metadata.create_all(engine)
