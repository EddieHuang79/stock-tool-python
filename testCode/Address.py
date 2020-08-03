#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 要建立一個有三層式的地址清單，如：城市、行政區、里名、道路名
# 可以隨時返回上一層查詢
# 可以隨時退出程式

# dictionary
addressInfo = {
    "台北市":{
        "中正區":{
            "水源里":["羅斯福路4段"],
            "富水里":["永春街"],
            "文盛里":["羅斯福路3段"],
         },
        "大同區":{
            "國順里":["延平北路3段"],
            "建明里":["重慶北路一段"],
            "光能里":["民生西路"],
        },
        "信義區":{
            "西村里":["基隆路1段"],
            "正和里":["仁愛路4段"],
            "興隆里":["基隆路1段"],
        },

    },
    "新北市":{
        "板橋區":{
            "黃石里":["宮口街"],
            "自強里":["中正路"],
            "金華里":["金華街"],
        },
        "中和區":{
            "中原里": ["永和路"],
            "連和里": ["連城路"],
            "連城里": ["連城路"],
        },
        "新莊區":{
            "中平里": ["中平路"],
            "中原里": ["中港路"],
            "昌平里": ["中華路2段"],
        },
    },
    "台中市":{
        "北屯區":{
            "北屯里": ["太原路"],
            "北京里": ["國校巷"],
            "北興里": ["北屯路"],
        },
        "后里區": {
            "廣福里": ["寺山路"],
            "仁里里": ["圳寮路"],
            "義里里": ["梅里路"],
        },
        "北區": {
            "頂厝里": ["永興街"],
            "賴村里": ["梅亭街"],
            "賴旺里": ["中清路一段"],
        }
    }
}

isEndCity = False

while isEndCity == False:

	isEndSection = False

	inputCity = input('請輸入要找的城市: ')

	if len(inputCity) < 1:

		print('未輸入字串！')

	else:

		isCityExist = addressInfo.get(inputCity)

		if isCityExist != None:

			while isEndSection == False:

				isEndLi = False

				inputSection = input('請輸入要找的行政區('+inputCity+')，回上一層請輸入back: ')

				if inputSection == 'back':
					break

				isSectionExist = addressInfo[inputCity].get(inputSection)

				if isSectionExist != None:

					while isEndLi == False:

						inputLi = input('請輸入要找的里名('+inputCity+')('+inputSection+')，回上一層請輸入back: ')

						if inputLi == 'back':
							break

						isLiExist = addressInfo[inputCity][inputSection].get(inputLi)

						if isLiExist != None:
							message = '您所查找的路名如下('+inputCity+')('+inputSection+')('+inputLi+'): ' + ','.join(addressInfo[inputCity][inputSection][inputLi])
							message+= '，要從城市重新開始查詢請輸入City, 行政區請輸入Section, 里請輸入 Li, 結束請輸入 End: '
							isContinue = input(message)
							if isContinue == 'City':
								isEndSection = True
								isEndLi = True
							elif isContinue == 'Section':
								isEndLi = True
							elif isContinue == 'End':
								isEndCity = True
								isEndSection = True
								isEndLi = True
							else:
								print('重找路名')
								
						else:
							print('找不到所輸入的里名')
				else:
					print('找不到所輸入的行政區')

		else:
			print('找不到所輸入的城市')
