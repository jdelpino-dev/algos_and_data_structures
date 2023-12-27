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
    if (!this.head) throw new Error('List is empty');
    // Initialize curr and prev pointers
    let curr = this.head;
    let prev = null;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
      this.length--;
      return curr.val;
    }

    // Traverse to the end of the list
    while (curr.next) {
      prev = curr;
      curr = curr.next;
    }

    // Set the tail to the node previous to the last node
    this.tail = prev;
    this.tail.next = null;

    // Decrement the length by 1
    this.length--;

    // Return the value of the last node
    return curr.val;
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

    let curr = this.head;
    let counter = 0;

    while (counter < idx) {
      curr = curr.next;
      counter++;
    }

    return curr.val;
  }

  /** setAt(idx, val): set val at idx to val
   * @param {number} idx
   * @param {any} val
   */
  setAt(idx, val) {
    if (idx >= this.length) throw new Error('Index out of bounds');

    let curr = this.head;
    let counter = 0;

    while (counter < idx) {
      curr = curr.next;
      counter++;
    }

    curr.val = val;
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

    let curr = this.head;
    let counter = 0;

    while (counter < idx - 1) {
      curr = curr.next;
      counter++;
    }

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

    let curr = this.head;
    let counter = 0;

    while (counter < idx - 1) {
      curr = curr.next;
      counter++;
    }

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
