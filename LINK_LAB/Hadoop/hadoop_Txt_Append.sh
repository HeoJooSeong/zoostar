#!/bin/bash

foldername=/home/link/tmpTxt


for LINE in $foldername/* 
do
	filename=`basename $LINE .txt`
	filefullname=`basename $LINE`

	hadoop fs -copyToLocal /user/root/Txt_archives/`expr \( $filename / 1000 \) \* 1000 + 1`_`expr \( \( $filename / 1000 \) + 1 \) \* 1000`txt.tar /home/link/tmpTxt
	cd /home/link/tmpTxt
	tar -rf `expr \( $filename / 1000 \) \* 1000 + 1`_`expr \( \( $filename / 1000 \) + 1 \) \* 1000`txt.tar $filefullname
	hadoop fs -copyFromLocal `expr \( $filename / 1000 \) \* 1000 + 1`_`expr \( \( $filename / 1000 \) + 1 \) \* 1000`txt.tar /user/root/Txt_archives

done 

