import requests
import xlrd
from demoLog import demo_Log


# 读表方法，返回游戏表格礼物列表 list_game ===================================================================================
def read_excel():
    def push_data(col):
        if sheet_gifts.cell(row, col).value != '':
            return str(int(sheet_gifts.cell(row, col).value))

    def push_name(col2):
        if sheet_gifts.cell(row, col2).value != '':
            return sheet_gifts.cell(row, col2).value

    table_game = xlrd.open_workbook(r"D:\iGame海外游戏社区\表格校验\人气值礼品表.xls")
    sheet_gifts = table_game.sheet_by_name('礼品表')
    row_num = sheet_gifts.nrows
    col_num = sheet_gifts.ncols
    list_games = []
    for row in range(1, row_num):
        try:
            gid = push_data(0)
            name = push_name(1)
            price = push_data(4)
            popularity = push_data(5)
            intimacy = push_data(6)
            if intimacy is None:
                intimacy = str(0)
            limit = push_data(9)
            itemid = push_data(17)
            sort = push_data(22)
            exclusive = push_data(23)
            if exclusive is None:
                exclusive = str(0)
            dict_gift = {
                '礼品ID': gid,
                '礼品名称': name,
                '价格': price,
                '人气值': popularity,
                '亲密度': intimacy,
                '赠送上限': limit,
                '物品ID': itemid,
                '专属礼物': exclusive,
                '礼品顺序': sort
            }
            list_games.append(dict_gift)
        except Exception as e:
            demo_Log().log().error(f"in {row} line error：{e}")
    return list_games


# 爬取管理端的方法，返回社群礼物列表 list_club=================================================================================
def request_gifts():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
        'cookie': 'language=zh_CN; TimeZone=+8; userToken=fca9b4c99785a2e22a782cc85ce729ad;'
                  ' nickname=libichen; user_id=92; uin=714a26a6725218697c4d3fbc4a1b5076; area=id; sess_gameid=10041'
    }
    url = "https://t.admin.meemo.club/index.php/community/Gift/getList?id=&gid=&name=&currentPage=1&pageSize=10"

    list3 = []
    response = requests.get(url=url, headers=headers)
    content = response.content.decode('utf-8')
    dict1 = response.json()  # 一、先把结果转json，也就是python中dict类型
    # print(dict1)
    list1 = [dict1['data']]  # 二、取出字典中 key 为 data 的所有值
    dict2 = list1[0]  # 三、每次循环把列表里的index为0的值拿出来，那个值就是字典，现在把外面那个[]给剥掉了，只剩下字典了，比较麻烦的是第一个是列表[]

    # 先动态获取页数
    totalCount = int(dict2['totalCount'])
    page = totalCount % 10
    if totalCount % 10 == 0:
        page = int(totalCount / 10)
    else:
        page = int(totalCount / 10) + 1

    for i in range(page + 1):
        currentPage = str(i)
        param = {
            'id': '',
            'gid': '',
            'name': '',
            'currentPage': currentPage,
            'pageSize': '10'
        }
        resp = requests.get(url=url, params=param, headers=headers)

        dict1 = resp.json()  # 一、先把结果转json，也就是python中dict类型
        # print(dict1)
        list1 = [dict1['data']]  # 二、取出字典中 key 为 data 的所有值
        dict2 = list1[0]  # 三、每次循环把列表里的index为0的值拿出来，那个值就是字典，现在把外面那个[]给剥掉了，只剩下字典了，比较麻烦的是第一个是列表[]
        list2 = []

        if list1[0] == []:  # 四、加一个判断，过滤掉第一个为[]的值
            pass
        else:
            # print(dict2)
            # print(dict2['list'])
            list2 = dict2['list']
            # print(list2)

            for j in range(0, len(list2)):  # 取出单个字典 list2[j]
                # list2[j]['name'] = str(list2[j]['name'])
                list3.append(list2[j])

    return list3


# 两个list的对比方法，格式为list[{礼物1}{礼物2}.......]=======================================================================
print('ID比对如下         >>>>>>\n')


def list_diff(list_gameid, list_clubid, list1, list2):
    # 对比ID

    for i in range(len(list1)):
        list_gameid.append(str(list1[i]['礼品ID']))  # 把游戏的ID单独拿出来，存到列表

    for j in range(len(list2)):
        list_clubid.append(str(list2[j]['gid']))  # 把社群的ID单独拿出来，存到列表

    # A和B对比不同,A有B没有，即为新增
    if set(list_gameid).difference(set(list_clubid)) != set():
        print('新增ID有：')
        print(sorted(set(list_gameid) - set(list_clubid)))
    else:
        print('无新增ID')

    # B和A对比不同,B有A没有，即为删除
    if set(list_clubid).difference(set(list_gameid)) != set():
        print('删除ID有')
        print(sorted(set(list_clubid) - set(list_gameid)))
    else:
        print('无删除ID')

    print('\n与游戏配置不一致如下 >>>>>>\n')
    for i in list1:
        for j in list2:
            if str(i.get('礼品ID')) == str(j.get('gid')):  # 当礼物ID相同的时候，进行比对，ID不同的不比对

                if str(i.get('礼品名称')) != str(j.get('name')):
                    print(str('礼物ID为' + str(i.get('礼品ID')) + '的礼物名称：' + '游戏为' + i.get('礼品名称')) + '  社群为' + str(
                        j.get('name')))

                if str(i.get('价格')) != str(j.get('price')):
                    print(str('礼物ID为' + str(i.get('礼品ID')) + '的价格：' + '游戏为' + i.get('价格')) + '  社群为' + str(
                        j.get('price')))

                if str(i.get('人气值')) != str(j.get('popularity')):
                    print(
                        str('礼物ID为' + str(i.get('礼品ID')) + '的人气值：' + '游戏为' + i.get('人气值')) + '  社群为' + str(
                            j.get('popularity')))

                if str(i.get('亲密度')) != str(j.get('intimacy')):
                    print(str('礼物ID为' + str(i.get('礼品ID')) + '的亲密度：' + '游戏为' + i.get('亲密度')) + '  社群为' + str(
                        j.get('intimacy')))

                if str(i.get('赠送上限')) != str(j.get('limit')):
                    print(str('礼物ID为' + str(i.get('礼品ID')) + '的赠送上限：' + '游戏为' + i.get('赠送上限')) + '  社群为' + str(
                        j.get('limit')))

                if str(i.get('物品ID')) != str(j.get('itemid')):
                    print(str('礼物ID为' + str(i.get('礼品ID')) + '的物品ID：' + '游戏为' + i.get('物品ID')) + '  社群为' + str(
                        j.get('itemid')))

                if str(i.get('专属礼物')) != str(j.get('exclusive')):
                    print(
                        str('礼物ID为' + str(i.get('礼品ID')) + '的专属礼物：' + '游戏为' + i.get('专属礼物')) + '  社群为' + str(
                            j.get('exclusive')))

                if str(i.get('礼品顺序')) != str(j.get('sort')):
                    print(str('礼物ID为' + str(i.get('礼品ID')) + '的礼品顺序：' + '游戏为' + i.get('礼品顺序')) + '  社群为' + str(
                        j.get('sort')))


if __name__ == '__main__':
    # print(read_excel())
    list_gameid = []
    list_clubid = []
    list_game = read_excel()
    list_club = request_gifts()
    list_diff(list_gameid, list_clubid, list_game, list_club)
