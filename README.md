# tailscale-proxy-ip
tailscale内网穿透工具代理IP列表，提高国内用户访问速度


## 2024-3-12(代理IP每月更新一次，如果遇见无法使用的IP请更换其他IP尝试)

```
8.130.134.105
65.49.195.210
61.141.76.16
60.205.228.182	
60.171.194.63	
59.110.35.164	
59.110.153.192	
49.234.186.154	
49.232.230.124	
49.232.219.152	
49.232.138.251	
47.98.62.243	
47.97.202.197	
47.95.209.117	
47.94.88.138	
47.93.27.110	
47.92.132.89	
47.120.46.59	
47.116.43.147	
47.115.228.242	
47.115.218.53	
47.109.47.72	
47.109.27.44	
47.109.136.68	
47.109.102.206	
47.108.88.169	
47.107.164.30	
47.102.154.0
42.194.136.214	
42.193.106.95	
39.98.171.104	
39.91.166.209	
39.106.24.208	
39.102.33.219	
39.100.82.19	
222.186.61.48	
221.237.163.253	
211.128.96.206
202.95.1.18	
183.232.249.30	
183.136.206.136	
183.136.206.135
182.61.43.30	
182.42.105.251	
182.254.156.29	
175.178.61.187	
175.178.114.247
14.29.215.194	
139.9.61.243	
139.224.253.217	
139.224.226.248
139.196.235.183	
139.155.242.109
125.77.177.43	
124.222.145.200	
124.221.73.124	
124.114.120.165
123.60.165.97	
123.57.192.114	
123.57.184.213	
123.57.145.49	
123.56.164.174	
122.152.235.114	
121.61.115.38	
121.5.225.187	
121.41.168.187
121.40.172.172
121.40.159.46
121.36.110.42
121.199.30.253
120.79.67.41	
120.78.91.106	
120.26.194.83	
120.25.125.196
120.241.47.111
120.24.90.129	
119.91.220.218	
118.25.20.214
118.24.53.12	
118.24.28.206
116.205.235.225
116.196.76.195	
115.159.193.193
114.132.46.127	
114.132.160.99
114.116.240.121
113.88.3.81
113.31.114.236	
112.126.80.251
111.67.200.65
111.230.74.167	
111.230.55.205	
111.230.19.247	
111.229.37.116
111.229.128.54	
111.229.105.75	
106.54.232.104	
106.54.212.183
106.52.149.138
106.15.38.30
106.14.202.166
101.43.39.243
101.43.212.87	
101.43.205.223
101.43.123.233
101.42.41.212
101.42.224.220	
101.42.157.67	
101.42.0.22	
101.37.29.153	
101.35.222.241	
101.35.194.225	
101.237.34.189	
101.201.80.212
101.200.198.253	
101.133.146.250
1.12.238.73
1.117.75.240
```

## 使用步骤

1. 注册一个tailscale的账户并本机下载一个客户端。
注册地址：https://login.tailscale.com/login?next_url=%2Fadmin%2Facls%2Ffile
客户端下载地址：https://pkgs.tailscale.com/stable/

3. 添加代理IP配置

![image](https://github.com/sky984-11/tailscale-proxy-ip/assets/58068214/96042857-0019-4f58-baa7-e8e34b72974a)

参考配置如下，IPV4根据需要修改调整
```json
{
	"acls": [{"action": "accept", "dst": ["*:*"], "src": ["*"]}],
	"derpMap": {"OmitDefaultRegions": true, "Regions": {"901": {"Nodes": [{
		"DERPPort": 33445,
		"IPv4":     "101.200.198.253",
		"InsecureForTests": true,
		"Name":             "901a",
		"RegionID":         901,
	}], "RegionCode": "sky", "RegionID": 901, "RegionName": "sky"}}},
	"nodeAttrs": [{"attr": ["funnel"], "target": ["autogroup:member"]}],
	"ssh": [{
		"action": "check",
		"dst":    ["autogroup:self"],
		"src":    ["autogroup:member"],
		"users":  ["autogroup:nonroot", "root"],
	}],
}


```

3. 重启客户端(如果代理没生效重启，生效的话可以不进行这一步)



  
