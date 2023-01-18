import pandas as pd
import timeit
import statistics

def compare_function_performance(functions, inputs):
    function_times = {f.__name__: {} for f in functions} # initialize a dictionary for each function
    for function in functions:
        for input in inputs:
            execution_time = timeit.timeit(lambda: function(input), number=1)
            function_times[function.__name__][input] = execution_time # add input and runtime to the dictionary 
    input_times = {}
    for function, inputs_results in function_times.items():
        for input_, runtime in inputs_results.items():
            if function not in input_times:
                input_times[function] = {input_: runtime}
            else:
                input_times[function][input_] = runtime
    detail_table = pd.DataFrame.from_dict(input_times)

    df = pd.DataFrame.from_dict(function_times)
    
    summary_table = pd.DataFrame(columns=["max runtime", "min runtime", "average runtime", "difference (%)"]) # create an empty DataFrame with the desired columns
    for function, runtimes in function_times.items():
        max_runtime = max(runtimes.values()) # calculate max runtime
        min_runtime = min(runtimes.values()) # calculate min runtime
        average_runtime = statistics.mean(runtimes.values()) # calculate average runtime
        difference = round((max_runtime - min_runtime) / min_runtime * 100,1) # calculate difference in percentages
        summary_table.loc[function] = [max_runtime, min_runtime, average_runtime, difference] # add a row to the summary table with the calculated metrics
    return detail_table, summary_table
