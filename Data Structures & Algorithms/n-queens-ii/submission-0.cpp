class Solution {
public:
    int ans = 0;

    void dfs(int row, int n,
             vector<int>& cols,
             vector<int>& diag1,
             vector<int>& diag2) {

        if (row == n) {
            ans++;
            return;
        }

        for (int col = 0; col < n; col++) {
            int d1 = row - col + n - 1;
            int d2 = row + col;

            if (cols[col] || diag1[d1] || diag2[d2])
                continue;

            cols[col] = diag1[d1] = diag2[d2] = 1;

            dfs(row + 1, n, cols, diag1, diag2);

            cols[col] = diag1[d1] = diag2[d2] = 0;
        }
    }

    int totalNQueens(int n) {
        vector<int> cols(n, 0);
        vector<int> diag1(2 * n - 1, 0);
        vector<int> diag2(2 * n - 1, 0);

        dfs(0, n, cols, diag1, diag2);
        return ans;
    }
};