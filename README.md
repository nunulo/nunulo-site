# nunulo-site

Nunulo 照片社区与地图相册的公开介绍、政策与 Android 分发入口。

## 边界

- 静态站点源代码位于 `release-site`。
- 当前页面说明匿名展示、公开注册、产品能力、Web 入口、Android 安装步骤与数据边界。
- 隐私政策和服务条款分别位于 `release-site/privacy` 与 `release-site/terms`，当前版本为 `2026-08-11`。
- Android 下载使用 `nunulo-android` GitHub Release 的固定资产名，不在站点仓库提交 APK 或校验文件。
- API、用户 Web、管理端和内部方案不放入本仓库。

## 当前状态

Nunulo 稳定服务已经上线，本轮页面准备匿名只读窗口、公开注册和 Android `v0.2.5` 下载入口。管理后台保留给授权管理员，不作为公开站点导航项；物理 Android 仍需持续回归。

`Container` 工作流只构建当前静态站点，并使用提交 SHA 作为唯一镜像标签。构建镜像本身不表示页面已部署；是否在线仍需核对实际 Compose、容器与外部入口。

`python scripts/verify_release_site.py` 会核对本地引用、Web 入口、固定 APK/SHA-256 下载地址，并阻止旧私人版文案、内部验收文案和历史版本号重新进入当前页面。

当前页面固定指向稳定版 `v0.2.5`；只有对应 Release 资产实际存在后才允许部署这一版页面。稳定版不承担早期测试 APK 的原位升级兼容。

部署定义与服务器验收由 `nunulo-ops` 和全局 `server-ops` 工作流负责。
