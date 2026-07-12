# 中文简介：构建公开发布页镜像，只包含项目介绍和 APK 下载文件。
FROM nginx:1.27-alpine

COPY ops/nginx.release-site.conf /etc/nginx/conf.d/default.conf
COPY release-site/ /usr/share/nginx/html/

EXPOSE 80
