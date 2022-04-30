for dir in ./*/
do
   cd $dir
   pwd
   if [ -f goodfiles.txt ]; then # safe if already run on part of dataset
       touch goodfiles.txt
       mkdir badfiles/
       touch badfiles/badfiles.txt
       for logfile in log_*.txt
       do
           tmp=${logfile#*_}
           idx=${tmp%.*}
	   if grep -q "R__unzip: error" "$logfile"; then
	      echo "job num $idx: file corrupted"
	      echo $PWD/Ntuple_$idx.root >> badfiles/badfiles.txt
           elif ! grep -q "dropped waiting message count 0" "$logfile"; then
              echo "job num $idx not correctly finished"
              echo $PWD/Ntuple_$idx.root >> badfiles/badfiles.txt
              mv $PWD/Ntuple_$idx.root badfiles/
           else
              echo $PWD/Ntuple_$idx.root >> goodfiles.txt
           fi
       done           
   fi
   #temp=${dir#*/}
   #file=${temp::-1}
   #hadd -f $file.root Ntuple_*.root
   cd -   
done
