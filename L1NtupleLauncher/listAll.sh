for dir in ./*/
do
   cd $dir
   pwd
   if [[ ! -f goodfiles.txt ]]; then
      touch goodfiles.txt
      mkdir badfiles/
      touch badfiles/badfiles.txt
      for logfile in log*.txt
      do
         tmp=${logfile#*_}
         idx=${tmp%.*}
         out=$( tail -n 1 $logfile )
         if [[ $out == "dropped waiting message count 0" ]]; then
            echo $PWD/Ntuple_$idx.root >> goodfiles.txt
         else
            echo "job num $idx not correctly finished"
            echo $PWD/Ntuple_$idx.root >> badfiles/badfiles.txt
            mv $PWD/Ntuple_$idx.root badfiles/
         fi
      done
   fi
   cd -
done