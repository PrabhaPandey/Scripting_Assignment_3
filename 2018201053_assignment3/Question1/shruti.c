#include <bits/stdc++.h>
using namespace std;
/*------- Constants---- */
 
#define Long                    long long
#define Ulong                   unsigned long long
#define forn(i,n)               for( int i=0 ; i < n ; i++ )
#define mp(i,j)                 make_pair(i,j)
#define pb(a)                   push_back((a))
#define all(x)                  (x).begin(),(x).end()
#define gc                      getchar_unlocked
#define PI                      acos(-1.0)
#define EPS                     1e-9
#define xx                      first
#define yy                      second
#define lc                      ((n)<<1)
#define rc                      ((n)<<1|1)
#define db(x)                   cout << #x << " -> " << x << endl;
#define Di(x)                   int x;scanf("%d",&x)
#define min(a,b)                ((a)>(b) ? (b) : (a) )
#define max(a,b)                ((a)>(b) ? (a):(b))
#define ms(ara_name,value)      memset(ara_name,value,sizeof(ara_name))
 
/*************************** END OF TEMPLATE ****************************/
 
const int N = 4e5+5;
int n,q;
int a[N],b[N];
int sz;
vector<int>v;
int root[N];
// struct Node{
//     int ls,rs,cnt;
// }node[N*20];
struct node{
    struct node* children[2];
    bool is_leaf;
}node[N*20];
/*
struct node{
    int value;
    // struct node *left;
    // struct node *right;
    struct node* children[2];
    bool is_leaf;
}

struct node* versions[5];

struct node* create_node(){
    struct node * new_node=new struct node*;
    new_node->children[0]=NULL;
    new_node->children[1]=NULL;
    is_leaf=false;
}

string getBinary(int num){
    string result;
    while(num!=0){
        result+=to_string(num%10);
        num/=10;
    }
    while(result.length()!=32){
        result+='0';
    }
    reverse(result.begin(),result.end());
    return result;
}

void insert_normal(struct node* root,int key){
    string binary=getBinary(key);
    struct node* crawl=root;
    for (int i = 0; binary[i]!='\0'; ++i)
    {
        int indx=binary[i]-'0';
        if(crawl->children[indx]==NULL){
            crawl->children[indx]=create_node;
        }
        crawl=crawl->children[indx];
    }
    crawl->is_leaf=true;
}
*/
void insert(struct node* prevVersion,struct node* newVersion,int key){
    string binary=getBinary(key);
    struct node*new_crawler=newVersion;
    struct node*prev_crawler=prevVersion;
    for(int i=0;binary[i]!='\0';i++){
        int indx=binary[i]-'0';
        new_crawler->children[indx]=create_node();
        new_crawler->children[!indx]=prev_crawler->children[!indx];
        new_crawler=new_crawler->children[index];
        prev_crawler=prev_crawler->children[indx];
    }
    new_crawler->is_leaf=true;
}


void update(int &n,int pre,int b,int e,int pos)
{//added pre,pos and replaced n with &n
    cout<<"in update: "<<"pre: "<<pre<<" b: "<<b<<" e: "<<e<<" pos: "<<pos<<endl;
    n = ++sz; //new step

    node[n] = node[pre]; //new step
    if(b==e && b== pos) {
        node[n].cnt ++;//new
        node[n].ls = node[n].rs = 0;//earlier simple push back
        return;
    }
    int mid = (b+e)/2;
    if(pos<= mid) update(node[n].ls, node[pre].ls, b, mid,pos);
    else update(node[n].rs, node[pre].rs, mid+1,e,pos);
    node[n].cnt = node[node[n].ls].cnt + node[node[n].rs].cnt;
}
 
int query(int r1,int r2, int b,int e,int x )
{
    if(b==e) return b;
    int oo = node[node[r1].ls].cnt - node[node[r2].ls].cnt;
    int mid = (b+e)/2;
    if(oo >= x) return query(node[r1].ls, node[r2].ls,b, mid,x);
    else return query(node[r1].rs , node[r2].rs, mid+1,e,x - oo );
}
int main()
{
    //freopen("in.txt","r",stdin);
    scanf("%d %d",&n,&q);
    for(int i = 1; i <= n; i ++ ) {
        scanf("%d",&a[i]);
        v.pb(a[i]);
    }
    cout<<"SORTING"<<endl;
    sort(all(v));
    for(int i = 1;i <= n; i ++ ) {
        a[i] = lower_bound(all(v),a[i]) - v.begin() + 1;
    }
    int S = v.size();
    update(root[1], 0, 1, S,a[1]); // 0 -> is the initial empty segment tree
    for(int i = 2; i <= n; i ++ ) {
        update(root[i], root[i-1],1,S,a[i]);
    }
     
    while(q--) {
        int l,r,x;
        scanf("%d %d %d",&l,&r,&x);
        int k = query(root[r], root[l-1], 1,S,x);
        printf("%d\n",v[k-1]);
    }
    return 0;
}