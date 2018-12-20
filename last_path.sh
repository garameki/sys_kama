getFile(){

	arg=$1
	for ele in ${arg//\// }; do
		:
	done
	echo $ele
}
pp=$(pwd)
aa=$(getFile $pp)
echo $aa
