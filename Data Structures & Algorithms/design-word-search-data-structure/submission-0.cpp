class WordDictionary {
private:
    struct TrieNode {
        TrieNode* children[26];
        bool isEnd;

        TrieNode() {
            for (int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
            isEnd = false;
        }
    };

    TrieNode* root;

    bool dfs(string& word, int idx, TrieNode* node) {
        if (idx == word.size()) {
            return node->isEnd;
        }

        char c = word[idx];

        if (c == '.') {
            for (int i = 0; i < 26; i++) {
                if (node->children[i] &&
                    dfs(word, idx + 1, node->children[i])) {
                    return true;
                }
            }
            return false;
        }

        int child = c - 'a';

        if (!node->children[child]) {
            return false;
        }

        return dfs(word, idx + 1, node->children[child]);
    }

public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* node = root;

        for (char c : word) {
            int idx = c - 'a';

            if (!node->children[idx]) {
                node->children[idx] = new TrieNode();
            }

            node = node->children[idx];
        }

        node->isEnd = true;
    }

    bool search(string word) {
        return dfs(word, 0, root);
    }
};
