class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> st;
        TreeNode* lastVisited = nullptr;

        while (root || !st.empty()) {
            while (root) {
                st.push(root);
                root = root->left;
            }

            TreeNode* node = st.top();

            if (node->right && lastVisited != node->right) {
                root = node->right;
            } else {
                result.push_back(node->val);
                lastVisited = node;
                st.pop();
            }
        }

        return result;
    }
};