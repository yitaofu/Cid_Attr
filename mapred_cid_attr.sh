#!/bin/bash

#rm archives/work.zip
#zip -r archives/work.zip scripts/

HADOOP_BIN="/usr/local/webserver/hadoop/bin/hadoop"
STREAMING_JAR="/usr/local/webserver/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar"

###########################################
#PROJ_ROOT=`pwd`
#cd ${PROJ_ROOT}

DATE=`date +%F_%H:%M:%S`
AUTHOR="fuyitao"
MODULE="cid_attr"

mkdir logs/${DATE}
LOG_DIR="logs/${DATE}"

###############################
#hadoop path
HHOME="/data/archive/app_oeudjgn5872a7c3aaa54_datamine/${AUTHOR}/"
INPUT_DATA="/data/archive/app_oeudjgn5872a7c3aaa54_datamine/zhanghua/taobao_mine/2016-09-07/cid_id_attr_val/part-*"

#生成数据路径
OUTPUT_DATA="${HHOME}/cid_attr"

${HADOOP_BIN} fs -rm -r ${OUTPUT_DATA}

${HADOOP_BIN} jar ${STREAMING_JAR} \
		-input ${INPUT_DATA} \
		-output ${OUTPUT_DATA} \
		-mapper cid_attr_map.py \
		-reducer cid_attr_red.sh \
		-file cid_attr_map.py \
		-file cid_attr_red.sh \
		-jobconf mapred.map.tasks=301 \
		-jobconf mapred.reduce.tasks=201 \
		-jobconf mapred.job.priority="NORMAL" \
		-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
		-jobconf stream.num.map.output.key.fields=2 \
		-jobconf num.key.fields.for.partition=1 \
		-jobconf mapred.job.name="${MODULE}_${AUTHOR}" \
		1>${LOG_DIR}/$MODULE.msg 2>${LOG_DIR}/$MODULE.err

