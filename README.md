# A Backup tool
 backup some folders to other folders using python scripts
 
**脚本是为给电脑做定期备份而设计的。** 

**内容：**

主要包含两个`gui.py`和`backup.py`两个python脚本，一个配置文件`config.txt`。每个文件简要介绍如下
 
 - `backup.py`：将源文件夹内的的所有文件备份到目标文件夹。`backup.py`只重新复制相比于上次修改过的内容，并且始终保持目标文件夹内内容与源文件夹内内容一致，也就是说在执行备份炒作时**会删除目标文件夹内有但源文件夹内没有的文件或子文件夹**。
 - `config.txt`：包含多个源文件夹路径和目标文件夹路径，**每一行**包含一个源文件夹路径和对应的目标文件夹路径，两个路径之间以"------"作为分隔符（要求源文件夹路径和目标文件夹路径中不包含"------"）。
 - `gui.py`：提供一个编辑`config.txt`，调用`backup.py`执行备份操作的图形界面。

**使用方法如下：**

运行`gui.py`，会弹出窗口

<img src="https://github.com/cwt2001/backup_tools/assets/69576774/fd4ee83e-0b1b-495b-a7d1-af4a6390ea96" width="500" />

窗口中的各个部分含义如下
- 界面中间的文本框：最初显示的是`config.txt`中内容，文本框内的内容可以直接更改
- `Source Folder`按钮：选择源文件夹
- `Dest Folder`按钮：选择目标文件夹
- `Add to config file`按钮：将上面选择的源文件夹和目标文件夹对应路径加到`config.txt`中
- `Save config file`按钮：将**当前文本框**中显示内容重新保存为`config.txt`
- `Backup`按钮：将`config.txt`中对应源文件夹备份到对应的目标文件夹中

在使用时，先运行`gui.py`，修改`config.txt`内容（也可不修改），然后再点`Backup`按钮即可完成操作。


 
 
 
