#上傳資料
echo "# working-space" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/YAngTsungJen/working-space.git
git push -u origin master