import requests

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox,
                             QHBoxLayout, QDialog)
import webbrowser
from PyQt5.QtCore import Qt


class SettingsWidget(QWidget):
    """
    软件设置功能区组件
    用于配置软件的各种参数和选项
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        """初始化软件设置界面UI元素"""
        # 创建主布局
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # 软件信息区域
        info_group = QWidget()
        info_layout = QVBoxLayout(info_group)
        info_layout.setSpacing(8)

        # 添加软件标题
        title_label = QLabel("StarRail Team Assistant")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(title_label)

        # 添加软件信息
        self.current_version = "Beta0.1"
        info_layout.addWidget(QLabel(f"版本号: {self.current_version}"))
        info_layout.addWidget(QLabel(f"作者: @JasonShane"))
        
        info_layout.addWidget(QLabel(f"© {2025} 版权所有"))

        # 添加到主布局
        main_layout.addWidget(info_group)

        # 添加 spacer 使内容顶部对齐
        main_layout.addStretch()

        # 重置按钮区域
        reset_layout = QHBoxLayout()
        # 添加检查更新按钮
        check_update_btn = QPushButton("检查更新")
        check_update_btn.setStyleSheet("padding: 8px 16px;")
        check_update_btn.clicked.connect(self.show_check_update_dialog)
        reset_layout.addWidget(check_update_btn)
        # 添加间距
        reset_layout.addSpacing(10)
        # 添加重置按钮
        reset_button = QPushButton("重置软件")
        reset_button.setStyleSheet("padding: 8px 16px; background-color: #dfe6e9;")
        reset_button.clicked.connect(self.show_reset_confirmation)
        reset_layout.addWidget(reset_button)
        reset_layout.setAlignment(Qt.AlignCenter)

        # 添加到主布局
        main_layout.addLayout(reset_layout)

        self.setLayout(main_layout)

    def show_reset_confirmation(self):
        """显示重置软件确认对话框"""
        reply = QMessageBox.question(
            self,
            "确认重置",
            "是否确认重置软件到初始状态？此操作将清除所有配置。",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # 这里将在后续实现实际的重置逻辑
            QMessageBox.information(self, "提示", "软件已重置为初始状态")

    def get_latest_version(self):
        """从GitHub API获取最新版本号"""
        try:
            url = "https://api.github.com/repos/xJasonShane/StarRail-Team-Assistant/tags"
            print(f"请求GitHub API: {url}")
            response = requests.get(url, timeout=10)
            print(f"API响应状态码: {response.status_code}")
            response.raise_for_status()  # 抛出HTTP错误
            data = response.json()
            print(f"API响应数据: {data}")
            if data and isinstance(data, list):
                tag_name = data[0].get("name")
                print(f"提取到最新标签版本号: {tag_name}")
                return tag_name
            print("未找到任何标签版本")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"HTTP错误: {str(e)}，状态码: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print("网络连接错误，无法连接到GitHub服务器")
        except requests.exceptions.Timeout:
            print("请求超时，无法获取最新版本信息")
        except Exception as e:
            print(f"获取最新版本失败: {str(e)}")
        return None

    def compare_versions(self, current, latest):
        """比较版本号（简单实现，仅支持主版本.次版本格式）"""
        # 移除可能的前缀如'v'或'Beta'
        current = current.replace("Beta", "").replace("v", "")
        latest = latest.replace("Beta", "").replace("v", "")

        # 分割版本号并转换为整数列表
        current_parts = list(map(int, current.split(".")))
        latest_parts = list(map(int, latest.split(".")))

        # 比较版本号
        for i in range(max(len(current_parts), len(latest_parts))):
            current_part = current_parts[i] if i < len(current_parts) else 0
            latest_part = latest_parts[i] if i < len(latest_parts) else 0
            if latest_part > current_part:
                return True
            elif latest_part < current_part:
                return False
        return False

    def show_check_update_dialog(self):
        """检查更新并显示结果对话框"""
        print("开始检查更新流程")
        try:
            # 获取最新版本
            print("正在获取最新版本号...")
            latest_version = self.get_latest_version()
            print(f"获取到最新版本号: {latest_version}")

            # 处理检查结果
            if not latest_version:
                QMessageBox.warning(self, "检查失败", "无法连接到更新服务器，请稍后重试。")
                return

            # 比较版本
            current_version = self.current_version
            print(f"当前版本: {current_version}, 最新版本: {latest_version}")
            is_newer = self.compare_versions(current_version, latest_version)
            print(f"版本比较结果: {is_newer}")

            if is_newer:
                reply = QMessageBox.question(
                    self,
                    "发现新版本",
                    f"当前版本: {current_version}\n最新版本: {latest_version}\n是否前往GitHub Releases页面下载更新？",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes
                )
                if reply == QMessageBox.Yes:
                    webbrowser.open("https://github.com/xJasonShane/StarRail-Team-Assistant/releases")
            else:
                QMessageBox.information(self, "已是最新版本", f"当前版本 {current_version} 已是最新版本。")
        except Exception as e:
            print(f"检查更新时发生错误: {str(e)}")
            QMessageBox.critical(self, "错误", f"检查更新失败: {str(e)}")