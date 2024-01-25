import os
import random
import winsound
import time
from cmd import Cmd
from typing import IO

__author__ = "MCTF-Alpha-27"
__version__ = "1.0.0"

class Solfeggio(Cmd):
    intro = "欢迎使用视唱练耳命令行\n"
    prompt = "♪> "

    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None:
        super().__init__(completekey, stdin, stdout)
        os.system("title 视唱练耳命令行 v%s"%__version__)
        self.groups = []
        self.number_to_name = {"1": "do", "2": "re", "3": "mi", "4": "fa", "5": "sol", "6": "la", "7": "si"}
        self.note_freqs = [262, 294, 330, 349, 392, 440, 494]

    def play_note(self, frequency, duration=1000):
        if not 1 <= int(frequency) <= 7:
            print("唱名的简谱写法无效。\n")
            return
        winsound.Beep(self.note_freqs[frequency - 1], duration)

    def do_cls(self, *ignored):
        """
        清空屏幕。

        用法：cls
        """
        os.system("cls")

    def do_practice(self, *ignored):
        """
        展示5组新的视唱练耳练习。

        用法：practice
        """
        self.groups.clear()
        for i in range(5): # 共5组，一组3个唱名
            self.groups.append(random.sample(range(1, 8), 3))
        for i in range(len(self.groups)):
            print(str(i + 1) + ".", self.groups[i])
        print()

    def do_showname(self, note_number=None):
        """
        将一个唱名的简谱写法转为此唱名的名称。

        用法：showname [note_number]
            没有参数        转换上一组视唱练耳练习的写法，如果有。
            note_number    一个唱名的简谱写法。
        """
        if note_number:
            if not 1 <= int(note_number) <= 7:
                print("唱名的简谱写法无效。\n")
                return
            print(note_number, "->", self.number_to_name[note_number])
            print()
        else:
            if len(self.groups) == 0:
                return
            for i in range(len(self.groups)):
                print(str(i + 1) + ".", self.groups[i], "->", [self.number_to_name[str(j)] for j in self.groups[i]])
            print()
    
    def do_playnote(self, note_number=None):
        """
        播放一个唱名的声音。

        用法：playname [note_number]
            没有参数        播放上一组视唱练耳练习的唱名声音，如果有。
            note_number    一个唱名的简谱写法。
        """
        if note_number:
            note_number = int(note_number)
            if not 1 <= note_number <= 7:
                print("唱名的简谱写法无效。\n")
                return
            self.play_note(note_number)
        else:
            if len(self.groups) == 0:
                return
            for i in range(len(self.groups)):
                os.system("cls")
                for k in range(len(self.groups)):
                    if k == i: # 用箭头指出当前正播放的唱名
                        print(str(k + 1) + ".", self.groups[k], "<-")
                    else:
                        print(str(k + 1) + ".", self.groups[k])
                print()
                print("当前播放：", self.groups[i], "->", [self.number_to_name[str(j)] for j in self.groups[i]])
                for j in self.groups[i]:
                    self.play_note(j)
                time.sleep(1)
            print()

Solfeggio().cmdloop()
