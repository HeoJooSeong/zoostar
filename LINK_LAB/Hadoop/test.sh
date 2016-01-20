#!/bin/bash

foldername=/Users/zoostar/Desktop/pdf/


for LINE in $foldername/* 
do
	filename=`basename $LINE .pdf`
	filefullname=`basename $LINE`
	#echo $filename
#	echo `expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar

	mv /Users/zoostar/Desktop/pdftar/`expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar /Users/zoostar/Desktop/pdf
	cd /Users/zoostar/Desktop/pdf
	tar -rf `expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar $filefullname
	mv  `expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar /Users/zoostar/Desktop/pdftar/

done 

