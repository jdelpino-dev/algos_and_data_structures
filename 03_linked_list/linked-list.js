// LinkedList Implementation

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

  /** getNodeAt(idx): retrieve node at idx.
   * @param {number} idx
   * @return {Node}
   */
  getNodeAt(idx) {
    if (idx >= this.length) throw new Error('Index out of bounds');

    let curr = this.head;
    for (let i = 0; i < idx; i++) {
      curr = curr.next;
    }

    return curr;
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
    this.length++;
  }

  /** unshift(val): Add new value to start of list.
   * @param {any} val
   */
  unshift(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    }
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
  }

  /** pop(): return & remove last item, that is, the tail of the linked list.
   * Throws error if list is empty.
   * @return {any}
   */
  pop() {
    // If the list is empty, throw an error
    if (!this.head) throw new Error('List is empty');

    // If the list has a length of 1, set the head and tail to null
    if (this.length === 1) {
      const curr = this.head;
      this.head = null;
      this.tail = null;
      this.length--;
      return curr.val;
    }

    // Otherwise traverse the list to get the last and second to last nodes
    const secondToLast = this.getNodeAt(this.length - 2);
    const last = secondToLast.next;

    // Set the tail to the node previous to the last node
    this.tail = secondToLast;
    this.tail.next = null;

    // Decrement the length by 1
    this.length--;

    // Return the value of the last node
    return last.val;
  }

  /** shift(): return & remove first item.
   * Throws error if list is empty.
   * @return {any}
   */
  shift() {
    if (!this.head) throw new Error('List is empty');

    const val = this.head.val;
    this.head = this.head.next;
    this.length--;

    if (this.length === 0) {
      this.tail = null;
    }

    return val;
  }

  /** getAt(idx): get val at idx.
   * @param {number} idx
   * @return {any}
   */
  getAt(idx) {
    if (idx >= this.length) throw new Error('Index out of bounds');

    return this.getNodeAt(idx).val;
  }

  /** setAt(idx, val): set val at idx to val
   * @param {number} idx
   * @param {any} val
   */
  setAt(idx, val) {
    if (idx >= this.length) throw new Error('Index out of bounds');

    this.getNodeAt(idx).val = val;
  }

  /** insertAt(idx, val): add node w/val before idx.
   * @param {number} idx
   * @param {any} val
   */
  insertAt(idx, val) {
    // If the index is greater than the length, throw an error
    if (idx >= this.length + 1) throw new Error('Index out of bounds');

    // If the list is empty, or the index is the same as the length,
    // push a new node to the end of the list
    if (this.length === 1 || idx === this.length) {
      this.push(val);
      return;
    }

    // If the index is 0, unshift a new node to the start of the list
    if (idx === 0) {
      this.unshift(val);
      return;
    }

    // Otherwise, traverse the list to the node before the index
    let curr = this.getNodeAt(idx - 1);

    const newNode = new Node(val);
    newNode.next = curr.next;
    curr.next = newNode;

    this.length++;
  }

  /** removeAt(idx): return & remove item at idx.
   * @param {number} idx
   * @return {any}
   */
  removeAt(idx) {
    // If the index is greater than the length, throw an error
    if (idx >= this.length) throw new Error('Index out of bounds');

    // If the index is 0, shift a node from the start of the list
    if (idx === 0) return this.shift();

    // If the index is the same as the length-1 or the list has a length of 1,
    // pop a node from the end of the list
    if (idx === this.length - 1) return this.pop();

    // Otherwise, traverse the list to the node before the index
    let curr = this.getNodeAt(idx - 1);

    val = curr.next.val;
    curr.next = curr.next.next;

    this.length--;

    return val;
  }

  /** average(): return an average of all values in the list
   * @return {number}
   */
  average() {
    if (!this.head) return 0;

    let curr = this.head;
    let sum = 0;

    while (curr) {
      sum += curr.val;
      curr = curr.next;
    }

    return sum / this.length;
  }
}

/** Node: node for a singly linked list.
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

export default LinkedList;
