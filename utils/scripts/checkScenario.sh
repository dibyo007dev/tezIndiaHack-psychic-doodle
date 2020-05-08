  echo "---------------------";
echo " Tests ";
echo "---------------------";
./utils/SmartPyBasic/SmartPy.sh test ./contract/dataTokenizer_test.py ./test-build; 
cat ./test-build/test.output;
echo "---------------------";
