#include <unordered_map>
#include <algorithm>
using namespace std;

constexpr int MAX_DEVICE = 10005;
int root, id; 

int parent[MAX_DEVICE];
int distToParent[MAX_DEVICE];
int depth[MAX_DEVICE];

int firstID[MAX_DEVICE], secondID[MAX_DEVICE];            
int firstLatency[MAX_DEVICE], secondLatency[MAX_DEVICE]; 

unordered_map<int, int> idmap;

void init(int mDevice)
{
	for (int i = 0; i <= id; ++i) {
		firstLatency[i] = secondLatency[i] = 0;
	}
	root = id = 1;
	idmap.clear();
	idmap[mDevice] = id;
}

void update(int pid, int cid) {
	int distSum = 0;
	while (pid) {                                 
		distSum += distToParent[cid];
		if (firstID[pid] == cid) {                
			if (firstLatency[pid] < distSum)         
				firstLatency[pid] = distSum;
			else
				break;                         
		}
		else if (firstLatency[pid] < distSum) {     
			secondLatency[pid] = firstLatency[pid];
			secondID[pid] = firstID[pid]; 
			firstLatency[pid] = distSum;
			firstID[pid] = cid;                   
		}
		else if (secondLatency[pid] < distSum) {      
			secondLatency[pid] = distSum;
			secondID[pid] = cid;
		}
		else
			break;                             

		cid = pid;
		pid = parent[pid];                
	}
}

void connect(int mOldDevice, int mNewDevice, int mLatency)
{
	int old_device_id = idmap[mOldDevice];                  
	int new_device_id = ++id;

	idmap[mNewDevice] = new_device_id;                      
	
	parent[new_device_id] = old_device_id;
	depth[new_device_id] = depth[old_device_id] + 1;  
	distToParent[new_device_id] = mLatency;          

	update(old_device_id, new_device_id);
}

int measure(int mDevice1, int mDevice2)          
{
	int sid = idmap[mDevice1];
	int eid = idmap[mDevice2];

	if (depth[sid] > depth[eid]) swap(sid, eid);  
	int diff = depth[eid] - depth[sid];           
	int ret = 0;
	while (diff--) {                             
		ret += distToParent[eid];                   
		eid = parent[eid];                           
	}
	while (sid != eid) {                          
		ret += distToParent[sid] + distToParent[eid];   
		sid = parent[sid], eid = parent[eid];          
	}
	return ret;
}

int test(int mDevice)
{
	int mid = idmap[mDevice];
	int pid = parent[mid];
	int ret = firstLatency[mid] + secondLatency[mid];  

	int distSum = firstLatency[mid];                  
	while (pid) {                               
		distSum += distToParent[mid];
		if (secondLatency[pid]) {                    
			if (firstID[pid] == mid)              
				ret = max(ret, distSum + secondLatency[pid]);  
			else                                  
				ret = max(ret, distSum + firstLatency[pid]);  
		}
		else {
			ret = max(ret, distSum);              
		}
		mid = pid, pid = parent[pid];               
	}

	return ret;
}