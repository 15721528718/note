# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-10 14:44   #2024/10/10 14:44
@File：VAR.PY
@IDE：PyCharm
@Motto：南风知我意
"""
# 常量集
LOGINPARAMS = {
	"testev": {
		"shanghu": {
			"data": {
				"grant_type": "password",
				"pageType": 2,
				"password": "1d3b393b812ac1b2661fbc2cbfbf8366",
				"pwdLevel": 2,
				"scope": "all",
				"username": "Bee99"
			},
			"headers": {
				"authorization": "Basic c2FhczpzYWFzX3NlY3JldA==",
				"content-type": "multipart/form-data",
				"host": "saastestadminboss2023.adre45.com",
				"origin": "http://saastestadminboss2023.adre45.com",
				"referer": "http://saastestadminboss2023.adre45.com/",
				"identity-type":"user"
			},
			"url": "http://saastestadminboss2023.adre45.com/api/mgt/auth/oauth/token?grant_type=password&scope=all&username=Bee99&password=1d3b393b812ac1b2661fbc2cbfbf8366&pageType=2&pwdLevel=2"
		},
		"yunying": {
			"data": {
				"grant_type": "password",
				"pageType": 1,
				"password": "1d3b393b812ac1b2661fbc2cbfbf8366",
				"pwdLevel": 2,
				"scope": "all",
				"username": "Bee66"
			},
			"headers": {
				"authorization": "Basic c2FhczpzYWFzX3NlY3JldA==",
				"content-type": "multipart/form-data",
				"host": "saastestadmin2023.adre45.com",
				"origin": "http://saastestadmin2023.adre45.com",
				"referer": "http://saastestadmin2023.adre45.com/",
				"identity-type":"user"
			},
			"url": "http://saastestadmin2023.adre45.com/api/mgt/auth/oauth/token?grant_type=password&scope=all&username=Bee66&password=1d3b393b812ac1b2661fbc2cbfbf8366&pageType=1&pwdLevel=2"
		}
	},
	"uatev": {
		"shanghu": {
			"data": {
				"grant_type": "password",
				"pageType": 2,
				"password": "35c9c487c411f76c1568412683809c8f",
				"pwdLevel": 2,
				"scope": "all",
				"username": "Bee77"
			},
			"headers": {
				"authorization": "Basic c2FhczpzYWFzX3NlY3JldA==",
				"content-type": "multipart/form-data",
				"host": "newboss2.90818321.com:17443",
				"origin": "https://newboss2.90818321.com:17443",
				"referer": "https://newboss2.90818321.com:17443/",
				"identity-type":"user"
			},
			"url": "https://newboss2.90818321.com:17443/api/mgt/auth/oauth/token?grant_type=password&scope=all&username=bee77&password=35c9c487c411f76c1568412683809c8f&pageType=2&pwdLevel=2"
		},
		"yunying": {
			"data": {
				"grant_type": "password",
				"pageType": 1,
				"password": "35c9c487c411f76c1568412683809c8f",
				"pwdLevel": 2,
				"scope": "all",
				"username": "Bee11"
			},
			"headers": {
				"authorization": "Basic c2FhczpzYWFzX3NlY3JldA==",
				"content-type": "multipart/form-data",
				"host": "newyunying2.90818321.com:17443",
				"origin": "https://newyunying2.90818321.com:17443",
				"referer": "https://newyunying2.90818321.com:17443/",
				"identity-type":"user"
			},
			"url": "https://newyunying2.90818321.com:17443/api/mgt/auth/oauth/token?grant_type=password&scope=all&username=bee11&password=35c9c487c411f76c1568412683809c8f&pageType=1&pwdLevel=2"
		}
	}
}

# 优惠活动列表
ACTIVITY_LIST= ["充值次数活动", "总存款金额", "总有效投注额", "注册即赠送", "首次下注", "充值即送", "完善信息",
					 "取款返利", "自定义活动",
					 "周有效投注", "月有效投注", "日救援金", "周救援金", "月救援金", "自定义活动2", "三方活动",
					 "自定义存取款", "自定义有效投注",
					 "自定义救援金", "自定义存款投注", "自定义盈利活动", "回归存款活动", "回归投注活动", "回归盈利活动",
					 "回归亏损活动",
					 "手机号匹配活动"]