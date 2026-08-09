# nunulo-site

Nunulo 邀请制多人测试的公开介绍与 Android 分发入口。

## 边界

- 静态站点源代码位于 `release-site`。
- 当前页面说明多人测试范围、Web/Admin 入口、Android 安装步骤与测试边界。
- Android 下载使用 `nunulo-android` GitHub Release 的固定资产名，不在站点仓库提交 APK 或校验文件。
- API、用户 Web、管理端和内部方案不放入本仓库。

## 当前状态

邀请制多人测试环境已经上线，页面提供用户 Web、管理员后台、GitHub Organization 和 Android `v0.2.0-test.1` 固定 Release 资产入口。首轮线上四角色、并发、治理、R2 对账与数据库恢复验收已通过；当前尚未公开正式发布，物理 Android 仍待验收，测试数据继续按可丢弃环境管理。

`Container` 工作流只构建当前静态站点，并使用提交 SHA 作为唯一镜像标签。构建镜像本身不表示页面已部署；是否在线仍需核对实际 Compose、容器与外部入口。

`python scripts/verify_release_site.py` 会核对本地引用、Web/Admin 入口、固定 APK/SHA-256 下载地址，并阻止旧私人版文案和历史版本号重新进入当前页面。

Android 包名仍为 `com.lumokato.nunulo`。当前页面固定指向 `v0.2.0-test.1`，避免 GitHub 的 `releases/latest` 忽略预发布版本；只有对应 Release 资产实际存在后才算下载入口可用。测试包不承担历史安装升级兼容。

部署定义与服务器验收由 `nunulo-ops` 和全局 `server-ops` 工作流负责。
