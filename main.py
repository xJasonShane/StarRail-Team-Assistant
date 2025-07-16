import sys
import webbrowser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
                             QDesktopWidget, QLabel, QPushButton, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import Qt


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
        self.resize(800, 600)  # 设置初始大小而非固定几何尺寸
        self.setMinimumSize(600, 450)  # 添加最小尺寸限制
        self.center_window()
        self.init_ui()

    def center_window(self):
        """将窗口居中显示在屏幕上"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
    main()