#!/bin/bash

foldername=/home/link/tmpPdf
mv /home/link/paper_archive/*.pdf /home/link/tmpPdf/

for LINE in $foldername/* 
do
	filename=`basename $LINE .pdf`
	filefullname=`basename $LINE`
	#echo $filename
#	echo `expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar
	hadoop fs -copyToLocal /user/root/Pdf_archives/`expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar /home/link/tmpPdf
	cd /home/link/tmpPdf
	tar -rf `expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar $filefullname
	hadoop fs -rm /user/root/Pdf_archives/`expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar
	hadoop fs -copyFromLocal `expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar /user/root/Pdf_archives
#	mv /Users/zoostar/Desktop/pdftar/`expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar /Users/zoostar/Desktop/pdf
#	cd /Users/zoostar/Desktop/pdf
#	tar -rf `expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar $filefullname
#	mv  `expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar /Users/zoostar/Desktop/pdftar/
	rm /home/link/tmpPdf/`expr \( $filename / 100 \) \* 100 + 1`_`expr \( \( $filename / 100 \) + 1 \) \* 100`pdf.tar
done 

mv /home/link/paper_archive/*."pdf" /home/link/paper_archive_Save

