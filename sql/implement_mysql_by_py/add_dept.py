import pymysql

def main():
    no = int(input('编号：'))
    name = input('名字：')
    loc = input('所在地')
    password = input('密码：')

    # 1. 创建数据库对象
    con = pymysql.connect(
        host='localhost',
        port=3306,
        database='hrs',
        charset='utf8',
        user='root',
        password=password
    )

    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行sql并获取执行结果
            result = cursor.execute(
                'insert into tb_dept values (%s, %s, %s)',
                (no, name, loc)
            )
        if result == 1:
            print('提交成功')
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接，释放资源
        con.close()

if __name__ == '__main__':
    main()