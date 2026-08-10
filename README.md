# nunulo-site

Nunulo 邀请制照片地图的公开介绍与 Android 分发入口。

## 边界

- 静态站点源代码位于 `release-site`。
- 当前页面说明产品能力、Web/Admin 入口、Android 安装步骤与数据边界。
- Android 下载使用 `nunulo-android` GitHub Release 的固定资产名，不在站点仓库提交 APK 或校验文件。
- API、用户 Web、管理端和内部方案不放入本仓库。

## 当前状态

Nunulo 邀请制服务已经上线，页面提供用户 Web、管理员后台、GitHub Organization 和 Android `v0.2.1` 固定 Release 资产入口。四角色权限、并发、治理、R2 对账、对象恢复与数据库恢复已经完成线上验证；物理 Android 仍需持续回归。

`Container` 工作流只构建当前静态站点，并使用提交 SHA 作为唯一镜像标签。构建镜像本身不表示页面已部署；是否在线仍需核对实际 Compose、容器与外部入口。

`python scripts/verify_release_site.py` 会核对本地引用、Web/Admin 入口、固定 APK/SHA-256 下载地址，并阻止旧私人版文案和历史版本号重新进入当前页面。

Android 包名为 `com.lumokato.nunulo`。当前页面固定指向稳定版 `v0.2.1`；只有对应 Release 资产实际存在后才算下载入口可用。稳定版不承担早期测试 APK 的原位升级兼容。

部署定义与服务器验收由 `nunulo-ops` 和全局 `server-ops` 工作流负责。
