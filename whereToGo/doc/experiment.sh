find | 
grep -Ev ".git|.pyc" |
sort |
sed "s|\./whereToGo|    |g" |
sed "s|/data/|    |g" |
sed "s|/doc/|    |g" |
sed "s|/src/|    |g" |
sed "s|testdata/|    |g" |
sed "s|fusion/|    |g" |
sed "s|lib/|    |g" |
sed "s|navigation/|    |g" |
sed "s|sensors/|    |g" |
sed "s|ui/|    |g" 
