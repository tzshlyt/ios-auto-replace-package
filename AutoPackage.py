# -*- coding: utf-8 -*-

import os
import sys
import shutil
import re
import datetime
import subprocess
from pprint import pprint
from PIL import Image
from pbxproj import XcodeProject
import chardet

import Config


def replace_images():
    """替换图片资源文件"""
    print "============================ 替换图片 ==============================="
    for x in Config.image_paths:
        des_path_dir = os.path.join(_work_dir(), x)
        src_path_dir = os.path.join(_work_dir(), "customization", x)
        assert(os.path.isdir(des_path_dir))
        assert(os.path.isdir(src_path_dir))

        src_images = _find_images(src_path_dir)
        des_images = _find_images(des_path_dir)
        if len(src_images) != len(des_images):
            pprint("The count of source images %d not equal to destination images %d" %(len(src_images), len(des_images)))
            sys.exit()

        for image in src_images:
            src_image_path = os.path.join(src_path_dir, image)
            des_image_path = os.path.join(des_path_dir, image)

            if not os.path.exists(des_image_path):                   # 比较文件名
                print("image name mistake : %s" % src_image_path)
                sys.exit()

            # 比较图片大小
            im1, im2 = Image.open(src_image_path), Image.open(des_image_path)
            if (im1.size != im2.size):
                print("image size mistake : %s" % src_image_path)
                print("source image size %s  destination image size %s" %(im1.size, im2.size))
                sys.exit()

            try:
                # 如果目标文件存在，会替换原来的文件
                shutil.copyfile(src_image_path, des_image_path)
            except Exception as e:
                print("!!!!!!!!!!! 替换图片失败 !!!!!!!!!! ", e)
                sys.exit()


def replace_strings():
    """替换文字"""
    print "============================ 替换文字 ==============================="
    assert(len(Config.name_zh))
    assert(len(Config.name_en))
    for x in Config.string_paths:
        string_path = os.path.join(_work_dir(), x)
        assert (os.path.isfile(string_path))

        file = open(string_path, 'r')
        temp_path = "temp"
        temp_file = open(temp_path, 'w')

        lines = file.readlines()
        for line in lines:
            match = re.search(r'^".*".*(=).*".*";$', line)    # 找到“=”号
            if match:
                index = match.start(1)
                tarl = line[index:]
                if "en.lproj" in string_path:
                    pattern = re.compile(
                        r'xxx-proj-name', re.IGNORECASE)  # 替换“=”后半部分的名称
                    tarl = pattern.sub(Config.name_en, tarl)
                else:
                    pattern = re.compile("xxx", re.IGNORECASE)
                    tarl = pattern.sub(Config.name_zh, tarl)
                result = line[0:index] + tarl   # 拼接前半部分和替换的后半部分

                temp_file.write(result)
            else:
                temp_file.write(line)

        file.close()
        temp_file.close()
        file = None
        temp_file = None
        try:
            shutil.copyfile(temp_path, string_path)
        except Exception as e:
            print("!!!!!!!!!!! 替换文字失败 !!!!!!!!!! ", e)
            sys.exit()
        finally:
            os.remove(temp_path)



def replace_group():
    """替换 group id"""
    print "============================ 替换 group ==============================="
    assert(len(Config.group_id))
    for x in Config.group_paths:
        group_path = os.path.join(_work_dir(), x)
        _simple_replace(group_path, 'group.com.jianguopuzi.ios', Config.group_id)



def replace_share():
    """替换 微信 和 QQ 的分享 Id"""
    path1 = os.path.join(
        _work_dir(), 'iphone-app/xxx-proj-name/Classes/ApplicationDelegate.m')
    path2 = os.path.join(_work_dir(), 'iphone-app/xxx-proj-name/xxx-proj-name-Info.plist')
    path3 = os.path.join(_work_dir(
    ), 'iphone-app/xxx-proj-name/Classes/FileOperationsUI/ShareFileViewController.m')

    wechat_paths = [path1, path2]
    for path in wechat_paths:
        _simple_replace(path, 'wx8888888888888888', Config.WxAppIdUrl)

    _simple_replace(path2, 'tencent8888888888', Config.QQAppIdUrl)

    qq_paths = [path1, path3]
    for path in qq_paths:
        _simple_replace(path1, '8888888888', Config.QQAppId)



def replace_email():
    """替换反馈意见邮箱"""
    path = os.path.join(
        _work_dir(), 'iphone-app/xxx-proj-name/Classes/MoreLive/OtherSettingTableViewController.m')
    _simple_replace(path, 'ios.feedback@xxx-proj-name.net', Config.feedbackEmail)



def setup_appserver():
    """设置服务器地址"""
    server_conf_Path = os.path.join(
        _work_dir(), "iphone-app/xxx-proj-name/Server-conf.plist")
    if not os.path.exists(server_conf_Path):
        # 因为添加文件操作需要同时在配置文件里添加groups
        print "!!!!!!!!!! 设置服务器地址失败, 请手动创建 Server-conf.plist"
        sys.exit()

    set_cmd = 'Set :enterpriseServer ' + Config.enterpriseServer
    process = subprocess.Popen(
        ['/usr/libexec/PlistBuddy', '-c', set_cmd, server_conf_Path])
    process.wait()
    if process.returncode != 0:
        print "!!!!!!!!!!! 设置服务器地址失败 !!!!!!!!!!"
        sys.exit()


def build_and_package():
    """编译打包"""
    print "============================ 编译打包 ==============================="
    formt_time = datetime.datetime.now().strftime('-%Y%m%d-%H%M')
    common_name = Config.name_en + formt_time
    archive_name = common_name + '.xcarchive'
    archive_path = os.path.join(
        _work_dir(), 'history', common_name, archive_name)
    project_path = os.path.join(_work_dir(), 'iphone-app/xxx-proj-name/')
    workspace_path = os.path.join(project_path, "xxx-proj-name.xcworkspace")

    project = XcodeProject.load(
        os.path.join(project_path, "xxx-proj-name.xcodeproj/project.pbxproj"))
    # project.backup()    # 可选择备份

    rootObject = project["rootObject"]
    projects = project["objects"]
    attributes = projects[rootObject]["attributes"]["TargetAttributes"]
    targetsObject = projects[rootObject]["targets"]

    for target in targetsObject:
        attributes[target]["DevelopmentTeam"] = Config.targets[    # 修改 team
            target]["DEVELOPMENT_TEAM"]
        attributes[target]["ProvisioningStyle"] = "Manual"         # 设置为手动管理证书

        buildConfigurationListObject = projects[
            target]["buildConfigurationList"]
        buildConfigurationsObject = projects[
            buildConfigurationListObject]["buildConfigurations"]

        for buildConfig in buildConfigurationsObject:
            buildSettings = projects[buildConfig]["buildSettings"]

            # 修改签名类型
            buildSettings["CODE_SIGN_IDENTITY[sdk=iphoneos*]"] = Config.targets[target]["CODE_SIGN_IDENTITY"]

            for k, v in Config.targets[target].iteritems():   # 根据配置修改证书等
                buildSettings[k] = v
    project.save()

    # xcarchive
    archive_cmd = 'xcodebuild -workspace %s -scheme %s -configuration %s -archivePath %s clean archive' % (
        workspace_path, "xxx-proj-name", Config.configuration, archive_path)
    print 'archive_cmd: ', archive_cmd
    process = subprocess.Popen(archive_cmd, shell=True)
    process.wait()
    if process.returncode != 0:
        print "!!!!!!!!!!! 编译失败 !!!!!!!!!!"
        sys.exit()

    # 打包成ipa包
    export_name = common_name + '.ipa'
    export_path = os.path.join(_work_dir(), 'history', common_name, export_name)
    export_cmd = 'xcodebuild -exportArchive -archivePath  %s -exportPath %s -exportOptionsPlist exportOptions.plist' % (
        archive_path, export_path)
    print 'export_cmd: ', export_cmd
    export_process = subprocess.Popen(export_cmd, shell=True)
    export_process.wait()
    if process.returncode != 0:
        print "!!!!!!!!!!! 打包失败 !!!!!!!!!!"
        sys.exit()


def _work_dir():
    return os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))


def _find_images(path):     # 过滤非图片文件
    list_files = os.listdir(path)
    images = [image for image in list_files if os.path.splitext(image)[-1] == ".png"] 
    return images


def _simple_replace(path, org, des):
    assert(os.path.isfile(path))
    assert(len(org))
    assert(len(des))
    with open(path, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            line = line.replace(org, des)
            f.write(line)


if __name__ == '__main__':
    # replace_images()
    # replace_strings()
    replace_group()
    # replace_share()
    # replace_email()
    # setup_appserver()

    # 注意：前面的函数未使用过，使用前先修改配置
    build_and_package()
