# -*- coding: utf-8 -*-

userPage = {
	"page_name": u" ",
	"locate": "",
	"not_visable": "",
	"elements": {
        "module_name":          u"",
		"moduleStatus":          "//div[@class = '']/ul/li",
		"userTable": 			('table_001', 	"//div[@class = '']"),
		"user_icon":			('button', 	    "//div[@class = '']"),
		"user_menu":			('list_003',    ""),
		"statusFilter": 		('list_005',    "//div[@class = '']//input[@placeholder='']"),
		"addBtn": 		 		('button', "//"),
		"actionAlert":	 		("alert",  "//div[@class = '']/p"),
		"salesAreaTree": 		("dropTree_004", ""),
	},
	"forms": {

		"addForm": {
			"locate": "",
			"elements": {
				"userName": 	("text",            ""),
				"mobilePhone": 	("text",            ""),
				"saleAreaName": ("dropTree_002",    ""),
                "mainPost":     ("list_001",        "//label[contains(text(),'主岗位')]/following::input"),
                "sex":          ("list_001",        "//label[contains(text(),'性别')]/following::input"),
				"workCode": 	("text",            "//input[@placeholder='工号']"),
				"entryDate": 	("datepicker_001",  "//input[@placeholder='入职日期']"),
				"shortCode": 	("text",            "//input[@placeholder='短号']"),
				"email": 		("text",            "//input[@placeholder='邮箱']"),
				"idcard": 		("text",            "//input[@placeholder='身份证号']"),
				"QQ": 			("text",            "//input[@placeholder='QQ']"),
				"weChat": 		("text",            "//input[@placeholder='微信号']"),
				"tel":			("text",            "//input[@placeholder='固定电话']"),
				"address": 		("text",            "//div[contains(@class, 'address-border')]/input"),
				"remark": 		("text",            "//textarea[@type='textarea']"),
				"ifGenAccount": ("checkbox_002",    "//label[@class = 'el-checkbox']"),
				"cancelBtn":	("button",          "//div[@class='el-dialog__headerbtn']"),
				"saveBtn":		("button",          "//button/span[contains(text(), '保存')]"),
			},
		},


	},
}
