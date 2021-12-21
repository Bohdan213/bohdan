#include<iostream>
#include<queue>
#include<vector>
#include<math.h>
using namespace std;
int main() {
	freopen("example3.csv", "r", stdin);
	int n;
	double step;
	cin >> n >> step;
    	int FROM_i, FROM_j, TO_i, TO_j;
    	cin >> FROM_i >> FROM_j;
	cin >> TO_i >> TO_j;
	vector<vector<double> > arr(n, vector<double>(n));
	for(int i = 0;i < n; ++i)
	{
		for(int j = 0;j < n; ++j)	
		{
			scanf("%lf",&arr[i][j]);
		}
	}
	fclose(stdin);
    	vector<vector<double> > dist(n, vector<double>(n, INT_MAX));
	vector<int> p(n*n);
   	dist[FROM_i][FROM_j]=0;
    	priority_queue<pair<double, pair<int, int> > > q;
    	q.push(make_pair(0,make_pair(FROM_i, FROM_j)));
    	while(!q.empty())
    	{
        	pair<double, pair<int, int> > front = q.top();
        	int from_i = front.second.first;
        	int from_j = front.second.second;
        	double len = -front.first;
 		if(from_i == TO_i && from_j == TO_j)  {
			break;
		}
		q.pop();
 		if (len > dist[from_i][from_j])  {
			continue;
		}
        	if((from_i - 1) >= 0)  {
			int to_i = from_i-1;
			int to_j = from_j;
	        	double cost = pow(pow(abs(arr[from_i - 1][from_j] - arr[from_i][from_j]),2) + pow(step,2),1.0/2);
        		if(dist[to_i][to_j] > len + cost) {
        	    		dist[to_i][to_j] = len + cost;
        	    		q.push(make_pair(-dist[to_i][to_j],make_pair(from_i-1,from_j)));
        	    		p[to_i * n + to_j] = from_i * n + from_j;
        		}
		}
		if(from_i + 1 < n)
		{
			int to_i = from_i+1;
			int to_j = from_j;
	        	double cost = pow(pow(abs(arr[from_i + 1][from_j] - arr[from_i][from_j]),2) + pow(step,2),1.0/2);
        		if(dist[to_i][to_j] > len + cost) {
        	    	dist[to_i][to_j] = len + cost;
        	    	q.push(make_pair(-dist[to_i][to_j],make_pair(from_i+1,from_j)));
        	    	p[to_i * n + to_j] = from_i * n + from_j;
        		}
		}
		if(from_j - 1 >= 0)
		{
			int to_i = from_i;
			int to_j = from_j-1;
	        	double cost = pow(pow(abs(arr[from_i][from_j-1] - arr[from_i][from_j]),2) + pow(step,2),1.0/2);
        		if(dist[to_i][to_j] > len + cost) {
        	    	dist[to_i][to_j] = len + cost;
        	    	q.push(make_pair(-dist[to_i][to_j],make_pair(from_i,from_j-1)));
        	    	p[to_i * n + to_j] = from_i * n + from_j;
        		}
		}
		if(from_j + 1 < n)
		{
			int to_i = from_i;
			int to_j = from_j+1;
	        	double cost = pow(pow(abs(arr[from_i][from_j+1] - arr[from_i][from_j]),2) + pow(step,2),1.0/2);
        		if(dist[to_i][to_j] > len + cost) {
        	    	dist[to_i][to_j] = len + cost;
        	    	q.push(make_pair(-dist[to_i][to_j],make_pair(from_i,from_j+1)));
        	    	p[to_i * n + to_j] = from_i * n + from_j;
        		}
		}
    	}
	int TO = TO_i * n + TO_j;
    	vector<int> put(1, TO);
    	int FROM = FROM_i * n + FROM_j;
   	p[FROM] = -1;
	while(p[TO] != -1) {
	    	TO = p[TO];
	   	put.push_back(TO);
	}
	freopen("answ.txt", "w", stdout);
	printf("%.9lf\n", dist[TO_i][TO_j]);
    	for(int i = put.size()-1; i >= 0; --i) {
		cout << put[i] / n << ' ' <<  put[i] % n  << endl;
	}
	fclose(stdout);
	return 0;
}
