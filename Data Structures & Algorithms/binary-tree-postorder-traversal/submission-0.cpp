class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        dfs(root, ans);
        return ans;
    }

    void dfs(TreeNode* node, vector<int>& ans) {
        if (!node) return;

        dfs(node->left, ans);
        dfs(node->right, ans);
        ans.push_back(node->val);
    }
};