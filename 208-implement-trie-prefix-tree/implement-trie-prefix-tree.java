class Trie {

    private static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isEndOfWord = false;
    }

    private final TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        if (word == null) return;
        
        TrieNode current = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            current = current.children.computeIfAbsent(ch, c -> new TrieNode());
        }
        current.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode node = findNode(word);
        return node != null && node.isEndOfWord;
    }

    public boolean startsWith(String prefix) {
        return findNode(prefix) != null;
    }

    private TrieNode findNode(String str) {
        if (str == null) return null;
        
        TrieNode current = root;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            current = current.children.get(ch);
            if (current == null) {
                return null;
            }
        }
        return current;
    }
}