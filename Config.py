# -*- coding: utf-8 -*-

# app name (修改)
name_en = 'xiaopang'
name_zh = '小胖'

# 服务器地址(修改)
enterpriseServer = '192.168.2.31'

# 编译配置 (可不修改)
configuration = 'Release'

# 微信分享 (不设置将不能分享到微信)
WxAppIdUrl = 'wx6e666f66b66c666f'

# qq 分享 (不设置将不能分享到qq)
QQAppIdUrl = 'tencent1111111111'
QQAppId = '2222222222'

# 反馈邮箱 (修改)
feedbackEmail = 'ios.feedback@xxoo.net'

# group id (修改)
group_id = 'group.com.xiaopang.cloud'

# 打包使用描述文件 (修改)
exportProvisioningProfile = 'xiaopang Cloud Provisioning Profile'

# (修改)
# team id
# 签名
# product id
# 描述文件

# 1D6058900D05DD3D006BFB54 /* xxoo */,
# C7A2C0711A4BC6EF00D9F140 /* DocumentProvider */,
# C7A2C07F1A4BC6EF00D9F140 /* DocumentProviderFileProvider */,
# 3FEDDE551C3BD47B00573A76 /* Action */,

development_team = '88LW8888V8'
code_sign_identity = "iPhone Distribution";

targets = {
    '1D6058900D05DD3D006BFB54': {
        'DEVELOPMENT_TEAM': development_team,
        'CODE_SIGN_IDENTITY': code_sign_identity,
        'PRODUCT_BUNDLE_IDENTIFIER': "com.xiaopang.cloud",
        'PROVISIONING_PROFILE': "8aa88888-a888-8edc-bfb8-888d8ff888fb",
        'PROVISIONING_PROFILE_SPECIFIER': "xiaopang Cloud Provisioning Profile"
    },

    'C7A2C0711A4BC6EF00D9F140': {
        'DEVELOPMENT_TEAM': development_team,
        'CODE_SIGN_IDENTITY': code_sign_identity,
        'PRODUCT_BUNDLE_IDENTIFIER': "com.xiaopang.cloud.DocumentProvider",
        'PROVISIONING_PROFILE': "99cc99ac-9999-99e9-99b9-bf9e9e99ab99",
        'PROVISIONING_PROFILE_SPECIFIER': "xiaopang CloudDP Provisioning Profile"
    },

    'C7A2C07F1A4BC6EF00D9F140': {
        'DEVELOPMENT_TEAM': development_team,
        'CODE_SIGN_IDENTITY': code_sign_identity,
        'PRODUCT_BUNDLE_IDENTIFIER': "com.xiaopan.cloud.DocumentFileProvider",
        'PROVISIONING_PROFILE': "77bb7f7d-7777-777d-bf77-7777d777fb77",
        'PROVISIONING_PROFILE_SPECIFIER': "xiaopang CloudDFP Provisioning Profile"
    },

    '3FEDDE551C3BD47B00573A76': {
        'DEVELOPMENT_TEAM': development_team,
        'CODE_SIGN_IDENTITY': code_sign_identity,
        'PRODUCT_BUNDLE_IDENTIFIER': "com.xiaopang.cloud.actions",
        'PROVISIONING_PROFILE': "6e666666-a6f6-66a6-6a66-f6666b6fe66f",
        'PROVISIONING_PROFILE_SPECIFIER': "xiaopang CloudActions Provisioning Profile"
    }
}

# 替换 group id 的路径
group_paths = [
    'iphone-app/xxoo/xxoo.entitlements',
    'iphone-app/xxoo/Action/Action.entitlements',
    'iphone-app/xxoo/DocumentProvider/DocumentProvider.entitlements',
    'iphone-app/xxoo/DocumentProviderFileProvider/DocumentProviderFileProvider.entitlements',

    'iphone-app/xxoo/Classes/NTSAppGroupId.h',
    'iphone-app/xxoo/DocumentProviderFileProvider/Info.plist'
]

# 替换文字的路径
string_paths = [
    'iphone-app/xxoo/en.lproj/InfoPlist.strings',
    'iphone-app/xxoo/en.lproj/Localizable.strings',
    'iphone-app/xxoo/Action/en.lproj/InfoPlist.strings',
    'iphone-app/xxoo/DocumentProvider/en.lproj/InfoPlist.strings',

    'iphone-app/xxoo/zh-Hans.lproj/InfoPlist.strings',
    'iphone-app/xxoo/zh-Hans.lproj/Localizable.strings',
    'iphone-app/xxoo/Action/zh-Hans.lproj/InfoPlist.strings',
    'iphone-app/xxoo/DocumentProvider/zh-Hans.lproj/InfoPlist.strings'
]

# 替换图片的路径
image_paths = [
    'iphone-app/xxoo/Images.xcassets/AppIcon-2.appiconset/',
    'iphone-app/xxoo/Images.xcassets/AppIcon.appiconset/',
    'iphone-app/xxoo/Images.xcassets/AppLaunchImage.launchimage/',
    'iphone-app/xxoo/Images.xcassets/File Type/spolightIcon.imageset/',
    'iphone-app/xxoo/Images.xcassets/LauchIcon.imageset/',
    'iphone-app/xxoo/Images.xcassets/Misc/xxoo_20x20.imageset/',
    'iphone-app/xxoo/Images.xcassets/Pad Login/pad_login_logo.imageset/'
]
