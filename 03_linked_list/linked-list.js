/** Node: node for a singly linked list. */

/** Node: constructor for node class.
 * @property {any} val
 * @property {Node} next
 */
class Node {
  /**
   * Constructs a new node with the given value.
   * @param {any} val
   */
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

/** LinkedList: chained together nodes. */

/** LinkedList: chained together nodes.
 * @property {Node} head
 * @property {Node} tail
 * @property {number} length
 */
class LinkedList {
  /**
   * Constructs a new linked list instance.
   * @param {any[]} vals
   */
  constructor(vals = []) {
    this.head = null;
    this.tail = null;
    this.length = 0;

    for (const val of vals) this.push(val);
  }

  /** Add new value to end of list.
   * @param {any} val
   */
  push(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  /** unshift(val): add new value to start of list. */

  unshift(val) {}

  /** pop(): return & remove last item. */

  pop() {}

  /** shift(): return & remove first item. */

  shift() {}

  /** getAt(idx): get val at idx. */

  getAt(idx) {}

  /** setAt(idx, val): set val at idx to val */

  setAt(idx, val) {}

  /** insertAt(idx, val): add node w/val before idx. */

  insertAt(idx, val) {}

  /** removeAt(idx): return & remove item at idx, */

  removeAt(idx) {}

  /** average(): return an average of all values in the list */

  average() {}
}

export default LinkedList;
