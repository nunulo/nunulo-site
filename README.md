# nunulo-site

Nunulo 邀请制多人测试的公开介绍与 Android 分发入口。

## 边界

- 静态站点源代码位于 `release-site`。
- 当前页面说明多人测试范围、Web/Admin 入口、Android 安装步骤与测试边界。
- Android 下载使用 `nunulo-android` GitHub Release 的固定资产名，不在站点仓库提交 APK 或校验文件。
- API、用户 Web、管理端和内部方案不放入本仓库。

## 当前状态

历史测试 APK、模拟器截图、签名升级记录和端到端结果不再作为当前发布信息。页面明确说明项目仍未正式上线，当前仅用于邀请制多人测试。

`Container` 工作流只构建当前静态状态页，并使用提交 SHA 作为唯一镜像标签。构建镜像不表示页面已部署，也不表示 Nunulo 已正式上线。

`python scripts/verify_release_site.py` 会核对本地引用、Web/Admin 入口、固定 APK/SHA-256 下载地址，并阻止旧私人版文案和历史版本号重新进入当前页面。

Android 包名仍为 `com.lumokato.nunulo`。当前页面固定指向 `v0.2.0-test.1`，避免 GitHub 的 `releases/latest` 忽略预发布版本；只有对应 Release 资产实际存在后才算下载入口可用。测试包不承担历史安装升级兼容。

部署定义与服务器验收由 `nunulo-ops` 和全局 `server-ops` 工作流负责。
