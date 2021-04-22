# aws_ondemand_instance_finder
finds best matching instance for the requirement provided with cost comparison

can be used to find all the instances with the required spec:
  1. open aws_pricing_ondemand_analysis.py
  2. use function find_bestInstance()  , pass parameters cpu and ram requirements & keep current_region and current_instance_type as None
  3. run the scripts.
  
can be used to find cheapest instance in other regions
  1. open aws_pricing_ondemand_analysis.py
  2. use function find_bestInstance()  , pass parameters cpu and ram requirements & keep current_region as the region in which you want and current_instance_type as the instance type which you want to compare with.
  3. run the scripts.
  
 can be used to find the required configuration in specific region
  1. open aws_pricing_ondemand_analysis.py
  2. use function find_bestInstance()  , pass parameters cpu and ram requirements & keep current_region as the required region and current_instance_type as None
  3. run the scripts.
