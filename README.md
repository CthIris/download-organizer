# download-organizer
自动整理下载文件夹的 Python 命令行工具

## 背景
下载文件夹长期堆积安装包、文档、图片混在一起，手动整理费时且易错

## 功能 (v1)
- 按文件类型自动分类到子目录
- --dry-run 模式：只预览不执行
- 同名文件自动加序号，不覆盖
- 操作日志 organizer.log

## 使用方法
python organizer.py --source ~/Downloads --dry-run
python organizer.py --source ~/Downloads

## 技术栈
Python 3.14 标准库（pathlib / shutil / argparse / logging）
纯面向对象设计

## TODO (v2)
JSON 自定义分类规则 / undo 还原 / 按月份归档
