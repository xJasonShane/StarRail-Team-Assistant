from PyQt5.QtWidgets import QWidget, QVBoxLayout


class TeamConfigWidget(QWidget):
    """
    队伍配置功能区组件
    用于创建和管理游戏队伍配置
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """初始化队伍配置界面UI元素"""
        layout = QVBoxLayout()
        self.setLayout(layout)