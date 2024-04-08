/* The knows API is defined for you.
      bool knows(int a, int b); */

// O(n^2) time and O(n^2) calls to knows()
class Solution1 {
public:
    int findCelebrity(int n) {
        
        // O(n^2) time and O(n^2) calls to knows()
        vector<vector<int>> trust;
        for(int p1 = 0; p1 < n; p1++) {
            for(int p2 = p1 + 1; p2 < n; p2++) {
                if(knows(p1, p2)) trust.push_back({p1, p2});
                if(knows(p2, p1)) trust.push_back({p2, p1});
            } 
        }
        
        // O(n + m) <= O(n^2) time
        int m = trust.size();
        vector<int> p_trusts(n, 0), trusts_p(n, 0);
        for(int i = 0; i < m; i++) {
            int ai = trust[i][0], bi = trust[i][1];
            p_trusts[ai]++;
            trusts_p[bi]++;
        }
        
        // O(n) time
        for(int p = 0; p < n; p++) {
            if(p_trusts[p] == 0 && trusts_p[p] == n-1) {
                return p;
            }
        }
        return -1;
    }
};

// O(n) time with at most 3n-3 calls to knows()
class Solution {
public:
    int findCelebrity(int n) {
        int celeb = 0;
        for(int p = 1; p < n; p++) {
            if(knows(celeb, p)) celeb = p;
        }
        
        for(int p = 0; p < n; p++) {
            if(p != celeb) {
                if(knows(celeb, p)) return -1;
                if(knows(p, celeb) == false) return -1;
            }
        }
        return celeb;
    }
};
