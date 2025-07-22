import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
                             QDesktopWidget, QLabel, QPushButton, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor


from widgets.team_config import TeamConfigWidget
from widgets.character_settings import CharacterSettingsWidget
from widgets.software_settings import SettingsWidget


class MainWindow(QMainWindow):
    """
    主窗口类
    包含三个核心功能区的标签页界面
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StarRail Team Assistant")
        self.resize(1000, 700)  # 增大默认窗口尺寸
        self.setMinimumSize(600, 450)  # 添加最小尺寸限制
        self.center_window()
        self.setup_styles()
        self.init_ui()

    def center_window(self):
        """将窗口居中显示在屏幕上"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setup_styles(self):
        """设置应用程序样式表实现现代化界面风格"""
        self.setStyleSheet(""
            # 全局样式
            "QWidget {"
                "font-family: 'Inter', 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;"
                "font-size: 15px;"
                "color: #333333;"
                "background-color: #f8f9fa;"
            "}"

            # 主窗口样式
            "QMainWindow {"
                "background-color: #f0f2f5;"
            "}"

            # 标签页控件样式
            "QTabWidget::pane {"
                "border: 1px solid #dee2e6;"
                "border-radius: 8px;"
                "background-color: #ffffff;"
                "margin: 10px;"
            "}"
            "QTabBar::tab {"
                "background-color: #e9ecef;"
                "color: #495057;"
                "border: none;"
                "border-top-left-radius: 6px;"
                "border-top-right-radius: 6px;"
                "padding: 10px 20px;"
                "margin-right: 2px;"
                "min-width: 120px;"
                "height: 36px;"
                "font-size: 16px;"
            "}"
            "QTabBar::tab:selected {"
                "background-color: #ffffff;"
                "color: #212529;"
                "font-weight: 500;"
                "border-top: 2px solid #6c5ce7;"
            "}"
            "QTabBar::tab:hover:!selected {"
                "background-color: #dee2e6;"
            "}"

            # 按钮样式
            "QPushButton {"
                "background-color: #6c5ce7;"
                "color: white;"
                "border: none;"
                "border-radius: 6px;"
                "padding: 8px 16px;"
                "font-weight: 500;"
                "font-size: 15px;"
                "min-height: 36px;"
            "}"
            "QPushButton:hover {"
                "background-color: #5d4fc7;"
            "}"
            "QPushButton:pressed {"
                "background-color: #4a3fc7;"
            "}"
            "QPushButton:disabled {"
                "background-color: #6c757d;"
                "color: #ffffff;"
            "}"

            # 标签样式
            "QLabel {"
                "color: #212529;"
            "}"
            "QLabel#titleLabel {"
                "font-size: 24px;"
                "font-weight: bold;"
                "color: #6c5ce7;"
            "}"
            "QLabel#subtitleLabel {"
                "font-size: 17px;"
                "color: #6c757d;"
            "}"

            # 消息框样式
            "QMessageBox {"
                "background-color: #ffffff;"
                "border-radius: 8px;"
            "}"
            "QMessageBox QLabel {"
                "color: #212529;"
            "}"
            "QMessageBox QPushButton {"
                "min-width: 80px;"
            "}"
        "")

    def init_ui(self):
        """初始化主窗口UI元素"""
        # 创建标签页控件
        tab_widget = QTabWidget()
        tab_widget.setStyleSheet("QTabBar::tab { height: 30px; width: 120px; }")

        # 添加三个功能区标签页
        tab_widget.addTab(TeamConfigWidget(), "队伍配置")
        tab_widget.addTab(CharacterSettingsWidget(), "角色设置")
        tab_widget.addTab(SettingsWidget(), "软件设置")

        # 设置中央部件
        self.setCentralWidget(tab_widget)


def main():
    """应用程序入口函数"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import traceback
    import sys
    try:
        # 确保日志目录存在
        import os
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, 'app_startup.log')
        
        def log(message):
            """同时输出到控制台和日志文件"""
            print(message)
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(message + '\n')
        
        log("开始启动应用程序...")
        log("初始化QApplication...")
        app = QApplication(sys.argv)
        log("创建主窗口...")
        window = MainWindow()
        log("显示主窗口...")
        window.show()
        log("启动应用程序事件循环...")
        sys.exit(app.exec_())
    except Exception as e:
        error_msg = f"程序启动失败: {str(e)}"
        stack_trace = traceback.format_exc()
        log(error_msg)
        log("错误堆栈:\n" + stack_trace)
        # 同时写入标准错误流
        print(error_msg, file=sys.stderr)
        print("错误堆栈:\n" + stack_trace, file=sys.stderr)
        sys.exit(1)