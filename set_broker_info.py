#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from service.broker import brokerService

brokerInfo = {
	"1020":"合庫",
	"1030":"土銀",
	"1040":"臺銀",
	"1090":"台灣工銀",
	"1110":"台灣企銀",
	"1160":"日盛",
	"1230":"彰銀",
	"1260":"宏遠",
	"1360":"港商麥格理",
	"1380":"台灣匯立證券",
	"1400":"港商蘇皇",
	"1440":"美林",
	"1470":"台灣摩根士丹利",
	"1480":"美商高盛",
	"1520":"瑞士信貸",
	"1530":"港商德意志",
	"1560":"港商野村",
	"1570":"港商法國興業",
	"1590":"花旗環球",
	"1650":"新加坡商瑞銀",
	"1660":"港商聯昌",
	"2180":"亞東",
	"2200":"元大期貨",
	"2210":"群益期貨",
	"3000":"台新銀",
	"5050":"大展",
	"5110":"富隆",
	"5260":"大慶",
	"5320":"高橋",
	"5380":"第一金",
	"5460":"寶盛",
	"5500":"豐銀",
	"5600":"永興",
	"5660":"日進",
	"5690":"豐興",
	"5850":"統一",
	"5860":"盈溢",
	"5870":"光隆",
	"5920":"元富",
	"5960":"日茂",
	"6010":"(牛牛牛)亞證券",
	"6110":"台中銀",
	"6160":"中國信託",
	"6210":"新百王",
	"6380":"光和",
	"6450":"永全",
	"6460":"大昌",
	"6480":"福邦",
	"6620":"全泰",
	"6640":"渣打商銀",
	"6660":"和興",
	"6910":"德信",
	"6950":"福勝",
	"7000":"兆豐",
	"7030":"致和",
	"7070":"豐農",
	"7080":"石橋",
	"7120":"台安",
	"7530":"富順",
	"7690":"金興",
	"7750":"北城",
	"7790":"國票",
	"7900":"豐德",
	"8150":"台新",
	"8380":"安泰",
	"8440":"摩根大通",
	"8450":"康和",
	"8490":"萬泰",
	"8520":"中農",
	"8560":"新光",
	"8580":"聯邦商銀",
	"8660":"萬通",
	"8690":"新壽",
	"8700":"花旗",
	"8710":"陽信",
	"8770":"大鼎",
	"8840":"玉山",
	"8880":"國泰",
	"8890":"大和國泰",
	"8900":"法銀巴黎",
	"8910":"台灣巴克萊",
	"8960":"香港上海匯豐",
	"9100":"群益金鼎",
	"9200":"凱基",
	"9300":"華南永昌",
	"9600":"富邦",
	"9800":"元大",
	"9A00":"永豐金"
}

for code in brokerInfo:
	brokerService.setBrokerInfo(code, brokerInfo[code])
