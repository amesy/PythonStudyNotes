import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP
from sqlalchemy.orm import sessionmaker

# 注意增删改后不要忘记commit.

# 连接数据库,返回数据库引擎.
engine = create_engine("mysql+pymysql://mysqlcli:12345678@10.68.7.20:3306/news_files?charset=utf8", echo=True)
# 生成orm基类.
Base = declarative_base()
# 定义表.
class News(Base):
    # 表名.
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(200), nullable=False)
    types = Column(String(2000), nullable=False)
    image = Column(String(10), nullable=True)
    author = Column(String(20), )
    view_count = Column(Integer)
    create_at = Column(TIMESTAMP)
    is_valid = Column(Boolean)


# 创建数据表，如果数据表存在，则忽视.
Base.metadata.create_all(engine)

# 创建与数据库的会话session class ,注意这里返回给session的是个class,不是实例.
Session = sessionmaker(bind=engine)

class OrmTest:
    def __init__(self):
        self.session = Session()

    def add_one(self):

        """
        新增记录
        """

        new_obj = News(
            title="标题",
            content="内容",
            types='娱乐'
        )

        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    # 获取一条数据.
    def get_one(self):
        # 获取id=4的数据.
        return self.session.query(News).get(4)

    # 获取多条数据.
    def get_more(self):
        return self.session.query(News).filter_by(types="娱乐")

    # 修改单条数据.
    def update_one_data(self, pk):
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            new_obj.title = 'python'
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False

    # 修改多条数据.
    def update_more_data(self):
        # filter()可以用 大小等于号，filter_by()只能用等于号.
        new_obj = self.session.query(News).filter_by(title = "python")
        if new_obj:
            for item in new_obj:
                item.view_count = 111
                self.session.add(item)
            self.session.commit()
            return True
        return False

    # 删除单条数据.
    def delete_one_data(self, pk):
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            self.session.delete(new_obj)
            self.session.commit()
            return True
        return False

    def delete_more_data(self):
        new_obj = self.session.query(News).filter_by(title="标题")
        if new_obj:
            for item in new_obj:
                self.session.delete(item)
            self.session.commit()
            return True
        return False

def main():
    obj = OrmTest()
    # rest = obj.add_one()
    # print(rest.id)

    # rest = obj.get_one()
    # if rest:
        # print("id:{0}->title:{1}".format(rest.id, rest.title))
    # else:
    #     print('not exist.')

    # rest = obj.get_more()
    # if rest:
    #     for item in rest:
    #         print("id: {0} -> title: {1}".format(item.id, item.title))

    # print(obj.update_one_data(4))
    # print(obj.update_more_data())

    # print(obj.delete_one_data(5))
    print(obj.delete_more_data())

if __name__ == '__main__':
    main()
