import pymysql
from pymysql.cursors import DictCursor

class MysqlSearch:

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            # 获取连接.
            self.conn = pymysql.connect(
                host = '10.68.7.20',
                user = 'mysqlcli',
                password = '12345678',
                db = 'news',
                port = 3306,
                charset = 'utf8'
            )
        except pymysql.Error as e:
            print("Error: {0}".format(13))

    def close_conn(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print("Error: {0}".format(e))

    def get_one1(self, author, page, page_size):
        # 分页查询数据
        # page: 第几页, page_size: 每页多少条.
        offset = (int(page) - 1) * int(page_size)
        # 准备sql语句
        select_sql = "select * from `news` where `author` = %s order by `id` desc limit %s, %s;"
        # 找到游标
        self.cursor = self.conn.cursor(DictCursor)
        # 执行sql
        self.cursor.execute(select_sql, (author, offset, page_size, ))
        # 获取查询结果
        res = self.cursor.fetchall()
        # 关闭连接
        self.close_conn()
        return res

    def get_one(self):

        """
        查询一条记录.
        方法get_one1中使用了带列名的查询方式，通过DictCursor将游标设置为字典类型,方便后续使用。
        而该方法中使用了cursor的description属性，主要用在另一python连接mysql的驱动 - MySQLdb中。
        pymysql也通用该方法，只是处理过程略微繁琐。此处用到了zip函数做K/V关联。

        """

        # 准备sql语句
        select_sql = "select * from `news` where `types` = %s order by `id` desc;"
        # 找到游标
        self.cursor = self.conn.cursor()
        # 执行sql
        self.cursor.execute(select_sql, ('娱乐', 2,2))
        # 获取查询结果
        # 查询一条记录
        res = dict(zip([k[0] for k in self.cursor.description], self.cursor.fetchone()))
        # 关闭连接
        self.close_conn()
        print(res)

    def add_one(self):
        try:
            # 准备sql.
            sql = (
                "insert into `news`(`title`, `content`, `types`, `image`, `author`, `view_count`, `is_valid`) value"
                "(%s, %s, %s, %s, %s, %s, %s);"
            )
            # 获取链接和游标.
            self.cursor = self.conn.cursor()
            # 执行sql, 返回受影响行数.
            self.cursor.execute(sql, ('thirty-one', '第31条', '娱乐', 'http://thirty-one.png', 'amesy', '1', '1',))
            self.cursor.execute(sql, ('thirty-one', '第31条', '娱乐', 'http://thirty-one.png', 'amesy', 'er', '1',))
            # 提交事务，sql报错则不会提交.
            self.conn.commit()
        except:
            print('error')
            # self.conn.commit()
            self.conn.rollback()
        finally:
            # 关闭连接,释放资源.
            self.close_conn()


def main():
    obj = MysqlSearch()
    # obj.get_one()

    # rest = obj.get_one1('amesy', 2, 3)
    # for item in rest:
    #     print(item)
    #     print('---------------------------')

    obj.add_one()

if __name__ == '__main__':
    main()