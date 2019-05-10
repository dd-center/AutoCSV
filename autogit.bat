title Auto Update
color 16

echo;
echo;

echo 切换到GitHub备份目录
cd C:\Users\Administrator\Documents\blive

echo 开始提交代码到本地仓库
echo 当前目录是：%cd%

echo 开始添加变更
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
git add .
echo 执行结束！
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo 提交变更到本地仓库
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
set declation=%date:~0,4%%date:~5,2%%date:~8,2%-%time:~3,-3%   
git commit -m "上传于 %declation% "
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo 将变更情况提交到远程git服务器
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
git push origin master
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo 批处理执行完毕！
echo;
