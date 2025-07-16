import webbrowser
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox,
                             QHBoxLayout)
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
        info_layout.addWidget(QLabel(f"版本号: Beta0.1"))
        info_layout.addWidget(QLabel(f"作者: @JasonShane"))
        
        # Github按钮
        github_btn = QPushButton("Github仓库")
        github_btn.setStyleSheet("color: #0066cc; text-decoration: underline; background: none; border: none;")
        github_btn.setCursor(Qt.PointingHandCursor)
        github_btn.clicked.connect(self.show_github_confirmation)
        info_layout.addWidget(github_btn)

        info_layout.addWidget(QLabel(f"© {2025} 版权所有"))

        # 添加到主布局
        main_layout.addWidget(info_group)

        # 添加 spacer 使内容顶部对齐
        main_layout.addStretch()

        # 重置按钮区域
        reset_layout = QHBoxLayout()
        reset_button = QPushButton("重置软件")
        reset_button.setStyleSheet("padding: 8px 16px; background-color: #f0f0f0;")
        reset_button.clicked.connect(self.show_reset_confirmation)
        reset_layout.addWidget(reset_button)
        reset_layout.setAlignment(Qt.AlignCenter)

        # 添加到主布局
        main_layout.addLayout(reset_layout)

        self.setLayout(main_layout)

    def show_github_confirmation(self):
        """显示访问Github确认对话框"""
        reply = QMessageBox.question(
            self,
            "访问Github",
            "是否打开浏览器访问项目Github页面？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            webbrowser.open("https://github.com/xJasonShane/StarRail-Team-Assistant")

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