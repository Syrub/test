[app]

title = TEST
package.name = test1
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.10.14,kivy==2.3.1
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.gradle_repository_url = https://mirrors.aliyun.com/macports/distfiles/gradle/

[buildozer]

log_level = 2
warn_on_root = 1