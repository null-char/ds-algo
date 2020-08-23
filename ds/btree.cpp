#include <iostream>

// Binary tree implementation in C++

class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node(int newVal) {
        val = newVal;
        left = NULL;
        right = NULL;
    }
};

class BinaryTree {
public:
    BinaryTree() {
        root = NULL;
    }

    ~BinaryTree() {
        destroyTree();
    }

    /// Destroys the binary tree from the root to all its leaves.
    void destroyTree() {
        destroyTree(root);
    }

    void insert(int val) {
        if (root == NULL) {
            root = new Node(val);
        } else {
            insert(val, root);
        }
    }

    Node* search(int val) {
        return search(val, root);
    }

private:
    Node* root;

    // Internal overload for deleting specific nodes.
    // Recursively delete each of the specified node's children exhaustively.
    void destroyTree(Node* node) {
        if (node != NULL) {
            destroyTree(node->right);
            destroyTree(node->left);
            delete node;
        }
    }

    void insert(int val, Node* node) {
        if (val < node->val) {
            if (node->left != NULL) {
                insert(val, node->left);
            } else {
                node->left = new Node(val);
            }
        } else if (val >= node->val) {
            if (node->right != NULL) {
                insert(val, node->right);
            } else {
                node->right = new Node(val);
            }
        }
    }

    Node* search(int val, Node* node) {
        if (node != NULL) {
            if (val == node->val) {
                return node;
            } else if (val < node->val) {
                return search(val, node->left);
            } else {
                return search(val, node->right);
            }
        }

        return NULL;
    }
};

int main() {
    BinaryTree* btree = new BinaryTree();
    btree->insert(10);
    // Value of node to find
    const int v = 10;
    Node* n = btree->search(v);

    if (n != NULL) {
        printf("Found node with value %d", v);
    } else {
        printf("Required node with value %d not found", v);
    }

    delete btree;
}