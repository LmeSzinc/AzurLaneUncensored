# 碧蓝航线反和谐 AzurLaneUncensored

旨在打造更方便 ~~更Geek~~ 的碧蓝航线反和谐。



本仓库文件所有立绘文件均来自于 [azurlane_uncensored](https://github.com/taofan233/azurlane_uncensored)。该仓库实际是空项目，仅在 Releases 发布更新。每次更新不发布新 Release，而是直接替换已有 Release 的 Assets，给版本控制带来了极大的不便。AzurLaneUncensored 将这些文件添加进 git 中，并提供自动反和谐的方法。

另外，这里需要讲解一些反和谐方式和纠正原仓库中的错误认识。

1. **localization.txt 反和谐**。将下面的内容写入 `com.bilibili.azurlane/files/localization.txt` 即可解锁特殊触摸和取消一些由代码控制的和谐，比如长岛 ”干物三连！“ 皮肤中的安全裤。

   ```
   Localization = true
   Localization_skin = true
   ```

   目前认为，这是游戏开发者故意留的后门。你可以大胆地认为，使用 localization.txt 反和谐是安全的。

2. **替换立绘反和谐**。localization.txt 并不能取消所有的和谐，因为一些和谐是直接画在了立绘图片上，比如矶风的 “新年合战“ 皮肤。因此，需要替换这些立绘图片。这些用来替换的立绘，并不是原仓库所说的 "废案"，而是外服的未和谐的立绘。

   修改立绘文件有潜在风险的。

3. **舰船名称反和谐**。舰船名称反和谐，以上方式均不能实现，只能通过修改 scripts 文件实现（com.bilibili.azurlane/files/AssetBundles/scripts32），本仓库和原仓库均不会提供修改过的 scripts 文件。scripts 文件包含各种游戏数据，修改它等同于制作科技，也就是外挂。同时，你也无法保证他人制作的 scripts 是否有修改其他内容 ~~有脏东西~~。

   修改 scripts 文件存在风险。

4. **光环助手反和谐**。大部分公司不会在没有利益的情况下，持续地免费地发布内容，而光环助手恰恰有着持续的免费的内容更新。作为一个 Geek，你不应该使用第三方游戏客户端，以免帐号密码泄漏或造成更严重的后果。

   使用第三方游戏客户端反和谐，风险最高。



## 使用反和谐

1. 使用 [ADB](https://developer.android.com/studio/releases/platform-tools)，查看已连接的设备。

   ```
   adb devices
   ```

   你会看到像这样的输出，第一列的内容是设备的 Serial，以 `127.0.0.1` 或 `emulator` 开头 Serial 的是模拟器，由数字英文组成的 Serial 是安卓真机。记住你的 Serial。

   ```
   List of devices attached
   127.0.0.1:59865 device
   da****de        device
   ```

   > 如果你没有找到你的设备
   >
   > - 安卓真机可以尝试重新插拔，然后重新执行 `adb devices`。
   > - 模拟器可以在网上搜索该模拟器的 Serial，然后执行 `adb connect <serial>`。

2. Clone 本项目

   ```
   git clone https://github.com/LmeSzinc/AzurLaneUncensored
   ```

   这将下载超过 70MB 的文件，如果你访问 Github 确有困难，可以使用 [码云镜像](https://gitee.com/LmeSzinc/AzurLaneUncensored)

   ```
   git clone https://github.com/LmeSzinc/AzurLaneUncensored
   ```

3. 在本项目根目录下，使用 ADB 命令推送文件，这里以模拟器的路径为例，命令将在 2-3 秒内执行完毕。

   ```
   adb -s <serial> push files /sdcard/Android/data/com.bilibili.azurlane
   ```
   
4. 重启碧蓝航线。



