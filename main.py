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