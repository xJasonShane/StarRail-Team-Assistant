from PyQt5.QtWidgets import QWidget, QVBoxLayout


class CharacterSettingsWidget(QWidget):
    """
    角色设置功能区组件
    用于查看和编辑角色属性与技能
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """初始化角色设置界面UI元素"""
        layout = QVBoxLayout()
        self.setLayout(layout)