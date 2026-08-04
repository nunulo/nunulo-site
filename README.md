# nunulo-site

Nunulo 公开项目介绍和 Android 发布页。

## 边界

- 静态站点源代码位于 `release-site`。
- 发布页只承载产品介绍、版本状态、APK 下载和校验信息。
- APK 作为 GitHub Release 或部署制品发布，不提交到 Git。
- API、用户 Web、管理端和内部方案不放入本仓库。

## 当前状态

页面已经使用 Nunulo，并记录当前 `0.1.0-personal.2` 个人签名测试包、截图和 SHA-256。APK 仍是本地忽略制品，不进入 Git；发布或部署前必须从同一 Android 提交的 CI 制品取得 APK 并核对页面校验值。

公开站点镜像不在普通 push 时自动发布，因为仓库不保存 APK。发布时手动运行 `Container` 工作流，提供同一 Android 构建产物的 HTTPS 地址和 SHA-256；流水线会先下载并校验 APK，再发布 amd64/arm64 镜像。

普通 push 和 PR 会运行 `python scripts/verify_release_site.py`，静态核对页面版本、包名、APK 链接、截图路径和 SHA-256 清单；手工发布流水线增加 `--require-apk`，同时校验实际 APK 内容。

当前 Android 包名为 `com.lumokato.nunulo`，个人稳定签名和模拟器原位升级已验证。物理 ARM 设备上的高德原生地图、拍照和大图尚未验收，页面不得写成实机完成。

部署定义与服务器验收由 `nunulo-ops` 和全局 `server-ops` 工作流负责。
