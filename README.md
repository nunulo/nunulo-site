# nunulo-site

Nunulo 公开项目介绍和 Android 发布页。

## 边界

- 静态站点源代码位于 `release-site`。
- 发布页只承载产品介绍、版本状态、APK 下载和校验信息。
- APK 作为 GitHub Release 或部署制品发布，不提交到 Git。
- API、用户 Web、管理端和内部方案不放入本仓库。

## 当前状态

页面品牌已经使用 Nunulo，但正式 release keystore、包名、版本策略和可升级 APK 尚未完成。上线前必须同步更新版本号、SHA-256、发布日期和变更说明。

部署定义与服务器验收由 `nunulo-ops` 和全局 `server-ops` 工作流负责。
