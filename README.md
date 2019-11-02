# How it works
This is an iterative greedy node network generation algorithm that will attempt to continue building a "best value" node network until terminated.  The initial state is determined by nodes that you configure as required in **gen_nodes_main**.  The program will then check all combinations of node:city for required nodes + 1 node from the rest of the graph, iterating through all possible +1 nodes.  After all +1 nodes are calculated, the best node is added to the required nodes and the program iteratively decides the next +1 node.

The following optimizations are done to speed up possible network generation:
* A number of nodes, proportional to your goal cp investment, are removed from consideration in the initial iterative step as they will be selected during the greedy step when the graph is filled in.
* a number of nodes whose value/cp ratio are quite low are removed from initial consideration, as they don't appear appear in final graphs.  However these nodes are still considered for the greedy step when the graph is filled in.  EG Roud Sulfur Mining, that isn't selected even if Roud Sulphur is a required node.
* A limited subset of node:city connections are considered per node.  As you are not likely to connect Star's End to Valencia.

Example output for a 200 cp network that takes Heidel 7-4 2f Workshop and doesn't have p2w housing is included as an example.  It will not be updated as market conditions change.  Was ran until the first +1 node was found.

# Running
Requires Python 3.6 or newer due to use of f-string.  As of 2019/7/10, does not work with pypy3 due to a lack of Pool support.  Program uses multiprocessing to calculate multiple graphs at once, so it will spawn cpu_count-2 workers, with a minimum worker count of 1.

Program will run until stopped[1] while keeping track of the best result seen so far, however starting a new instance will begin again from the initial state.

[1] Program will terminate if a round of +1 node did not generate a better graph than the previous round of +1.  The example setup will terminate after attempting to find an 8th node, as there are none available that make the graph better than the 7th round result.

# Configuration
**items.csv** and **gen_nodes_main.py** are the 2 files that are intended to be modified by a user of this program.  **visualize.py** is a helper file to create a graph of the selected nodes in order to more easily find them.

**items.csv** is a snapshot of current item prices on the Central Market.  If an item does not sell, or you do not want that item to be considered, set its value to 0.  If a production node has only 0 value output, it will be ignored for graph generation

**gen_nodes_main** is where you configure the settings to match your desired output.  
* required output: select all nodes that have the required output.  See items.csv for names.
* required nodes(that have output): see resources_mine/hr_cleaned_nodes for node ids.  Set specific resource nodes as required for your network.
* required monster nodes:  Intended for non-resource nodes as it will overwrite output if you select a resource node.  Does not allocate a worker to that node.
* See additional comments in that file for other configuration options.

# Example advanced configuration
If you, like me, use the Heidel tool/clothing shop in 7-4 2F, you will need to make some minor modifications to get correct graphs.  First subtract the cost of that housing chain from your available cp(8) and then add any lodging on that chain to your free lodging(4), finally subtract 1 from lodging for your worker that will be in the workshop.  In summary you would subtract 8 from your total cp, and add 3 to your bonus Heidel lodging.  If you also had the p2w lodging, that means you would set your Heidel lodging to 6 in **gen_nodes_main**.

# Disclaimers
Node layout is from http://www.somethinglovely.net/bdo/ with minor cleanup to some node names and missing node connections.

Node yield is from https://www.bdodae.com/nodes/ with minor cleanup to remove unnecessary node:city connections and change some node names.