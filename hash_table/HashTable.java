import java.util.LinkedList;

class Main {
  public static void main(String[] args) {
    // create a new hash map
    HashTable<String, Integer> map = new HashTable(2, 0.75f);
    System.out.println("INITIAL STATE:");
    System.out.println(map.print());

    // fill map with fruits
    put(map, "apple", 1);
    put(map, "banana", 2);
    put(map, "orange", 3);
    put(map, "grapes", 4);

    // update value of orange
    put(map, "orange", 8);

    // remove apple
    remove(map, "apple");

    // get value of banana and orange
    System.out.println("READ VALUES:");
    System.out.println("banana: " + map.get("banana"));
    System.out.println("orange: " + map.get("orange"));
  }

  // wrappers with print:
  private static void put(HashTable<String, Integer> ht, String k, Integer v) {
    System.out.println("INSERTING: " + k + "=" + String.valueOf(v));
    ht.put(k, v);
    System.out.println(ht.print());
  }

  private static void remove(HashTable<String, Integer> ht, String k) {
    System.out.println("REMOVING: " + k);
    ht.remove(k);
    System.out.println(ht.print());
  }
}

class HashTable<K, V> {
  private static final int DEFAULT_CAPACITY = 16;
  private static final float DEFAULT_LOAD_FACTOR = 0.75f;

  private int capacity;
  private float loadFactor;
  private int size;
  private LinkedList<Node<K, V>> table[];

  public HashTable() {
    this(DEFAULT_CAPACITY, DEFAULT_LOAD_FACTOR);
  }

  public HashTable(int capacity, float loadFactor) {
    this.capacity = capacity;
    this.loadFactor = loadFactor;

    this.table = new LinkedList[capacity];
  }

  private static class Node<K, V> {
    final K key;
    V value;

    Node(K key, V value) {
      this.key = key;
      this.value = value;
    }
  }

  private int hash(K key, int cap) {
    // make hashcode positive and make sure it fits into the table
    return (key.hashCode() & 0xfffffff) % cap;
  }

  // inserts node into the provided table
  private void insert(LinkedList<Node<K, V>> tbl[], int index, Node<K, V> node) {
    // get a bucket with the hash (create one if it doesn't exist)
    LinkedList<Node<K, V>> bucket = tbl[index];
    if (bucket == null) {
      bucket = new LinkedList<Node<K, V>>();
      tbl[index] = bucket;
    }

    // check if key is already in the bucket and just update it.
    for (Node<K, V> n : bucket) {
      if (n.key.equals(node.key)) {
        n.value = node.value;
        return;
      }
    }

    // otherwise add a new entry to bucket
    bucket.add(node);
  }

  public void put(K key, V value) {
    // check if we need to resize
    this.size += 1;
    if (this.size > this.capacity * this.loadFactor) {
      resize();
    }

    this.insert(this.table, this.hash(key, this.capacity), new Node<K, V>(key, value));
  }

  public V get(K key) {
    // get a bucket with the hash
    int index = this.hash(key, this.capacity);
    LinkedList<Node<K, V>> bucket = this.table[index];

    if (bucket == null) {
      return null;
    }

    // find the key in the bucket
    for (Node<K, V> node : bucket) {
      if (node.key.equals(key)) {
        return node.value;
      }
    }

    return null;
  }

  public void remove(K key) {
    // get a bucket with the hash
    int index = this.hash(key, this.capacity);
    LinkedList<Node<K, V>> bucket = this.table[index];

    if (bucket == null) {
      // key already removed
      return;
    }

    // find the key and remove the node.
    for (Node<K, V> node : bucket) {
      if (node.key.equals(key)) {
        bucket.remove(node);
        this.size -= 1;
        return;
      }
    }
  }

  private void resize() {
    int newCapacity = this.capacity * 2;

    LinkedList<Node<K, V>> newTable[] = new LinkedList[newCapacity];

    for (LinkedList<Node<K, V>> bucket : this.table) {
      if (bucket == null) {
        continue;
      }

      for (Node<K, V> node : bucket) {
        int index = this.hash(node.key, newCapacity);
        this.insert(newTable, index, node);
      }
    }

    this.table = newTable;
    this.capacity = newCapacity;
  }

  public String print() {
    String out = "";

    for (int i = 0; i < this.capacity; i++) {
      LinkedList<Node<K, V>> bucket = this.table[i];
      out += "[" + i + "]";
      if (bucket == null || bucket.size() == 0) {
        out += "\n";
        continue;
      }

      out += " ->";
      for (Node<K, V> node : bucket) {
        out += " (" + node.key + ": " + node.value + ")";
      }
      out += "\n";
    }

    return out;
  }
}
