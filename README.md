# tailscale-proxy-ip
tailscale内网穿透工具代理IP列表，提高国内用户访问速度


## 代理列表(每周自动更新，如果遇见无法使用的IP请更换其他IP尝试)
<!-- BLOG_START -->
### 更新日期: 2024-09-14 12:41:41
```
61.141.76.16

```
<!-- BLOG_END -->

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



  
