import pymysql

def main():
    no = int(input('编号：'))
    password = input('密码：')
    con = pymysql.connect(
        host='localhost',
        port=3306,
        database='hrs',
        charset='utf8',
        user='root',
        password=password,
        autocommit=True
    )

    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'delete from tb_dept where dno=%s',
                (no,)
            )
        if result == 1:
            print('我可真是厉害啊')
    finally:
        con.close()


if __name__ == '__main__':
    main()